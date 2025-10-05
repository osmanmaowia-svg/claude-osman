#!/usr/bin/env python3

import sys
import socket
import struct
import random
import time

class DNSClient:
    def __init__(self):
        self.dns_server = "8.8.8.8"
        self.dns_port = 53
        self.timeout = 5
        self.max_attempts = 3
        
    def create_dns_query(self, hostname):
        print("Preparing DNS query..")

        query_id = random.randint(0, 65535)
        flags = 0x0100
        qdcount = 1
        ancount = 0
        nscount = 0
        arcount = 0
        
        header = struct.pack('!HHHHHH', query_id, flags, qdcount, ancount, nscount, arcount)
        
        qname = self.encode_domain_name(hostname)
        qtype = 1
        qclass = 1
        
        question = qname + struct.pack('!HH', qtype, qclass)
        dns_query = header + question
        
        self.query_id = query_id
        self.query_hostname = hostname
        
        return dns_query
    
    def encode_domain_name(self, hostname):
        encoded = b''
        labels = hostname.split('.')
        for label in labels:
            encoded += struct.pack('!B', len(label)) + label.encode('ascii')
        encoded += b'\x00'
        return encoded
    
    def send_query(self, dns_query):
        print("Contacting DNS server..")
        print("Sending DNS query..")
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(self.timeout)
        
        try:
            for attempt in range(1, self.max_attempts + 1):
                try:
                    sock.sendto(dns_query, (self.dns_server, self.dns_port))
                    response, addr = sock.recvfrom(512)
                    print(f"DNS response received (attempt {attempt} of {self.max_attempts})")
                    return response
                    
                except socket.timeout:
                    if attempt < self.max_attempts:
                        continue
                    else:
                        return None
                        
        finally:
            sock.close()
    
    def parse_response(self, response):
        print("Processing DNS response..")
        print("-" * 76)
        if len(response) < 12:
            return
        
        header_data = struct.unpack('!HHHHHH', response[:12])
        resp_id, flags, qdcount, ancount, nscount, arcount = header_data
        
        qr = (flags >> 15) & 1
        opcode = (flags >> 11) & 15
        aa = (flags >> 10) & 1
        tc = (flags >> 9) & 1
        rd = (flags >> 8) & 1
        ra = (flags >> 7) & 1
        z = (flags >> 4) & 7
        rcode = flags & 15
        
        print(f"header.ID = {resp_id}")
        print(f"header.QR = {qr}")
        print(f"header.OPCODE = {opcode}")
        print(f"header.AA = {aa}")
        print(f"header.TC = {tc}")
        print(f"header.RD = {rd}")
        print(f"header.RA = {ra}")
        print(f"header.Z = {z}")
        print(f"header.RCODE = {rcode}")
        print(f"header.QDCOUNT = {qdcount}")
        print(f"header.ANCOUNT = {ancount}")
        print(f"header.NSCOUNT = {nscount}")
        print(f"header.ARCOUNT = {arcount}")

        offset = 12
        if qdcount > 0:
            qname, offset = self.parse_domain_name(response, offset)
            if offset + 4 <= len(response):
                qtype, qclass = struct.unpack('!HH', response[offset:offset+4])
                offset += 4
                
                print(f"question.QNAME = {qname}")
                print(f"question.QTYPE = {qtype}")
                print(f"question.QCLASS = {qclass}")
        
        for i in range(ancount):
            if offset >= len(response):
                break
            name, offset = self.parse_domain_name(response, offset)
            if offset + 10 > len(response):
                break
                
            rr_type, rr_class, ttl, rdlength = struct.unpack('!HHIH', response[offset:offset+10])
            offset += 10
            if offset + rdlength > len(response):
                break
            rdata = response[offset:offset+rdlength]
            offset += rdlength
            
            print(f"answer.NAME = {name}")
            print(f"answer.TYPE = {rr_type}")
            print(f"answer.CLASS = {rr_class}")
            print(f"answer.TTL = {ttl}")
            print(f"answer.RDLENGTH = {rdlength}")
            
            if rr_type == 1 and rdlength == 4:
                ip_addr = socket.inet_ntoa(rdata)
                print(f"answer.RDATA = {ip_addr} ## resolved IP address ##")
            else:
                print(f"answer.RDATA = {rdata.hex()}")
        
        print("-" * 76)
    
    def parse_domain_name(self, response, offset):
        labels = []
        jumped = False
        original_offset = offset
        while offset < len(response):
            length = response[offset]
            if length == 0:
                offset += 1
                break
            elif (length & 0xC0) == 0xC0:
                if not jumped:
                    original_offset = offset + 2
                pointer = struct.unpack('!H', response[offset:offset+2])[0] & 0x3FFF
                offset = pointer
                jumped = True
            else:
                offset += 1
                if offset + length > len(response):
                    break
                labels.append(response[offset:offset+length].decode('ascii'))
                offset += length
        
        domain_name = '.'.join(labels) if labels else ''
        return domain_name, original_offset if jumped else offset
    
    def query_hostname(self, hostname):
        dns_query = self.create_dns_query(hostname)
        response = self.send_query(dns_query)
        
        if response:
            self.parse_response(response)

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    hostname = sys.argv[1]
    client = DNSClient()
    client.query_hostname(hostname)

if __name__ == "__main__":
    main()