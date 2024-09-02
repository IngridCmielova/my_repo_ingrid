import socket
import threading

# Globální proměnná pro počítání návštěv
visitor_count = 0

# Mutex (zámek) pro ochranu sdílené proměnné
lock = threading.Lock()


# Funkce pro obsluhu klienta
def handle_client(client_socket):
    global visitor_count

    # Zamknutí přístupu k proměnné
    with lock:
        visitor_count += 1
        current_visit = visitor_count
    # Odeslání návštěvnosti klientovi
    client_socket.send(f"Počet návštěv: {current_visit}\n".encode('utf-8'))

    # Zavření spojení
    client_socket.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9999))
    server.listen(5)  # Server může naslouchat až 5 klientům současně
    print("Server naslouchá na portu 9999...")

    while True:
        client_socket, addr = server.accept()
        print(f"Připojen klient: {addr}")

        # Vytvoření nového vlákna pro každého klienta
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()


# Spuštění serveru
if __name__ == "__main__":
    start_server()