import socket
import threading

HOST = '127.0.0.1'
PORT = 5050

# daftar client yang terhubung
clients = []

def broadcast(pesan, sender):
    """Kirim pesan ke semua client kecuali pengirim"""
    for client in clients:
        if client != sender:
            try:
                client.sendall(pesan)
            except:
                clients.remove(client)

def handle_client(conn, addr):
    print(f"[SERVER] Client terhubung: {addr}")
    clients.append(conn)

    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break

            print(f"[SERVER] Pesan dari {addr}: {data.decode()}")
            broadcast(data, conn)

        except:
            break

    conn.close()
    clients.remove(conn)
    print(f"[SERVER] Client terputus: {addr}")


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"[SERVER] Server berjalan di port {PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


if __name__ == "__main__":
    main()
