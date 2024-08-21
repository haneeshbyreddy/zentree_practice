## OSI

- Application layer
    - Features
        - Data from User <=> Application layer
        - Provides different Protocols to user applications for network communication
    - Protocols
        - DHCP
        - FTP
        - SMTP
        - HTTP
- Presentation layer
    - Features
        - Carries out encryption and decryption and data compression
        - Data translation
    - Protocols
        - Encryption
            - LPP (Lightweight presentation protocol)
            - SSL (Secure Socket layer)
        - Translation
            - JSON
            - UTF
- Session layer
    - Features
        - Establishing and ending sessions
        - Synchronizing communication
        - Avoids conflict with tokens (control tokens, data tokens)
    - Protocols
        - NetBIOS (Network basic input/output system)
        - SCP (Session Control Protocol):
- Transport Layer
    - Features
        - End-to-end communication
        - Segmentation and reassembly of data
        - Flow control
        - Error control
    - Protocols
        - TCP (Transmission Control Protocol)
        - UDP (User Datagram Protocol)
- Network Layer
    - Features
        - Logical addressing
        - Routing
        - Path determination
    - Protocols
        - IP (Internet Protocol)
        - ICMP (Internet Control Message Protocol)
        - OSPF (Open Shortest Path First)
- Data Link Layer
    - Features
        - Physical addressing
        - Error detection and correction
        - Flow control
    - Protocols
        - PPP (Point-to-Point Protocol)
        - HDLC (High-Level Data Link Control)
- Physical Layer
    - Features
        - Transmission and reception of raw bit streams
        - Defines electrical and physical specifications
    - Standards/Technologies
        - Ethernet physical layer
        - USB
        - Bluetooth physical layer

## Data walkthrough in OSI

Application Data: "GET /index.html HTTP/1.1"
↓
Presentation Data: [Encrypted("GET /index.html HTTP/1.1")]
↓
Session Data: [Session Token][Encrypted("GET /index.html HTTP/1.1")]
↓
Transport Segment: [TCP Header][Session Token][Encrypted("GET /index.html HTTP/1.1")]
↓
Network Packet: [IP Header][TCP Header][Session Token][Encrypted("GET /index.html HTTP/1.1")]
↓
Data Link Frame: [Ethernet Header][IP Header][TCP Header][Session Token][Encrypted("GET /index.html HTTP/1.1")][Ethernet Trailer]
↓
Physical: 1010101110101010... (bits converted to signals)