licznik_nie = 0

while True:
    odpowiedz = input("Czy pada? (tak/nie/nie wiem): ").strip().lower()

    if odpowiedz == "tak":
        print(f"Liczba odpowiedzi 'nie': {licznik_nie}")
        break
    elif odpowiedz == "nie":
        licznik_nie += 1
    elif odpowiedz == "nie wiem":
        print("To wyjdź na zewnątrz i się dowiedz.")
    else:
        print("Nie rozumiem tej odpowiedzi. Odpowiedz 'tak', 'nie' lub 'nie wiem'.")
