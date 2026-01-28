# opdracht 1 van fase 1
naam = input("Wat is je naam? ")
print("Hallo", naam)



# opdracht 2 van fase 1
A = int(input("Voer een nummer in: "))
B = int(input("Voer nog een nummer in: "))

print(A + B)



# opdracht 3 van fase 1
    # Geboortedatum vragen
jaar = int(input("Wat is je geboortjejaar? "))

    # Leeftijd nu berekenen (ongeveer)
huidig_jaar = 2026
leeftijd_nu = huidig_jaar - jaar

    # Leeftijd over 10 jaar
leeftijd_over_10_jaar = leeftijd_nu + 10

print("Over 10 jaar ben je ongeveer", leeftijd_over_10_jaar, "jaar oud.")



# opdracht 4 van fase 1
# Vraag wat de gebruiker invoert
keuze = input("Welke temperatuur voer je in? Fahrenheit of Celsius? (F/C): ").upper()
temperatuur = float(input("Voer de temperatuur in: "))

# Conversie
if keuze == "F":
    # Gebruiker gaf Fahrenheit → omrekenen naar Celsius
    print("Dat is", round((temperatuur - 32) * 5 / 9, 1), "°C")

if keuze == "C":
    # Gebruiker gaf Celsius → omrekenen naar Fahrenheit
    print("Dat is", round((temperatuur * 9 / 5) + 32, 1), "°F")






# opdracht 5 van fase 1
# hele getallen
getal = 10
print("Dit is een integer (hele getal):", getal)

# decimale getallen
kommagetal = 3.14
print("Dit is een float (decimaal getal):", kommagetal)

# String
tekst = "Hallo"
print("Dit is een string (tekst):", tekst)

# Boolean (waar/niet waar)
waar_of_niet = True
print("Dit is een boolean (True of False):", waar_of_niet)

# List
lijst = [1, 2, 3]
print("Dit is een list (lijst van items):", lijst)

# Dict sleutel:waarde
dict_voorbeeld = {"naam": "Jim", "leeftijd": 30}
print("Dit is een dictionary (sleutel:waarde):", dict_voorbeeld)


