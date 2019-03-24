from flask import Flask
from kennzahlenrechner import Main

app = Flask(__name__)

@app.route("/")
def index():
    programm = Main()
    programm.run_self

if __name__ == "__main__":
app.run(host='0.0.0.0', port=80)
