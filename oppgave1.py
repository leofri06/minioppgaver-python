name = input("Hva heter du?\n").capitalize().strip()
favorittspill = input("Hva er ditt favorittspill?\n").strip()

print(f"\nDette er {name}!\n"
      f"{name} er veldig glad i {favorittspill}.\n")

alder = input("Hvor gammel er du?\n").strip()
print(f"Om 5 år vil du være {int(alder) + 5} år gammel.")