from flask import Flask, flash, render_template, redirect

app = Flask(__name__)

app.secret_key="jnh67326aw35pmx56c5ryr4y6vb"

@app.route("/")
def login():
    return render_template("2_index.html")

@app.route("/logout")
def logout():
    flash("You have been logged out!", "success")
    return redirect("/")

app.run(debug= True)