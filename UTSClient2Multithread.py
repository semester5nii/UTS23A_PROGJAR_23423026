import socket
import threading

HOST = '127.0.0.1'
PORT = 5050

def terima_pesan(sock):
    while True:
        try:
            data = sock.recv(1024)
            if data:
                print("\n[Pesan Masuk] ", data.decode())
        except:
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    # Thread untuk menerima pesan
    threading.Thread(target=terima_pesan, args=(client,), daemon=True).start()

    print("Terhubung ke server. Ketik pesan lalu Enter:")

    while True:
        pesan = input()
        client.sendall(pesan.encode())


if __name__ == "__main__":
    main()
