while True:    
    poengsum = int(input("Skriv inn poengsummen din (0-100):\n").strip())

    if poengsum < 0 or poengsum > 100:
        print("\nIkke gyldig inndata, prøv igjen")
    elif poengsum < 35:
        print("\nDu fikk karakter 1.")
        break
    elif poengsum >= 35 and poengsum < 50:
        print("\nDu fikk karakter 2.")
        break
    elif poengsum >= 50 and poengsum < 65:
        print("\nDu fikk karakter 3.")
        break
    elif poengsum >= 65 and poengsum < 80:
        print("\nDu fikk karakter 4.")
        break
    elif poengsum >= 80 and poengsum <= 90:
        print("\nDu fikk karakter 5.")
        break
    elif poengsum > 90:
        print("\nDu fikk karakter 6.")
        break
