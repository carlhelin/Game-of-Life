class Celle:

    def __init__(self):
        self._status = "doed" #statusen bli opprinelig satt til død, de fleste skal være det

    def settDoed(self):
        self._status = "doed" #endrer den tilbake til død, og returnerer det
        return self._status

    def settLevende(self):
        self._status = "levende" #endrer til levende, returnerer det
        return self._status

    def erLevende(self):
        if self._status == "levende":
            return True
        return False

    def hentStatusTegn(self):
        if self.erLevende() == True:
            return ("O") #skriv dette som en stor 'O'
        return (".") #skriv hvis det er false som '.'
