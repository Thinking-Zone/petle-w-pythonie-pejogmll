# Napisz program, który poprosi użytkownika o podanie liczby całkowitej n.
# Jeśli podana liczba będzie mniejsza niż 1, program wyświetli komunikat: "Podaj liczbę większą lub równą 1".
# Jeśli liczba będzie większa lub równa 1, program wypisze wszystkie liczby od 1 do n wraz z ich kwadratami
# w formacie: "Liczba: [liczba], Kwadrat: [kwadrat]".
print("A pod spodem rozwiązanie tego zadanka, napisane w Pythonie :)")

n = int(input("Podaj liczbę całkowitą n: "))

if n < 1:
    print("Podaj liczbę większą lub równą 1")
else:
    for liczba in range(1, n + 1):
        print(f"Liczba: {liczba}, Kwadrat: {liczba ** 2}")
