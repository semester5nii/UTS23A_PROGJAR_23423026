import socket
import time

HOST = '127.0.0.1'
PORT = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("[SERVER] Server berjalan... menunggu koneksi.")

while True:
    conn, addr = server.accept()
    print(f"[SERVER] Terhubung dengan {addr}")

    # Delay untuk menguji timeout client
    time.sleep(5)
    try:
        conn.sendall("Halo dari server!".encode())
    except:
        print("[SERVER] Client terputus sebelum menerima data.")
    
    conn.close()
