import socket


def print_machine_info():
    host_name = socket.gethostname()
    try:
        ip_address = socket.gethostbyname(host_name)
    except Exception:
        ip_address = 'Unknown'
    print(f"Host name: {host_name}")
    print(f"IP address: {ip_address}")
