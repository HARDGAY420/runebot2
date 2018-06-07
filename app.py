from flask import Flask
import bot
app = Flask(__name__)

@app.route("/")
def main():
    #return "Welcome!"
    return bot.py

if __name__ == "__main__":
    app.run()