1.  Service time at first tollbooth = 8 cars × 12 sec/car = 96 seconds
    Propagation delay between tollbooths = 75 km ÷ 175 km/hr = 3/7 hours = 1,542.86 seconds
    Last car arrives at second tollbooth = 96 + 1,542.86 = 1,638.86 seconds
    Last car finishes service at second tollbooth = 1,638.86 + 12 = 1,650.86 seconds
    Last car arrives at third tollbooth = 1,650.86 + 1,542.86 = 3,193.72 seconds
    Last car finishes service at third tollbooth = 3,193.72 + 12 = 3,205.72 seconds
    End-to-End delay = 3,205.72 sec = 53.43 minutes

2.  a) 1000 kilobit = 1 megabit
    R1 = 500 kbps
    R2 = 2 Mbps = 2,000 kbps
    R3 = 1 Mbps = 1,000 kbps
    Throughput = 500 kbps
    b) [2 pts] File size = 4 million bytes = 4,000,000 bytes = 32,000,000 bits
    Time = File size / throughput
    Time = 32,000,000 bits / 500000 bits/secs = 64 seconds

3.  
    a)
    1. dproc: nodal processing
    2. dqueue: queueing delay
    3. dtrans: transmission delay
    4. dprop: propagation delay

b) {"Constant delay": [dproc, dtrans, dprop], "Variable delay": [dqueue]}

4.  a) 16
    b) 4
    c) No
    B->A->D will requires 8 connections for A-B link when the link can only support 4
    B->C->D will require 8 connections for B-C link when the link can only support 4

5.  a) 2
    b)
    2 or few users: combined transmission rate is no larger than 2 Mbps which is the link capacity so packets can be transmitted immediately without queuing
    3+ users actively transmitting at the same time: combined transmision rate is 3+ Mbps > 2 Mbps link capacity causing packets to remain in queue

6.  For P packets sent back-to-back:

1st Packet: starts at time 0
2nd Packet: starts at time L/R
3rd Packet: starts at time 2(L/R)
Pth Packet: starts at time (P-1)\*(L/R) and takes N\*(L/R)

Total end-to-end delay = (P-1)\*(L/R) + N\*(L/R) = ((P-1)+N)\*(L/R)

7.  a)
    Transport Layer: file is divided into segments and header is added (port number, sequence numbers)
    Network layer: adds IP header creating packets
    File -> Segments -> Packets

    b) Router uses destination IP address in the packets network layer header to determine the outgoing link. Router checks this address against the forwarding table to find the next hop.

    c)

    - driver doesn't know complete route like how packets don't carry the full path
    - each router maeks independent forwarding decisions
    - packet determines its next hop using information at each router (does not know forwarding table when on the way)

8.  [5+2+2 pts] Consider a packet of length L that begins at end system A and travels over
    three links to a destination end system B. These three links are connected by two
    packet switches. Let di, si, and Ri denote the length, propagation speed, and the
    transmission rate of the link i, for i = 1, 2, 3. The packet switch delays each packet by
    dproc. Assuming no queuing delays, in terms of di, si, Ri, (i = 1, 2, 3), and L.
    System A
    System B
    a) L/R1 + L/R2 + L/R3 + d1/s1 + d2/s2 + d3/s3 + 2\*dproc
    b) No, Propagation delay = di/si which is independent of L
    c) No, Propagation delay = di/si which is independent of Ri
