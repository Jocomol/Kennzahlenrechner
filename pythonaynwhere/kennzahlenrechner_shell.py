from kennzahlenrechner import Kennzahlenrechner
import os

def interactive():
    user_input = "?"
    running = True
    while running:
        if user_input is "help" or user_input is "?" or user_input is "Help":
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
        elif user_input is "start":
            rechner = Kennzahlenrechner()
            rechner.run()
        elif user_input is "bilanz":
            os.system("nano /home/Jocomol/kennzahlen_files/bilanz.yml")
        elif user_input is "kennzahlen":
            os.system(
                    "nano /home/Jocomol/kennzahlen_files" +
                    "/std_kennzahlen.yml")
        elif user_input is "exit":
            running = False
            break
        else:
            print(user_input,"ungültige Eingabe")

        user_input = input("kennzahlenrechner command: ")

if __name__ == "__main__":
    interactive()
