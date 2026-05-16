from local_machine_info import print_machine_info
import socket
import datetime


def run_server(host='0.0.0.0', port=65433):
    print_machine_info()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))
    print(f"UDP server listening on {host}:{port}")
    try:
        while True:
            data, addr = sock.recvfrom(1024)
            now = datetime.datetime.now()
            msg = data.decode('utf-8', errors='replace')
            print(f"[{now}] Received from {addr[0]}:{addr[1]}: {msg}")
            ack = f"ACK: {msg}"
            sock.sendto(ack.encode(), addr)
    except KeyboardInterrupt:
        print("Shutting down UDP server")
    finally:
        sock.close()


if __name__ == '__main__':
    run_server()
