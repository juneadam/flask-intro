"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']
DISS = ['stupid','cotton-headed-ninny-muggins','silly']

@app.route('/')
def start_here():
    """Home page."""

    return "<!doctype html><html>Hi! This is the home page.<a href='/hello'>Click here for fun!</a></html>"


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/diss">
          What's your name? <input type="text" name="person">
          <input type="submit" value="Submit">
          AWESOMENESS.
        
        Choose compliment:
          <input type="radio" name="compliment" value="awesome" id="awesome-compliment">
          <label for="awesome-compliment">Awesome</label>
          <input type="radio" name="compliment" value="terrific" id="terrific-compliment">
          <label for="terrific-compliment">Terrific</label>
          <input type="radio" name="compliment" value="fantastic" id="fantastic-compliment">
          <label for="fantastic-compliment">Fantastic</label>
          <input type="radio" name="compliment" value="neato" id="neato-compliment">
          <label for="neato-compliment">neato</label>
          <input type="radio" name="compliment" value="fantabulous" id="fantabulous-compliment">
          <label for="fantabulous-compliment">Fanatabulous</label>
          <input type="radio" name="compliment" value="wowza" id="wowza-compliment">
          <label for="wowza-compliment">Wowza</label>
          <input type="radio" name="compliment" value="oh-so-not-meh" id="oh-compliment">
          <label for="oh-compliment">Oh-so-not-meh</label>
          <input type="radio" name="compliment" value="brilliant" id="brilliant-compliment">
          <label for="brilliant-compliment">brilliant</label>
          <input type="radio" name="compliment" value="incredible" id="incredible-compliment">
          <label for="incredible-compliment">incredible</label>
          <input type="radio" name="compliment" value="ducky" id="ducky-compliment">
          <label for="ducky-compliment">ducky</label>
          <input type="radio" name="compliment" value="coolio" id="coolio-compliment">
          <label for="coolio-compliment">coolio</label>
          <input type="radio" name="compliment" value="wonderful" id="wonderful-compliment">
          <label for="wonderful-compliment">wonderful</label>
          <input type="radio" name="compliment" value="smashing" id="smashing-compliment">
          <label for="smashing-compliment">smashing</label>
          <input type="radio" name="compliment" value="lovely" id="lovely-compliment">
          <label for="lovely-compliment">lovely</label>\

    
        </form>
       
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")
    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """

@app.route('/diss')
def diss_person():
    """Get user by name."""

    player = request.args.get("person")

    diss = choice(DISS)
    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi, {player}! I think you're {diss}!
      </body>
    </html>
    """

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
