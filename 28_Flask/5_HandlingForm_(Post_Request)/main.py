from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods= ["GET", "POST"])
def static_web():
    print(request.method)
    print(request.form)
    if request.method == "POST" :
        with open(f"created_emails/{request.form["name"]}.txt", "w") as f:
            f.write(f"Name of student - {request.form["name"]}\nEmail I'd of student - {request.form["email"]}")
        return render_template("index.html")
    else:
        return render_template("index.html")
app.run(debug= True)