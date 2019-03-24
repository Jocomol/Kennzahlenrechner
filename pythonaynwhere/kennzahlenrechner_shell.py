from Kennzahlenrechner.kennzahlenrechner import Kennzahlenrechner
import os

def interactive():
    user_input = "?"
    running = True
    while running:
        if user_input == "help" or user_input == "?" or user_input == "Help":
            print(
                    "--------------------------" +
                    "------------------------------------")
            print(
                    " start           |" +
                    " Startet den Kennzahlenrechner             |")
            print(
                    " bilanz          |" +
                    " Öffnet das Bilanzbearbeitungs Fenster     |")
            print(
                    " kennzahlen      |" +
                    " Öffnet das Kennzahlenbearbeitungs Fenster |")
            print(
                    " help / ? / Help |" +
                    " Zeigt diese Hilfe an                      |")
            print(
                    " exit            |" +
                    " Beendet das Programm                      |")
            print(
                    "------------------------------" +
                    "--------------------------------")
        elif user_input == "start":
            rechner = Kennzahlenrechner()
            rechner.run()
        elif user_input == "bilanz":
            os.system("nano /home/Jocomol/kennzahlen_files/bilanz.yml")
        elif user_input == "kennzahlen":
            os.system(
                    "nano /home/Jocomol/kennzahlen_files" +
                    "/std_kennzahlen.yml")
        elif user_input == "exit":
            running = False
            break
        else:
            print(user_input,"ungültige Eingabe")

        user_input = input("kennzahlenrechner command: ")

if __name__ ==  "__main__":
    interactive()
