import socket

HOST = '127.0.0.1'
PORT = 5050

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

pesan = "Tes Koneksi"
print("[CLIENT] Mengirim:", pesan)
client_socket.sendall(pesan.encode())

balasan = client_socket.recv(1024).decode()
print("[CLIENT] Balasan dari server:", balasan)

client_socket.close()
