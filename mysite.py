from flask import Flask
import random

app = Flask(__name__)


@app.route("/user/<username>/<lastname>") 
 
def index(username,lastname):
    symbol=["-","_","*","","!"]
    return f"{username}{random.choice(symbol)}{lastname}".lower()
    


app.run()

