import colorful
import yaml


class Main():

    def __init__(self):
        try:
            with open("./std_kennzahlen.yml", 'r') as stream:
                self.std_kennzahlen_yaml = yaml.load(stream)
            with open("./bilanz.yml", 'r') as stream:
                self.bilanz_yaml = yaml.load(stream)
        except Exception as e:
            print(colorful.bold_red(e))
        self.eigenkapitalrent = self.std_kennzahlen_yaml["kennzahlen"]["eigenkapitalrent"]
        self.gesamtkapitalrent = self.std_kennzahlen_yaml["kennzahlen"]["gesamtkapitalrent"]
        self.liquidmin_1 = self.std_kennzahlen_yaml["kennzahlen"]["liquidmin_1"]
        self.liquidmax_1 = self.std_kennzahlen_yaml["kennzahlen"]["liquidmax_1"]
        self.liquid_2 = self.std_kennzahlen_yaml["kennzahlen"]["liquid_2"]
        self.liquidmin_3 = self.std_kennzahlen_yaml["kennzahlen"]["liquidmin_3"]
        self.lagerumschlag = self.std_kennzahlen_yaml["kennzahlen"]["lagerumschlag"]
        self.debitorenzahlungsfrist = self.std_kennzahlen_yaml["kennzahlen"]["debitorenzahlungsfrist"]
        self.fremdfinanzierungsgradmin = self.std_kennzahlen_yaml["kennzahlen"]["fremdfinanzierungsgradmin"]
        self.fremdfinanzierungsgradmax = self.std_kennzahlen_yaml["kennzahlen"]["fremdfinanzierungsgradmax"]
        self.eigenfinanzierungsgradmin = self.std_kennzahlen_yaml["kennzahlen"]["eigenfinanzierungsgradmin"]
        self.eigenfinanzierungsgradmax = self.std_kennzahlen_yaml["kennzahlen"]["eigenfinanzierungsgradmax"]
        self.anlagedeckungsgradmin_1 = self.std_kennzahlen_yaml["kennzahlen"]["anlagedeckungsgradmin_1"]
        self.anlagedeckungsgradmax_1 = self.std_kennzahlen_yaml["kennzahlen"]["anlagedeckungsgradmax_1"]
        self.anlagedeckungsgrad_2 = self.std_kennzahlen_yaml["kennzahlen"]["anlagedeckungsgrad_2"]

        self.geschäftsform = self.bilanz_yaml["Bemerkungen"]["geschäftsform"]
        self.vorraete_anfangs_jahr = self.bilanz_yaml["Bemerkungen"]["vorraete_anfangs_jahr"]
        self.debitorenstand_anfangs_jahr = self.bilanz_yaml["Bemerkungen"]["debitorenstand_anfangs_jahr"]
        self.umsatzrentabilitaet = self.bilanz_yaml["Bemerkungen"]["umsatzrentabilitaet"]
        self.kapitalumschlag = self.bilanz_yaml["Bemerkungen"]["kapitalumschlag"]
        self.anlagenintensitaet = self.bilanz_yaml["Bemerkungen"]["anlagenintensitaet"]
        self.selbstfinanzierungsgrad = self.bilanz_yaml["Bemerkungen"]["selbstfinanzierungsgrad"]


    def validate_bilanz(self):
        print("WIP")
        #TODO

    def cal_gesamtkapitalrent(self):
        reingewinn = self.bilanz_yaml["Erfolgsrechnung"]["gewinn"]
        zinsen = self.bilanz_yaml["Erfolgsrechnung"]["Aufwand"]["zinsen"]
        gesamtkapital = self.bilanz_yaml["Bilanz"]["gesamtvermoegen"]
        resultat = (reingewinn + zinsen) * 100 / gesamtkapital
        if resultat >= 5:
            print(colorful.green("Die Gesamtkapitalrentabilität liegt bei " + str(resultat) +"%."))
        else:
            print(colorful.red("Die Gesamtkapitalrentabilität liegt bei " + str(resultat) +"%. Sie ist damit NICHT gewährleistet."))


if __name__ == "__main__":
    programm = Main()
    programm.cal_gesamtkapitalrent()
    x = input("press enter to end")
