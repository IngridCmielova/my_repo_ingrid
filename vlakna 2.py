import threading

# Požádání uživatele o zadání čísel a jejich uložení do seznamu
numbers = list(map(int, input("Zadejte čísla oddělená mezerou: ").split()))

# Funkce pro nalezení maximálního čísla
def find_max():
    maximum = max(numbers)
    print(f"Maximální číslo je: {maximum}")

# Funkce pro nalezení minimálního čísla
def find_min():
    minimum = min(numbers)
    print(f"Minimální číslo je: {minimum}")

# Vytvoření dvou vláken
thread1 = threading.Thread(target=find_max)
thread2 = threading.Thread(target=find_min)

# Spuštění vláken
thread1.start()
thread2.start()

# Čekání na dokončení vláken
thread1.join()
thread2.join()