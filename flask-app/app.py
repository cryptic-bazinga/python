from flask import Flask, render_template, jsonify, session
import random

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for session

def roll_numbers(profits):
    rolled = 100
    output = []
    consecutive_under_zero = 0
    jackpot_hit = False
    quips = [
        "Better luck next time!",
        "No jackpot for you!",
        "Try again, maybe you'll win!",
        "So close, yet so far!",
        "STOP GAMBLING!",
        "just stop at this point",
        "you should probably stop now",
        "and another and another and another...",
        "99% of gamblers quit before they hit the jackpot",
        "You know, the odds are against you",
        "one more roll and your kid doesn't go to college",
        "you should probably stop now",
        "damn you suck at this..."
        "i can tell your nose is blocking the screen, you jew."
    ]
    for x in range(0, 50):
        rolled = rolled - random.randint(0, 10)
        if rolled < 0:
            consecutive_under_zero += 1
            if consecutive_under_zero == 5:
                output.append(random.choice(quips))
                return output, profits
            chance = random.randint(0, 1)
            if chance == 1:
                rolled = random.randint(5, 20)
            else:
                rolled = random.randint(0, 4)
        else:
            consecutive_under_zero = 0
        if rolled == 5:
            chance = random.randint(0, 4)
            if chance == 1:
                output.append(f"{rolled}")
                output.append("JACKPOT!!!")
                profits += 1100  # Gain 1000 profit for jackpot (accounting for initial 100) 
                jackpot_hit = True
                break
            else:
                break
        output.append(f"{rolled}")
    if not jackpot_hit:
        output.append(random.choice(quips))
    return output, profits

@app.route('/')
def index():
    session['profits'] = 1000  # Reset profits on first load
    output, profits = roll_numbers(session['profits'])
    session['profits'] = profits
    return render_template("index.html", output=output, profits=profits)

@app.route('/reroll')
def reroll():
    profits = session.get('profits', 1000)
    profits -= 100  # Lose 100 profit for every reroll
    output, profits = roll_numbers(profits)
    session['profits'] = profits
    return jsonify({"output": output, "profits": profits})

if __name__ == '__main__':
    app.run(debug=True)
# written by cryptic_innovation / uncertifiedprogrammer
