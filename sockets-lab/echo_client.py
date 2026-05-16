import socket


def run_client(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        try:
            while True:
                msg = input("Message (or 'exit' to quit): ")
                if not msg:
                    continue
                if msg.lower() == 'exit':
                    break
                s.sendall(msg.encode())
                data = s.recv(1024)
                if not data:
                    print("Server closed connection")
                    break
                print("Received:", data.decode())
        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    run_client()
