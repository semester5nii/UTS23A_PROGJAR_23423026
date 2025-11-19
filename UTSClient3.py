import socket

HOST = "127.0.0.1"
PORT = 5050

# Membuat socket TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -----------------------------
# 1. Timeout 3 detik saat connect
# -----------------------------
client.settimeout(3)

try:
    print("[CLIENT] Mencoba koneksi ke server...")
    client.connect((HOST, PORT))
    print("[CLIENT] Berhasil terhubung ke server.")
except socket.timeout:
    print("[CLIENT] Koneksi timeout!")
    exit()
except Exception as e:
    print("[CLIENT] Error:", e)
    exit()

# -----------------------------
# 2. Timeout 2 detik saat membaca data
# -----------------------------
client.settimeout(2)

try:
    pesan = "Hello Server"
    print("[CLIENT] Mengirim:", pesan)
    client.sendall(pesan.encode())

    # mencoba menerima data
    data = client.recv(1024).decode()
    print("[CLIENT] Balasan:", data)

except socket.timeout:
    print("[CLIENT] Koneksi timeout!")

except Exception as e:
    print("[CLIENT] Error:", e)

finally:
    client.close()
