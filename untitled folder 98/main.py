import random
from flask import Flask, render_template, jsonify

app = Flask(__name__)

def get_level():
    difficulties = ["Easy", "Normal", "Hard", "Harder", "Insane", "Easy Demon", "Medium Demon", "Hard Demon", "Insane Demon"]
    difficulty = random.choice(difficulties)

    
    page = random.randint(1, 1000) if difficulty == "Insane" else \
           random.randint(1, 199) if difficulty == "Easy Demon" else \
           random.randint(1, 218) if difficulty == "Medium Demon" else \
           random.randint(1, 151) if difficulty == "Hard Demon" else \
           random.randint(1, 107) if difficulty == "Insane Demon" else \
           random.randint(1, 1000) if difficulty == "Easy" else \
           random.randint(1, 1000) if difficulty == "Normal" else \
           random.randint(1, 1000) if difficulty == "Hard" else \
           random.randint(1, 1000) if difficulty == "Harder" else \
           random.randint(1, 1000)
    
    level = random.randint(1, 10)

    return {
        "difficulty": difficulty,
        "page": page,
        "number": level
    }

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/randomize')
def randomize():
    level = get_level()
    return jsonify(level)

if __name__ == "__main__":
    app.run(debug=True)