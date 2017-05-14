import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
import os
import wifi

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)
with open(".env") as f:
  for line in f.readlines():
    parts = line.split("=")
    key = parts[0]
    val = parts[1].replace("\n", "")
    os.environ[key] = val

@ask.launch
def new_game():
    welcome_msg = render_template('welcome')
    return question(welcome_msg)


@ask.intent("ListPeopleInHouse")
def list_people_in_house():
  people = wifi.people_online()
  print "-"*10, people, "-"*10
  if len(people) == 0:
    return statement("nobody is home.")
  if len(people) == 1:
    return statement("only {name} is home.".format(name=people[0]))
  msg = ", ".join(people[:len(people)-1])
  msg = "{commas} and {last} are home.".format(commas=msg, last=people[-1])
  return statement(msg)


@ask.intent("YesIntent")
def next_round():
    numbers = [randint(0, 9) for _ in range(3)]
    round_msg = render_template('round', numbers=numbers)
    session.attributes['numbers'] = numbers[::-1]  # reverse
    return question(round_msg)


@ask.intent("AnswerIntent", convert={'first': int, 'second': int, 'third': int})
def answer(first, second, third):
    winning_numbers = session.attributes['numbers']
    if [first, second, third] == winning_numbers:
        msg = render_template('win')
    else:
        msg = render_template('lose')
    return statement(msg)


if __name__ == '__main__':
    app.run(debug=True, port=7242, host="0.0.0.0")
