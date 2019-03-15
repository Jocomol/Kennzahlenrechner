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
        self.reingewinn = self.bilanz_yaml["Erfolgsrechnung"]["gewinn"]
        self.zinsen = self.bilanz_yaml["Erfolgsrechnung"]["Aufwand"]["zinsen"]
        self.gesamtkapital = self.bilanz_yaml["Bilanz"]["gesamtvermoegen"]

    def validate_bilanz(self):
        print("WIP")
        # TODO

    def cal_gesamtkapitalrent(self):
        resultat = (self.reingewinn + self.zinsen) * 100 / self.gesamtkapital
        if resultat >= self.gesamtkapitalrent:
            print(colorful.green("Die Gesamtkapitalrentabilität liegt bei " + str(resultat) + "%."))
        else:
            print(colorful.red("Die Gesamtkapitalrentabilität liegt bei " + str(resultat) + "%. Sie ist damit NICHT gewährleistet."))

    def cal_liquiditaetsgrad1(self):
        liquide_mittel = self.bilanz_yaml["Bilanz"]["Aktiven"]["Umlaufvermoegen"]["liquide_mittel"]
        kurzfristiges_FK = 0
        for kf_fk in self.bilanz_yaml['Bilanz']['Passiven']['Fremdkapital']['Kurzfristiges_FK'].values():
            kurzfristiges_FK = kurzfristiges_FK + kf_fk
        resultat = liquide_mittel * 100 / kurzfristiges_FK
        if resultat >= self.liquidmin_1 and resultat <= self.liquidmax_1:
            print(colorful.green("Der Liquiditätsgrad_1 liegt bei " + str(resultat) + "%."))
        elif resultat < self.liquidmin_1:
            print(colorful.red("Der Liquiditätsgrad_1 liegt bei " + str(resultat) + "%. Dies ist zu tief"))
        elif resultat > self.liquidmin_1:
            print(colorful.red("Der Liquiditätsgrad_1 liegt bei " + str(resultat) + "%. Dies ist zu hoch"))
        else:
            print(colorful.red("Ein Fehler ist unterlaufen"))

    def cal_liquiditaetsgrad2(self):
        liquide_mittel = self.bilanz_yaml["Bilanz"]["Aktiven"]["Umlaufvermoegen"]["liquide_mittel"]
        kurzfristiges_FK = 0
        for kf_fk in self.bilanz_yaml['Bilanz']['Passiven']['Fremdkapital']['Kurzfristiges_FK'].values():
            kurzfristiges_FK = kurzfristiges_FK + kf_fk
        forderungen = self.bilanz_yaml["Bilanz"]["Aktiven"]["Umlaufvermoegen"]["debitoren"]
        resultat = (liquide_mittel + forderungen) * 100 / kurzfristiges_FK
        if resultat >= self.liquidmin_2:
            print(colorful.green("Der Liquiditätsgrad_2 liegt bei " + str(resultat) + "%."))
        else:
            print(colorful.red("Der Liquiditätsgrad_2 liegt bei " + str(resultat) + "%. Dies ist zu tief"))


if __name__ == "__main__":
    programm = Main()
    programm.cal_gesamtkapitalrent()
    programm.cal_liquiditaetsgrad1()
    programm.cal_liquiditaetsgrad2()
