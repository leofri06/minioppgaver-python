

forbudteOrd = ["styggtord1", "styggtord2", "styggtord3"]

melding = input("Skriv melding her: ")

if melding.lower() in forbudteOrd:
    print("\nMelding stoppet")
else:
    print(f"\nMelding sendt!\n '{melding}'")