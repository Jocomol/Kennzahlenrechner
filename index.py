from flask import Flask
from kennzahlenrechner import Kennzahlenrechner
import sys
import io

app = Flask(__name__)

@app.route("/")
def index():
    stdout_ = sys.stdout 
    stream = io.StringIO()
    sys.stdout = stream
    programm = Kennzahlenrechner()
    programm.run_self()
    sys.stdout = stdout_
    variable = stream.getvalue()
    return variable

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
