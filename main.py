import random
import time
import sys


def vytvor_tajne_cislo():
    """Generuje 4místné číslo s unikátními číslicemi, nezačíná nulou."""
    while True:
        cislo = str(random.randint(1000, 9999))  # Číslo nezačíná nulou
        if len(set(cislo)) == 4:  # Všechny číslice unikátní
            return cislo


def porovnej_cisla(tajne_cislo, tve_cislo):
    """
    Porovná čísla a vrátí počet bulls a cows.

    Bulls: správná číslice na správném místě.
    Cows: správná číslice na špatném místě.
    """
    bulls = 0
    cows = 0
    for i in range(4):
        if tajne_cislo[i] == tve_cislo[i]:
            bulls += 1
        elif tve_cislo[i] in tajne_cislo:
            cows += 1
    return bulls, cows


def vypis_statistiku(statistika):
    """
    Funkce vypíše přehled všech odehraných her a jejich výsledků.

    Parametry:
        statistika (dict): Slovník s výsledky her ve formátu {"Game 1": 5, "Game 2": 7, ...}
    Návratová hodnota:
        None
    """
    print("\nGame Statistics:")
    print("-" * 60)
    for hra, pokusy in statistika.items():
        print(f"{hra}: {pokusy} guesses")
    print("-" * 60)
    

def start_hry():
    """Funkce spouští hru a vypíše úvodní text."""
    statistika = {}
    hra_cislo = 1
    prvni_hra = True  # Sleduje, zda se jedná o první hru

    while True:
        # Úvodní text se vypíše jen při první hře
        if prvni_hra:
            uvodni_text = (
                f"Hi there!\n"
                f"{'-'*60}\n"
                f"I've generated a random 4-digit number for you.\n"
                f"Let's play a bulls and cows game.\n"
                f"{'-'*60}\n"
                f"Enter a number (or type 'exit' to quit):\n"
                f"{'-'*60}"
            )
            print(uvodni_text)
            prvni_hra = False  # Po první hře už se nebude vypisovat

        tajne_cislo = vytvor_tajne_cislo()
        print(tajne_cislo)  # Můžeš zakomentovat, pokud nechceš vidět tajné číslo
        pocet_pokusu = 0
        start_time = time.time()

        while True:
            tve_cislo = input(">>> ").strip().lower()
            if tve_cislo == "exit":
                print("Game exited. Goodbye!")
                if statistika:
                    vypis_statistiku(statistika)
                return sys.exit()

            # Kontroly vstupu
            if len(tve_cislo) != 4:
                print("Incorrect length, it must be a 4-digit number, try again...")
                continue
            if not tve_cislo.isdigit():
                print("It must be a number, try again...")
                continue
            if tve_cislo[0] == "0":
                print("The number cannot start with zero, try again...")
                continue
            if len(set(tve_cislo)) != 4:
                print("The number contains duplicate digits, try again...")
                continue

            pocet_pokusu += 1
            bulls, cows = porovnej_cisla(tajne_cislo, tve_cislo)

            if bulls == 4:
                total_time = int(round(time.time() - start_time))
                print(f"Correct! Number guessed in {pocet_pokusu} guesses.")
                print(f"Time taken: {total_time} seconds.")
                statistika[f"Game {hra_cislo}"] = pocet_pokusu
                hra_cislo += 1
                break
            else:
                print(f"{bulls} bull{'s' if bulls != 1 else ''}, {cows} cow{'s' if cows != 1 else ''}")

        # Opakování hry
        again = input("Do you want to play again? (yes/no): ").strip().lower()
        if again != "yes":
            vypis_statistiku(statistika)
            print("Thanks for playing! Goodbye!")
            return sys.exit()
        else:
            pass  # Pokračuje bez zobrazení úvodního textu


if __name__ == "__main__":
    start_hry()