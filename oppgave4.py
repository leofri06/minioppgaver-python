def add_item():
    vare = input("Skriv her: ")
    if vare.strip() == "":
        print("Varenavn kan ikke være tomt. Prøv igjen.")
        return True
    if vare.lower() == "ferdig":
        return False
    vareliste.append(vare)
    return True


vareliste = []

print("Skriv inn en vare (eller 'ferdig' for å avslutte): ")
while True:
    if not add_item():
        break

print("\nDu har lagt til følgende varer i handlelisten:")
for x, vare in enumerate(vareliste, start=1):
    print(f"{x}. {vare}")
print(f"\nTotalt antall varer i handlelisten: {len(vareliste)}")