import telebot
from flask import Flask
import time
from const import AccountType
from hiscores import Hiscores

app = Flask(__name__)

bot_token = "606742085:AAGKWDvVOH6R71mgPgeJdDkT4llp80vlso4"

bot = telebot.TeleBot(token=bot_token)


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "This is BOTonaan sisään v0.2.\nUse the command '/user=username' to fetch OSRS "
                          "stats of player 'username'.\nUse command 'user=username=skill' to get the level "
                          "of skill 'skill' of player 'username'.")

@bot.message_handler(commands=['kokonaan'])
def send_sisaan(message):
    bot.reply_to(message, "sisään")

@bot.message_handler(commands=['mutsis'])
def send_sisaan(message):
    bot.reply_to(message, "pillu")

@bot.message_handler(func=lambda msg: msg.text is not None and '/user=' in msg.text)
def at_answer(message):
    texts = message.text.split("=")
    username = texts[1]

    try:
        get_user = Hiscores(username)
        asd = get_user.skills
        total_lvl = 0
        koko = ""

        for key, value in asd.items():
            koko += key
            koko += " : "
            koko += str(value.level)
            total_lvl += value.level

            koko += '\n'

        koko += "TOTAL LEVEL : "
        koko += str(total_lvl)
        bot.reply_to(message, koko)
    except:
        bot.reply_to(message, "Unable to find player %s" % username)


@bot.message_handler(func=lambda msg: msg.text is not None and '/userskill=' in msg.text)
def at_skill(message):
    try:
        commands = message.text.split("=")
        username = commands[1]
        skill = commands[2]
        get_skills = Hiscores(username)

        skill_level = get_skills.skills[skill].level

        username += "'s "
        username += skill
        username += " level is: "
        username += str(skill_level)
        bot.reply_to(message, username)

    except:
        bot.reply_to(message, "Invalid input. Use '/help' for help.")


"""while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)"""
@app.route("/")
def main():
    while True:
        bot.polling()
if __name__ == "__main__":
    app.run()