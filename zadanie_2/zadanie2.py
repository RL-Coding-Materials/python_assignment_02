def statystyka_lancucha(tekst):
    # dostosu tak, aby instrukcja return była ok

    return {
        "liczba_slow": liczba_slow, # liczba
        "liczba_liter": liczba_liter, # liczba
        "liczba_cyfr": liczba_cyfr, # liczba
        "statystyka": statystyka_posortowana # słownik typu 'a': 1, '2': 3
    }

# Przykładowe użycie
if __name__ == "__main__":
    tekst_wejsciowy = "Ala ma 3 koty i 2 psy"
    wynik = statystyka_lancucha(tekst_wejsciowy)

    # Wyświetlanie wyników
    print("Liczba słów:", wynik["liczba_slow"])
    print("Liczba liter:", wynik["liczba_liter"])
    print("Liczba cyfr:", wynik["liczba_cyfr"])
    print("Statystyka częstości występowania:")
    for znak, liczba in wynik["statystyka"].items():
        print(f"'{znak}': {liczba}", end=" ")
