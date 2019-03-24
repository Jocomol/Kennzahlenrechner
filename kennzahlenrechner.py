import colorful
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
        self.eigenkapitalrent = self.std_kennzahlen_yaml[
            "kennzahlen"][
            "eigenkapitalrent"]
        self.gesamtkapitalrent = self.std_kennzahlen_yaml[
            "kennzahlen"][
            "gesamtkapitalrent"]
        self.liquidmin_1 = self.std_kennzahlen_yaml[
            "kennzahlen"][
            "liquidmin_1"]
        self.liquidmax_1 = self.std_kennzahlen_yaml[
            "kennzahlen"][
            "liquidmax_1"]
        self.liquid_2 = self.std_kennzahlen_yaml[
            "kennzahlen"][
            "liquid_2"]
        self.liquidmin_3 = self.std_kennzahlen_yaml[
            "kennzahlen"][
            "liquidmin_3"]
        self.liquidmax_3 = self.std_kennzahlen_yaml[
            "kennzahlen"][
            "liquidmax_3"]
        self.lagerumschlag = self.std_kennzahlen_yaml[
            "kennzahlen"][
            "lagerumschlag"]
        self.debitorenzahlungsfrist = self.std_kennzahlen_yaml[
            "kennzahlen"][
            "debitorenzahlungsfrist"]
        self.fremdfinanzierungsgradmin = self.std_kennzahlen_yaml[
            "kennzahlen"][
            "fremdfinanzierungsgradmin"]
        self.fremdfinanzierungsgradmax = self.std_kennzahlen_yaml[
            "kennzahlen"][
            "fremdfinanzierungsgradmax"]
        self.eigenfinanzierungsgradmin = self.std_kennzahlen_yaml[
            "kennzahlen"][
            "eigenfinanzierungsgradmin"]
        self.eigenfinanzierungsgradmax = self.std_kennzahlen_yaml[
            "kennzahlen"][
            "eigenfinanzierungsgradmax"]
        self.anlagedeckungsgradmin_1 = self.std_kennzahlen_yaml[
            "kennzahlen"][
            "anlagedeckungsgradmin_1"]
        self.anlagedeckungsgradmax_1 = self.std_kennzahlen_yaml[
            "kennzahlen"][
            "anlagedeckungsgradmax_1"]
        self.anlagedeckungsgrad_2 = self.std_kennzahlen_yaml[
            "kennzahlen"][
            "anlagedeckungsgrad_2"]

        # Options
        self.geschaeftsform = self.bilanz_yaml[
            "Bemerkungen"][
            "geschaeftsform"]
        self.vorraete_anfangs_jahr = self.bilanz_yaml[
            "Bemerkungen"][
            "vorraete_anfangs_jahr"]
        self.debitorenstand_anfangs_jahr = self.bilanz_yaml[
            "Bemerkungen"][
            "debitorenstand_anfangs_jahr"]
        self.umsatzrentabilitaet = self.bilanz_yaml[
            "Bemerkungen"][
            "umsatzrentabilitaet"]
        self.kapitalumschlag = self.bilanz_yaml[
            "Bemerkungen"][
            "kapitalumschlag"]
        self.anlagenintensitaet = self.bilanz_yaml[
            "Bemerkungen"][
            "anlagenintensitaet"]
        self.selbstfinanzierungsgrad = self.bilanz_yaml[
            "Bemerkungen"][
            "selbstfinanzierungsgrad"]
        self.benutzername = self.bilanz_yaml[
            "Bemerkungen"][
            "benutzername"]

        # Bilanz
        self.reingewinn = self.bilanz_yaml[
            "Erfolgsrechnung"][
            "GEWINN"]
        self.zinsen = self.bilanz_yaml[
            "Erfolgsrechnung"][
            "Aufwand"][
            "ZINSEN"]
        self.gesamtkapital = self.bilanz_yaml[
            "Bilanz"][
            "GESAMTVERMOEGEN"]
        self.liquide_mittel = self.bilanz_yaml[
            "Bilanz"][
            "Aktiven"][
            "Umlaufvermoegen"][
            "LIQUIDE_MITTEL"]
        self.forderungen = self.bilanz_yaml[
            "Bilanz"][
            "Aktiven"][
            "Umlaufvermoegen"][
            "DEBITOREN"]
        self.vorraete = self.bilanz_yaml[
            "Bilanz"][
            "Aktiven"][
            "Umlaufvermoegen"][
            "VORRAETE"]
        self.warenaufwand = self.bilanz_yaml[
            "Erfolgsrechnung"][
            "Aufwand"][
            "WARENAUFWAND"]
        self.verkaufserloes = self.bilanz_yaml[
            "Erfolgsrechnung"][
            "Ertrag"][
            "VERKAUFSERLOES"]

        self.kurzfristiges_FK = 0
        for kf_fk in self.bilanz_yaml[
                'Bilanz'][
                'Passiven'][
                'Fremdkapital'][
                'Kurzfristiges_FK'].values():
            self.kurzfristiges_FK += kf_fk

        self.eigenkapital = 0
        for ek in self.bilanz_yaml[
                'Bilanz'][
                'Passiven'][
                'Eigenkapital'].values():
            self.eigenkapital += ek

        self.umlaufvermoegen = 0
        for uv in self.bilanz_yaml[
                "Bilanz"][
                "Aktiven"][
                "Umlaufvermoegen"].values():
            self.umlaufvermoegen += uv

        self.ertrag = 0
        for er in self.bilanz_yaml[
                "Erfolgsrechnung"][
                "Ertrag"].values():
            self.ertrag += er

        self.fremdkapital = 0
        for fk in self.bilanz_yaml[
                "Bilanz"][
                "Passiven"][
                "Fremdkapital"].values():
            for ffk in fk.values():
                self.fremdkapital += ffk

        self.eigenkapital = 0
        for ek in self.bilanz_yaml[
                "Bilanz"][
                "Passiven"][
                "Eigenkapital"].values():
            self.eigenkapital += ek

        self.anlagevermoegen = 0
        for av in self.bilanz_yaml[
                "Bilanz"][
                "Aktiven"][
                "Anlagevermoegen"].values():
            self.anlagevermoegen += av

        self.langfristigesFK = 0
        for lffk in self.bilanz_yaml[
                "Bilanz"][
                "Passiven"][
                "Fremdkapital"][
                "Langfristiges_FK"].values():
            self.langfristigesFK += lffk

    def check_kennzahl_range(self, min, max, name, resultat):
        resultat = round(resultat, 2)
        if resultat >= min and resultat <= max:
            print(
                name, colorful.green(str(resultat) + "% ") +
                "[" + colorful.green("OK") + "]", "Min: " + str(min) +
                "% Max: " + str(max) + "%")
        elif resultat < min:
            print(
                name, colorful.red(str(resultat) + "% ") +
                "[" + colorful.red("Zu Tief") + "]", "Min: " + str(min) +
                "% Max: " + str(max) + "%")
        elif resultat > max:
            print(
                name, colorful.red(str(resultat) + "% ") +
                "[" + colorful.red("Zu Hoch") + "]", "Min: " + str(min) +
                "% Max: " + str(max) + "%")
        else:
            print(
                name, colorful.red(str(resultat) + "% ") +
                "[" + colorful.red("ERROR") + "]", "Min: " + str(min) +
                "% Max: " + str(max) + "%")

    def check_kennzahl(self, wert, name, resultat):
        resultat = round(resultat, 2)
        if name == "Durchschnits-Debitorenzahlungsfrist":
            if resultat < wert:
                print(
                    name, colorful.green(str(resultat)) +
                    " [" + colorful.green("OK") + "]", "Richtwert: " +
                    str(wert))
            else:
                print(
                    name, colorful.red(str(resultat)) +
                    " [" + colorful.red("Zu Hoch") + "]",
                    "Richtwert: " + str(wert))
        elif resultat >= wert:
            print(
                name, colorful.green(str(resultat) + "% ") +
                "[" + colorful.green("OK") + "]", "Richtwert: " +
                str(wert) + "%")
        else:
            print(
                name, colorful.red(str(resultat) + "% ") +
                "[" + colorful.red("Nicht Genug") + "]",
                "Richtwert: " + str(wert) + "%")

    def cal_gesamtkapitalrent(self):
        resultat = (self.reingewinn + self.zinsen) * 100 / self.gesamtkapital
        self.check_kennzahl(
            self.gesamtkapitalrent,
            "Gesamtkapitalrentabilität",
            resultat)

    def cal_liquiditaetsgrad1(self):
        resultat = self.liquide_mittel * 100 / self.kurzfristiges_FK
        self.check_kennzahl_range(
            self.liquidmin_1,
            self.liquidmax_1,
            "Liquiditätsgrad I",
            resultat)

    def cal_liquiditaetsgrad2(self):
        resultat = (
            self.liquide_mittel +
            self.forderungen) * 100 / self.kurzfristiges_FK
        self.check_kennzahl(
            self.liquid_2,
            "Liquiditätsgrad II",
            resultat)

    def cal_liquiditaetsgrad3(self):
        resultat = self.umlaufvermoegen * 100 / self.kurzfristiges_FK
        self.check_kennzahl_range(
            self.liquidmin_3,
            self.liquidmax_3,
            "Liquiditätsgrad III",
            resultat)

    def cal_eigenkapitalrentabilitaet(self):
        resultat = self.reingewinn * 100 / (
            self.eigenkapital - self.reingewinn)
        self.check_kennzahl(
            self.eigenkapitalrent,
            "Eigenkapitalrentabilität",
            resultat)

    def cal_umsatzrentabilitaet(self):
        resultat = self.reingewinn * 100 / self.ertrag
        self.check_kennzahl(
            self.umsatzrentabilitaet,
            "Umsatzrentablilität",
            resultat)

    def cal_kapitalumschlag(self):
        resultat = self.ertrag / self.gesamtkapital
        self.check_kennzahl(
            self.kapitalumschlag,
            "Kapitalumschlag",
            resultat)

    def cal_fremdfinanzierungsgrad(self):
        resultat = self.fremdkapital * 100 / self.gesamtkapital
        self.check_kennzahl_range(
            self.fremdfinanzierungsgradmin,
            self.fremdfinanzierungsgradmax,
            "Fremdfinanierungsgrad",
            resultat)

    def cal_eigenfinanzierungsgrad(self):
        resultat = self.eigenkapital * 100 / self.gesamtkapital
        self.check_kennzahl_range(
            self.eigenfinanzierungsgradmin,
            self.eigenfinanzierungsgradmax,
            "Eigenfinanzierungsgrad",
            resultat)

    def cal_anlageintensitaet(self):
        resultat = self.anlagevermoegen * 100 / self.gesamtkapital
        self.check_kennzahl(
            self.anlagenintensitaet,
            "Anlageveintensität",
            resultat)

    def cal_anlagedeckungsgrad1(self):
        resultat = self.eigenkapital * 100 / self.anlagevermoegen
        self.check_kennzahl_range(
            self.anlagedeckungsgradmin_1,
            self.anlagedeckungsgradmax_1,
            "Anlagedeckungsgrad I",
            resultat)

    def cal_anlagedeckungsgrad2(self):
        resultat = (
            self.eigenkapital +
            self.langfristigesFK) * 100 / self.anlagevermoegen
        self.check_kennzahl(
            self.anlagedeckungsgrad_2,
            "Anlagedeckungsgrad II",
            resultat)

    def cal_lagerumschlag(self):
        avg_warenvorrat = (self.vorraete + self.vorraete_anfangs_jahr) / 2
        resultat = self.warenaufwand / avg_warenvorrat
        self.check_kennzahl(
            self.lagerumschlag,
            "Lagerumschlag",
            resultat)

    def cal_debitorenzahlungsfrist(self):
        avg_debitoren = (
            self.forderungen +
            self.debitorenstand_anfangs_jahr) / 2
        resultat = avg_debitoren * 360 / self.verkaufserloes
        self.check_kennzahl(
            self.debitorenzahlungsfrist,
            "Durchschnits-Debitorenzahlungsfrist",
            resultat)

    def cal_selbstfinanzierungsgrad(self):
        if self.geschaeftsform == "KOLLEKT":
            if self.benutzername is not None:
                grundkapital = self.bilanz_yaml[
                    "Bilanz"][
                    "Passiven"][
                    "Eigenkapital"][
                    self.benutzername]
                anderes_eigen = 0
                for mb in self.bilanz_yaml[
                        "Bemerkungen"][
                        "Mitbesitzer"].values():
                    if mb is not None:
                        anderes_eigen += self.bilanz_yaml[
                            "Bilanz"][
                            "Passiven"][
                            "Eigenkapital"][
                            mb]
                    else:
                        print(colorful.red("Keine Konten gefunden"))
                zuwachskapital = self.eigenkapital - (
                            grundkapital +
                            anderes_eigen)
                resultat = zuwachskapital * 100 / grundkapital
            else:
                print(
                    colorful.red(
                        "Das Konto",
                        self.benutzername,
                        "konnte nicht gefunden werden"))
        else:
            if self.geschaeftsform == "AG":
                grundkapital = self.bilanz_yaml[
                    "Bilanz"][
                    "Passiven"][
                    "Eigenkapital"][
                    "AKTIENKAPITAL"]
            elif self.geschaeftsform == "Einzel":
                grundkapital = self.bilanz_yaml[
                    "Bilanz"][
                    "Passiven"][
                    "Eigenkapital"][
                    "EIGENKAPITAL"]
            elif self.geschaeftsform == "GMBH":
                grundkapital = self.bilanz_yaml[
                    "Bilanz"][
                    "Passiven"][
                    "Eigenkapital"][
                    "STAMMKAPITAL"]
            else:
                print(
                    colorful.red(
                        "Die Geschäftsform: " +
                        str(self.geschaeftsform) +
                        " ist ungültig"))
            zuwachskapital = self.eigenkapital - grundkapital
            resultat = zuwachskapital * 100 / grundkapital

        self.check_kennzahl(
            self.selbstfinanzierungsgrad,
            "Selbstfinanierungsgrad",
            resultat)


    def run_self(self):
        self.cal_eigenkapitalrentabilitaet()
        self.cal_gesamtkapitalrent()
        self.cal_liquiditaetsgrad1()
        self.cal_liquiditaetsgrad2()
        self.cal_liquiditaetsgrad3()
        self.cal_umsatzrentabilitaet()
        self.cal_kapitalumschlag()
        self.cal_fremdfinanzierungsgrad()
        self.cal_eigenfinanzierungsgrad()
        self.cal_anlageintensitaet()
        self.cal_anlagedeckungsgrad1()
        self.cal_anlagedeckungsgrad2()
        self.cal_lagerumschlag()
        self.cal_debitorenzahlungsfrist()
        self.cal_selbstfinanzierungsgrad()
