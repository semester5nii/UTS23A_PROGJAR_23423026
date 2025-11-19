import socket

HOST = '127.0.0.1'    # localhost
PORT = 5050           # port sesuai soal

# Membuat socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"[SERVER] Server berjalan pada port {PORT} ...")

while True:
    conn, addr = server_socket.accept()
    print(f"[SERVER] Terhubung dengan {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break

        pesan = data.decode()
        print(f"[SERVER] Pesan diterima: {pesan}")

        # Kirim balik (echo)
        conn.sendall(data)

    conn.close()
    print("[SERVER] Client terputus")
