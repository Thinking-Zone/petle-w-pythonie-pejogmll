import random

pada = random.choice([True, False])
zgaduj = True

while zgaduj:
    odpowiedz = input("Czy pada? (t/n) ").strip().lower()


    if odpowiedz == 't' and pada:
        print("Tak, pada!")
        zgaduj = False
    elif odpowiedz == 'n' and not pada:
        print("Nie, nie pada!")
        zgaduj = False
    else:
        print("Spróbuj ponownie.")
