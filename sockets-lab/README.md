
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

