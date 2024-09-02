import threading
import time

# Sdílený seznam, do kterého budou vlákna přidávat čísla
shared_list = []

# Zámek pro synchronizaci přístupu k sdílenému seznamu
lock = threading.Lock()

# Funkce, která přidává čísla do seznamu
def add_numbers():
    for i in range(1, 1001):
        # Simulace výpočtu
        time.sleep(0.001)  # 1 milisekunda zpoždění

        # Uzamknutí zámku před přidáním čísla do seznamu
        with lock:
            shared_list.append(i)

# Vytvoření dvou vláken
thread1 = threading.Thread(target=add_numbers)
thread2 = threading.Thread(target=add_numbers)

# Spuštění vláken
thread1.start()
thread2.start()

# Čekání na dokončení vláken
thread1.join()
thread2.join()

# Výsledek
print(f"Počet čísel v seznamu: {len(shared_list)}")
print(f"Prvních 10 čísel v seznamu: {shared_list[:10]}")
print(f"Posledních 10 čísel v seznamu: {shared_list[-10:]}")