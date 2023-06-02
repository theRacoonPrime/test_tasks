class Gepard:
    def __init__(self):
        self.pocet_zivotu = 9

    def je_zivy(self):
        return self.pocet_zivotu > 0

    def uber_zivot(self):
        if not self.je_zivy():
            print("Nemůžeš zabít již mrtvé zvíře!")
        else:
            self.pocet_zivotu -= 1

    def snez(self, jidlo):
        if not self.je_zivy():
            print("Je zbytečné krmit mrtvé zvíře!")
            return

        if jidlo == "ryba" and self.pocet_zivotu < 9:
            self.pocet_zivotu += 1
            print("Gepard spapal rybu a obnovil se mu jeden život.")
        else:
            print("Gepard se krmi.")

    def napapej_se(self):
        while self.pocet_zivotu < 9:
            self.snez("ryba")



