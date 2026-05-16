from local_machine_info import print_machine_info
import socket


def run_client(server_host='127.0.0.1', server_port=65433):
    print_machine_info()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(5.0)
    try:
        while True:
            msg = input("Message (or 'exit' to quit): ")
            if not msg:
                continue
            if msg.lower() == 'exit':
                break
            sock.sendto(msg.encode(), (server_host, server_port))
            try:
                data, _ = sock.recvfrom(1024)
                print("Received:", data.decode())
            except socket.timeout:
                print("No response (timeout)")
    except KeyboardInterrupt:
        pass
    finally:
        sock.close()


if __name__ == '__main__':
    run_client()
