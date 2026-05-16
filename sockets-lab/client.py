import socket

HOST = '127.0.0.1'
PORT = 65432


def run_client(message='Hello, server'):
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		s.sendall(message.encode())
		data = s.recv(1024)

	print(f"[CLIENT] Received: {data.decode()}")


if __name__ == '__main__':
	run_client()

