from spillebrett import Spillebrett

def main():
    rader = int(input("Hvor mange rader?"))
    rekker = int(input("Hvor mange rekker?"))

    spillern = Spillebrett(rader, rekker)
    spillern.tegnBrett()

    brukersValg = ""
    while brukersValg != 'q': #så lenge brukeren ikke skriver inn 'q'
        brukersValg = input("Press enter for aa fortsette. Skriv in q og enter for aa avslutte:")

        if brukersValg == "": #dersom brukeren bare trykker på enter, kjør spillet
            spillern.oppdatering()
            spillern.tegnBrett()
            spillern.finnAntallLevende()


# starte hovedprogrammet
main()
