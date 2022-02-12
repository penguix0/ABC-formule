##########################################################################
# Autheur        : Arne Cuperus
# Doel           : Dit programma automatiseert de ABC-formule
# Datum / versie : 11-02-2022 | Versie 2
#
# Invoer          : A, B, C
# Uitvoer         : D, x1, x2
# Gebruikte berekeningen / algoritmen : 
# - D = bˆ2 -4ac
# - x = (-b -/+ √D) ÷ (2*a)
#
# Overige opmerkingen : 
#  Dit python script valt onder het MIT license, zie LICENSE.md voor meer informatie.
##########################################################################

# Importeer 'math' om een wortel te kunnen trekken.
from math import sqrt
from unittest import skip

# Verklaar 'aantal_decimalen' met als waarde 1.
aantal_decimalen = 1

# Geef melding "De ABC-formule!" 
print ("\nDe ABC-formule!")

# Defenieer de functie 'verzamel_invoer' zonder parameters.
def verzamel_invoer():
    # Verklaar 'valide_invoer' als False
    valide_invoer = False
    # Zolang valide_invoer niet waar is.
    while valide_invoer == False:
        # Probeer om geldige invoer te vragen:
        try:
            # Geef melding "Welke waarde heeft: a?"
            # Input float(A)
            A = float(input("Welke waarde heeft: a? "))
            # Geef melding "Welke waarde heeft: b?"
            # Input float(B)
            B = float(input("Welke waarde heeft: b? "))
            # Geef melding "Welke waarde heeft: c?"
            # Input float(C)
            C = float(input("Welke waarde heeft: c? "))
            # Verklaar 'valide_invoer' als True
            valide_invoer = True
        # Wanneer de invoer geen geldig nummer is:
        except ValueError:
            # Geef melding "Voer een geldig nummer in."
            print("Voer een geldig nummer in.")
    
    # Retouneer A, B en C   
    return A, B, C


# Defenieer de functie 'bereken_discriminant' en geef hem 3 parameters (a,b,c). 
def bereken_discriminant(a:float, b:float, c:float):
    # Retouneer D (de discriminant) door de volgende formule te gebruiken: D=b^2 - 4ac.
    return (b**2) - (4*a*c)

# Defenieer de functie 'bereken_x' en geef hem 3 parameters (d, a, b).
def bereken_x(d:float, a:float, b:float):
    if d == 0:
        # Verklaar x1 met de formule ( -b - √6 ) ÷ 2*a
        x1 = (-b - sqrt(d)) / (2*a)
        # Retouneer x1
        return x1

    # Verklaar x1 met de formule ( -b - √6 ) ÷ 2*a
    x1 = (-b - sqrt(d)) / (2*a)
    # Verklaar x1 met de formule ( -b + √6 ) ÷ 2*a
    x2 = (-b + sqrt(d)) / (2*a)
    # Retouneer x1 en x2.
    return x1, x2

# Defenieer de functie 'main' deze functie is de primaire functie van het programma.    
def main():
    # Roep de functie verzamel_invoer() aan en geef A, B, C de waardes die geretouneerd worden 
    A, B, C = verzamel_invoer()
    # Roep de functie 'bereken_discriminant aan en geef de variabel D de geretouneerde waarde.
    D = bereken_discriminant(a=A,b=B,c=C)
    # Geef melding "\nD: " + str(int(D))
    print(f"\nD: {str(int(D))}")

    # Als D == 0:
    if D == 0:
        # Geef melding "Het discriminant is gelijk aan 0, er is één oplossing."
        print("Het discriminant is gelijk aan 0, er is één oplossing.")
        # Bereken x1.
        x1 = bereken_x(a=A, b=B, d=D)
        # Rond x1 af.
        x1 = round(x1, aantal_decimalen)
        # Geef melding "x1: " + str(x1)
        print(f"x1: {str(x1)}")     
        return   
    # Als D < 0:
    elif D < 0:
        # Geef melding "Het discriminant is kleiner dan 0, er zijn geen oplossingen mogelijk."
        print("Het discriminant is kleiner dan 0, er zijn geen oplossingen mogelijk.")
        return
    
    x1, x2 = bereken_x(a=A, b=B, d=D)
    # Bereken x1 en x2 en rond ze af tot 1 decimaal.
    x1 = round(x1, aantal_decimalen)
    x2 = round(x2, aantal_decimalen)
    # Geef melding "x1: " + str(x1)
    print(f"x1: {str(x1)}")
    # Geef melding "x2: " + str(x2)
    print(f"x2: {str(x2)}")

# Controleer of dit programma wordt uitgevoerd door een gebruiker en niet door een ander programma.
if __name__ == '__main__':
    # Herhaal de main functie voor altijd.
    while True: main()






