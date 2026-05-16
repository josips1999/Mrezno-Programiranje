
Lab 4 — Socket programming in Python
====================================

This folder contains examples for UDP and TCP echo servers and clients.

Files
- local_machine_info.py — helper to print hostname and IP address
- server_udp.py — simple UDP server (port 65433)
- client_udp.py — UDP client to send messages to server
- echo_server.py — TCP echo server (port 65432)
- echo_client.py — TCP client for the echo server

Running

1) UDP server/client

Start the UDP server in a terminal:

```bash
python3 sockets-lab/server_udp.py
```

Run the UDP client in another terminal:

```bash
python3 sockets-lab/client_udp.py
```

2) TCP echo server/client

Start the TCP echo server:

```bash
python3 sockets-lab/echo_server.py
```

Run the TCP client:

```bash
python3 sockets-lab/echo_client.py
```

Notes
- Type `exit` in clients to quit.
- `echo_server.py` treats the exact message `vaše_ime_prezime` as unsupported and returns `Unos nije podržan.`
- All programs import and call `print_machine_info()` at startup to show hostname and IP.

Examples

1) UDP example

Start server:

```bash
python3 sockets-lab/server_udp.py
```

Server console (example):

```
Host name: workspace
IP address: 127.0.0.1
UDP server listening on 0.0.0.0:65433
[2026-05-16 19:20:00.123456] Received from 127.0.0.1:52345: hello
```

Run client and send `hello`:

```bash
python3 sockets-lab/client_udp.py
```

Client console (example):

```
Host name: workspace
IP address: 127.0.0.1
Message (or 'exit' to quit): hello
Received: ACK: hello
```

2) TCP Echo example

Start server:

```bash
python3 sockets-lab/echo_server.py
```

Server console (example):

```
2026-05-16 19:21:00.123456
Host name: workspace
IP address: 127.0.0.1
TCP Echo server listening on 0.0.0.0:65432
Connected by ('127.0.0.1', 52346)
[2026-05-16 19:21:05.654321] From 127.0.0.1:52346 -> test message
```

Run client and send `test message`:

```bash
python3 sockets-lab/echo_client.py
```

Client console (example):

```
Message (or 'exit' to quit): test message
Received: test message
```

Screenshots / sample outputs

Sample console outputs are included in the repository under the `screenshots` folder as text files for convenience.


