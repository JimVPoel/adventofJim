import random

# Vraag de keuzes van de gebruiker
keuze_lengte = int(input("Hoe lang moet het wachtwoord zijn? "))
keuze_kleine_letters = input("Moeten er kleine letters in zitten? (ja/nee): ")
keuze_hoofdletters = input("Moeten er hoofdletters in zitten? (ja/nee): ")
keuze_nummers = input("Moeten er nummers in zitten? (ja/nee): ")
keuze_speciale_tekens = input("Moeten er speciale tekens in zitten? (ja/nee): ")

# Start met lege tekens-string
tekens = ""

# Voeg tekens toe afhankelijk van de keuzes (zonder +=)
if keuze_kleine_letters == "ja":
    tekens = tekens + "abcdefghijklmnopqrstuvwxyz"

if keuze_hoofdletters == "ja":
    tekens = tekens + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if keuze_nummers == "ja":
    tekens = tekens + "0123456789"

if keuze_speciale_tekens == "ja":
    tekens = tekens + "!@#$%&*"

# Genereer wachtwoord
wachtwoord = ""
for i in range(keuze_lengte):
    wachtwoord = wachtwoord + random.choice(tekens)

print("Gegenereerd wachtwoord:", wachtwoord)
