import colorful
import sys
import ruamel.yaml


class Main():

    def __init__(self):
        yaml = ruamel.yaml.YAML(typ='safe')
        try:
            with open("./std_kennzahlen.yml", 'r') as stream:
                self.std_kennzahlen_yaml = yaml.load(stream)
            with open("./bilanz.yml", 'r') as stream:
                self.bilanz_yaml = yaml.load(stream)
        except Exception as e:
            print(colorful.bold_red(e))

        # Standart Kennzahlen
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

        # Options
        self.geschäftsform = self.bilanz_yaml["Bemerkungen"]["geschäftsform"]
        self.vorraete_anfangs_jahr = self.bilanz_yaml["Bemerkungen"]["vorraete_anfangs_jahr"]
        self.debitorenstand_anfangs_jahr = self.bilanz_yaml["Bemerkungen"]["debitorenstand_anfangs_jahr"]
        self.umsatzrentabilitaet = self.bilanz_yaml["Bemerkungen"]["umsatzrentabilitaet"]
        self.kapitalumschlag = self.bilanz_yaml["Bemerkungen"]["kapitalumschlag"]
        self.anlagenintensitaet = self.bilanz_yaml["Bemerkungen"]["anlagenintensitaet"]
        self.selbstfinanzierungsgrad = self.bilanz_yaml["Bemerkungen"]["selbstfinanzierungsgrad"]

        # Bilanz
        self.reingewinn = self.bilanz_yaml["Erfolgsrechnung"]["GEWINN"]
        self.zinsen = self.bilanz_yaml["Erfolgsrechnung"]["Aufwand"]["ZINSEN"]
        self.gesamtkapital = self.bilanz_yaml["Bilanz"]["GESAMTVERMOEGEN"]
        self.liquide_mittel = self.bilanz_yaml["Bilanz"]["Aktiven"]["Umlaufvermoegen"]["LIQUIDE_MITTEL"]
        forderungen = self.bilanz_yaml["Bilanz"]["Aktiven"]["Umlaufvermoegen"]["DEBITOREN"]
        self.kurzfristiges_FK = 0
        for kf_fk in self.bilanz_yaml['Bilanz']['Passiven']['Fremdkapital']['Kurzfristiges_FK'].values():
            self.kurzfristiges_FK += kf_fk
        self.eigenkapital = 0
        for ek in self.bilanz_yaml['Bilanz']['Passiven']['Eigenkapitalkapital'].values():
             self.eigenkapital += ek
        self.umlaufvermoegen = 0
        for uv in self.bilanz_yaml["Bilanz"]["Aktiven"]["Umlaufvermoegen"].values():
            self.umlaufvermoegen += uv

    def validate_bilanz(self):
        print("WIP")
        # TODO

    def check_kennzahl_range(self, min, max, name, zahl):
        if resultat >= min and resultat <= max:
            print(name + colorful.green(str(resultat) + "% ") + "[" + colorful.green(OK) + "]" + "Min: " + min + "% Max: " + max + "%")
        elif resultat < min:
            print(name + colorful.red(str(resultat) + "% ") + "[" + colorful.red(Zu Tief) + "]" + "Min: " + min + "% Max: " + max + "%")
        elif resultat > max:
            print(name + colorful.red(str(resultat) + "% ") + "[" + colorful.red(Zu Hoch) + "]" + "Min: " + min + "% Max: " + max + "%")
        else:
            print(name + colorful.red(str(resultat) + "% ") + "[" + colorful.red(ERROR) + "]" + "Min: " + min + "% Max: " + max + "%")

    def cal_gesamtkapitalrent(self):
        resultat = (self.reingewinn + self.zinsen) * 100 / self.gesamtkapital
        if resultat >= self.gesamtkapitalrent:
            print(colorful.green("Die Gesamtkapitalrentabilität liegt bei " + str(resultat) + "%."))
        else:
            print(colorful.red("Die Gesamtkapitalrentabilität liegt bei " + str(resultat) + "%. Sie ist damit NICHT gewährleistet."))

    def cal_liquiditaetsgrad1(self):
        resultat = self.liquide_mittel * 100 / self.kurzfristiges_FK
        self.check_kennzahl_range(self.liquidmin_1, self.liquidmax_1, "Liquiditätsgrad 1", resultat)

    def cal_liquiditaetsgrad2(self):
        resultat = (self.liquide_mittel + self.forderungen) * 100 / self.kurzfristiges_FK
        if resultat >= self.liquid_2:
            print(colorful.green("Der Liquiditätsgrad_2 liegt bei " + str(resultat) + "%."))
        else:
            print(colorful.red("Der Liquiditätsgrad_2 liegt bei " + str(resultat) + "%. Dies ist zu tief"))

    def cal_liquiditaetsgrad3(self):
        resultat = self.umlaufvermögen * 100 / self.kurzfristiges_FK
        self.check_kennzahl_range(self.liquidmin_3, self.liquidmax_3, "Liquiditätsgrad 3", resultat)

    def cal_eigenkapitalrentabilitaet(self):
        resultat = self.reingewinn * 100 / (self.eigenkapital - self.reingewinn)
        if resultat >= self.eigenkapitalrent:
            print(colorful.green("Die Eigenkapitalrentabilität liegt bei " + str(resultat) + "%."))
        else:
            print(colorful.red("Die Eigenkapitalrentabilität bei " + str(resultat) + "%. Dies ist zu tief"))

if __name__ == "__main__":
    programm = Main()
    programm.cal_gesamtkapitalrent()
    programm.cal_liquiditaetsgrad1()
    programm.cal_liquiditaetsgrad2()
    programm.cal_eigenkapitalrentabilitaet()
    programm.cal_liquiditaetsgrad3()
