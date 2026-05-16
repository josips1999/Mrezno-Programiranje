import socket
import datetime
from local_machine_info import print_machine_info


def handle_client(conn, addr):
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            msg = data.decode('utf-8', errors='replace').strip()
            now = datetime.datetime.now()
            print(f"[{now}] From {addr[0]}:{addr[1]} -> {msg}")
            if msg == "vaše_ime_prezime":
                resp = "Unos nije podržan."
            else:
                resp = msg
            conn.sendall(resp.encode())


def run_server(host='0.0.0.0', port=65432):
    print(datetime.datetime.now())
    print_machine_info()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"TCP Echo server listening on {host}:{port}")
        try:
            while True:
                conn, addr = s.accept()
                handle_client(conn, addr)
        except KeyboardInterrupt:
            print("Shutting down TCP server")


if __name__ == '__main__':
    run_server()
