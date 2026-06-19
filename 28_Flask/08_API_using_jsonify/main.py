from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks = {
        "Ayush": 95,
        "Prathamesh": 93,
        "Anush":92,
        "Darshan":98,
        "Mayank":88
    }
    return jsonify(marks)

app.run(debug= True)