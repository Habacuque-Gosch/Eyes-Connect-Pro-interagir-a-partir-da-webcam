from flask import Flask


app = Flask(__name__)

app.secret_key = "Computer Vision"

from views import *

if __name__ == "__main__":
    app.run(debug=True)