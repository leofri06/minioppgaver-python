import random

print("Velkommen til gjetteleken!\n"
      "------------------------\n")
x = int(input("Skriv inn et heltall større enn 1:\n"))
nummer = random.randint(1, x)
antallforsok = 7
guesses = 0

while True:

    if guesses == antallforsok:
        print(f"\nBeklager, du har brukt opp alle dine {antallforsok} forsøk. Tallet var {nummer}.")
        break
    else:
        if guesses == 0:
            print(f"\nDu har {antallforsok} forsøk på å gjette hvilket tall jeg tenker på.\n")
        else:
            print(f"Du har {antallforsok - guesses} forsøk igjen.\n")
        
        gjett = int(input(f"Gjett et tall mellom 1 og {x}:\n"))

        if gjett == nummer:
            print("\nGratulerer! Du gjettet riktig!"
                  f"\nTallet jeg tenkte på var {nummer}.\n"
                  f"Du brukte {guesses + 1} forsøk på å gjette riktig.")
            break
        elif gjett < nummer:
            print("Tallet er høyere enn det du gjettet. Prøv igjen!")
            guesses = guesses + 1
            print("\n-----------------------\n"
                  f"\nDu har brukt {guesses} av {antallforsok} forsøk.")
        else:
            print("Tallet er lavere enn det du gjettet. Prøv igjen!")
            guesses = guesses + 1
            print("\n-----------------------\n"
                  f"\nDu har brukt {guesses} av {antallforsok} forsøk.")
