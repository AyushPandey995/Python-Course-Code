from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def static_web():
    Marks = {
        "Ayush" : 95,
        "Khushi" : 98,
        "Kanha" : 93,
        "Shraddha" : 91,
        "Omi" : 88,
        "Puchku" : 89,
        "Lucky" : 91,
        "Gulgulli" : 90
    }
    return render_template("index_2.html", Marks= Marks)

app.run(debug= True)
