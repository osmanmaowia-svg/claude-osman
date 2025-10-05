# Google DNS Server Context for PA1-DNS

## Overview
This document provides comprehensive context on Google's public DNS server for the CS-455 PA1-DNS programming assignment.

## Google Public DNS Server Details

### Primary DNS Server
- **IP Address**: `8.8.8.8`
- **Secondary DNS**: `8.8.4.4`
- **IPv6 Support**: `2001:4860:4860::8888` and `2001:4860:4860::8844`

### Assignment Requirements
According to PA1-DNS specifications:
- **Required Server**: Must use Google's public DNS server `8.8.8.8` for grading
- **Protocol**: DNS uses UDP for message transfer
- **Port**: Standard DNS port 53
- **Timeout**: Implement 5-second timeout with 3 retry attempts
- **Testing**: Can use other DNS servers (like GMU's) for testing, but final submission must work with `8.8.8.8`

## Technical Implementation Notes

### UDP Socket Connection
```c
// Example connection setup
struct sockaddr_in dns_server;
dns_server.sin_family = AF_INET;
dns_server.sin_port = htons(53);  // Standard DNS port
inet_pton(AF_INET, "8.8.8.8", &dns_server.sin_addr);
```

### Timeout and Retry Logic
- Wait 5 seconds for response
- Retry up to 3 times if no response received
- Print timeout error message after 3 failed attempts

### DNS Message Format
- Query messages must adhere to RFC 1035 specifications
- Header section with ID, QR, OPCODE, RD, QDCOUNT fields
- Question section with QNAME, QTYPE, QCLASS fields
- Response processing for Answer, Authority, and Additional sections

## Why Google DNS for This Assignment

### Reliability
- Google's DNS infrastructure is highly reliable and globally distributed
- Provides consistent responses suitable for testing and grading
- Minimal downtime and latency issues

### Performance
- Optimized for speed with global edge locations
- Low response times for DNS queries
- Suitable for timeout testing requirements

### Standard Compliance
- Fully compliant with DNS protocol specifications
- Proper handling of malformed queries
- Consistent error responses for debugging

## Alternative DNS Servers (For Testing Only)

Based on research from [Lifewire's DNS server list](https://www.lifewire.com/free-and-public-dns-servers-2626062):

### Cloudflare DNS
- Primary: `1.1.1.1`
- Secondary: `1.0.0.1`

### OpenDNS
- Primary: `208.67.222.222`
- Secondary: `208.67.220.220`

### Quad9 DNS
- Primary: `9.9.9.9`
- Secondary: `149.112.112.112`

**Note**: While these can be used for testing, the assignment will only be graded against Google's `8.8.8.8` server.

## Common Issues and Troubleshooting

### Connection Problems
- Verify UDP socket creation and binding
- Check firewall settings that might block DNS traffic
- Ensure proper error handling for connection failures

### Timeout Issues
- Implement proper socket timeout using `setsockopt()` with `SO_RCVTIMEO`
- Test timeout functionality with invalid DNS server IPs
- Verify retry logic increments attempt counter correctly

### Message Format Errors
- Validate DNS message structure against RFC 1035
- Use Wireshark to compare your queries with standard DNS packets
- Check byte ordering (network byte order) for multi-byte fields

## Debugging with Wireshark

### Packet Capture Setup
1. Start Wireshark capture on your network interface
2. Filter for DNS traffic: `udp.port == 53`
3. Run your DNS client program
4. Analyze captured packets to verify message format

### Key Things to Verify
- DNS query message structure
- Proper QNAME encoding (length-prefixed labels)
- Correct header field values
- Response message parsing

## Testing Strategy

### Basic Functionality
1. Test with simple domains (e.g., `gmu.edu`, `google.com`)
2. Verify IP address extraction from response
3. Test timeout functionality with invalid server

### Edge Cases
1. Invalid domain names
2. Non-existent domains
3. Network connectivity issues
4. Malformed query messages

### Output Verification
Your program should display:
```
$> my-dns-client gmu.edu
Preparing DNS query..
Contacting DNS server..
Sending DNS query..
DNS response received (attempt 1 of 3)
Processing DNS response..
----------------------------------------------------------------------------
header.ID = <value>
header.QR = <value>
header.OPCODE = <value>
....
question.QNAME = <value>
question.QTYPE = <value>
question.QCLASS = <value>
....
answer.NAME = <value>
answer.TYPE = <value>
....
answer.RDATA = <value> ## resolved IP address ##
---------------------------------------------------------------------------
```

## References

- [RFC 1035 - Domain Names - Implementation and Specification](https://tools.ietf.org/html/rfc1035)
- [Google Public DNS](https://developers.google.com/speed/public-dns)
- [Lifewire: Free and Public DNS Servers](https://www.lifewire.com/free-and-public-dns-servers-2626062)
- [DNS Message Format Documentation](https://tools.ietf.org/html/rfc1035#page-25)

---

**Important**: This assignment requires working specifically with Google's DNS server `8.8.8.8`. While other DNS servers can be used for testing, the final implementation must work with this server for grading purposes.
