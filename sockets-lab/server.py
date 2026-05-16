import socket

HOST = '0.0.0.0'
PORT = 65432


def run_server(host=HOST, port=PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen()
        print(f"[SERVER] Listening on {host}:{port}")

        conn, addr = s.accept()
        with conn:
            print(f"[SERVER] Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"[SERVER] Received: {data.decode()}")
                conn.sendall(data)


if __name__ == '__main__':
    run_server()
