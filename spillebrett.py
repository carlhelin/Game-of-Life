from random import randint
from celle import Celle

class Spillebrett:
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._generasjonsnummer = 0
        self._rutenett = []

        for rader in range(self._rader): #for antallet av rader
            self._rutenett.append([]) #utvid rutenettet med nye lister (nøstet liste)
            for kolonner in range(self._kolonner): #for antallet av kolonner
                self._rutenett[rader].append(Celle()) #utvid selve rutenettet sine rader med celle-objekter

        self._generer() #legger inn  generer slik at den genererer tilfeldige celler død og levende

    def _generer(self) :
        for rad in self._rutenett: #for radene i self._rutenett
            for celle in rad: #for cellene
                tilfeldig = randint(0,2) #tilfeldig tall, enten 0,1,2
                if tilfeldig == 2: #dersom tallet er 2
                    celle.settLevende() #blir cellen satt til levende

    def tegnBrett(self):
        for i in range(20): #gir litt mellomrom mellom hver oppdatering
            print()

        for listene in self._rutenett:
            for cellene in listene: #for cellene i listene
                print(cellene.hentStatusTegn(), end=' ') #print tegnet til cellen
            print() #lag nedhakk etter hver linje
        print("Generasjon:", self._generasjonsnummer, "Antall levende celler:", self.finnAntallLevende()) #print dette slik at man får live-update


    def finnNabo(self, rad, kolonne):
        naboer = [] #naboeen er tom liste

        #Dette er for hjornene i selve spillebrettet som har 3 naboer
        if rad == 0 and kolonne == 0:
            naboer = [[self._rutenett[0][1]], [self._rutenett[1][1]], [self._rutenett[1][0]]]
        elif rad == 0 and kolonne == self._kolonner-1:
            naboer = [[self._rutenett[0][-2]], [self._rutenett[1][-2]], [self._rutenett[1][-1]]]
        elif rad == self._rader-1 and kolonne == self._kolonner-1:
            naboer = [[self._rutenett[-1][-2]], [self._rutenett[-2][-1]], [self._rutenett[-2][-2]]]
        elif rad == self._rader-1 and kolonne == 0:
            naboer = [[self._rutenett[-1][1]], [self._rutenett[-2][1]], [self._rutenett[-2][0]]]

        #Dette er for selve kantene av spillebrettet som har 5 naboer
        elif rad == 0 and kolonne > 0 and kolonne < self._kolonner-1:
            naboer = [[self._rutenett[0][kolonne+1]], [self._rutenett[0][kolonne-1]], [self._rutenett[rad+1][kolonne+1]], [self._rutenett[rad+1][kolonne]], [self._rutenett[rad+1][kolonne-1]]]
        elif rad > 0 and rad < self._rader and kolonne == self._kolonner-1:
            naboer = [[self._rutenett[rad-1][kolonne]], [self._rutenett[rad-1][kolonne-1]], [self._rutenett[rad][kolonne-1]], [self._rutenett[rad+1][kolonne-1]], [self._rutenett[rad+1][kolonne]]]
        elif rad == self._rader-1 and kolonne > 0 and kolonne < self._kolonner-1:
            naboer = [[self._rutenett[rad][kolonne+1]], [self._rutenett[rad-1][kolonne+1]], [self._rutenett[rad-1][kolonne]], [self._rutenett[rad-1][kolonne-1]], [self._rutenett[rad][kolonne-1]]]
        elif rad > 0 and rad < self._kolonner and kolonne == 0:
            naboer = [[self._rutenett[rad+1][kolonne]], [self._rutenett[rad+1][kolonne+1]], [self._rutenett[rad][kolonne+1]], [self._rutenett[rad-1][kolonne+1]], [self._rutenett[rad-1][kolonne]]]

        #Dette er for midtbrikkene som har 8 naboer
        else:
            naboer = [ [self._rutenett[rad-1][kolonne-1]],
            [self._rutenett[rad][kolonne-1]],
            [self._rutenett[rad+1][kolonne-1]],
            [self._rutenett[rad+1][kolonne]],
            [self._rutenett[rad+1][kolonne+1]],
            [self._rutenett[rad][kolonne+1]],
            [self._rutenett[rad-1][kolonne+1]],
            [self._rutenett[rad-1][kolonne]] ]

        return naboer #gi tilbake naboer slik at oppdateringen av brettet vet hva den skal oppdatere til

    def oppdatering(self):
        dodTilLevende = [] #listen med de som er døde eller levende som skal være levende
        levendeTilDod = [] #listen med de som er levende som skal bli døde

        for rad in range(len(self._rutenett)):
            for kolonne in range(len(self._rutenett[rad])):
                naboSjekk = self.finnNabo(rad,kolonne) #finn naboene til 'den enkelte celle'

                levendeNaboer = [] #liste med de levende naboene til én celle
                for lister in naboSjekk:
                    for elementer in lister:
                        if elementer.erLevende() == True: #dersom cellene av naboene til 'den enkelte celle' lever
                            levendeNaboer.append(elementer) #blir dette liste med kun de levende elementer

                cellen = self._rutenett[rad][kolonne] #den spesifike cellen blir bestemt

                if cellen.erLevende() == True: #dersom den spesifikke cellen lever
                    if len(levendeNaboer) == 2 or len(levendeNaboer) == 3:
                        dodTilLevende.append(cellen) #og levende naboer er 2 eller 3, skal den fortsette å lev
                    if len(levendeNaboer) < 2 or len(levendeNaboer) > 3:
                        levendeTilDod.append(cellen) #dersom den spesifikke cellen har mer enn 3 eller færre enn 2 naboer som lever, dør den
                elif cellen.erLevende() == False: #Dersom det er en død celle
                    if len(levendeNaboer) == 3: #som har 3 naboer, skal den bli satt til levende
                        dodTilLevende.append(cellen)

        for celler in dodTilLevende: #sett cellene til de som skal leve videre eller bli født til levende
            celler.settLevende()
        for celler in levendeTilDod: #sett cellene til de som skal død til død
            celler.settDoed()
        self._generasjonsnummer += 1 #legg til 1 hver gang denne kjører

    def finnAntallLevende(self): #for å finne antall levende, går jeg igjennom selve elementene via en nøstet liste og dersom den listen er "O" blir cellen telt
        antallLevende = 0
        for lister in self._rutenett:
            for celle in lister:
                if celle.hentStatusTegn() == "O":
                    antallLevende += 1
        return antallLevende #returnerer selve resultatet
