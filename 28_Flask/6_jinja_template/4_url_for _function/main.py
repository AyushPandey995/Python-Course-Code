from flask import Flask, render_template

# app = Flask(__name__, static_url_path= "/public") #This is how we can change the path of files present in static folder.

# app = Flask(__name__, static_folder= "assets") #This is how we can replace the static folder with other folder.

# app = Flask(__name__, static_folder= "assets", static_url_path="/static") #This is how we can replace the static folder with other folder and use 'static' in url

app = Flask(__name__, static_folder= "assets")

@app.route("/")
def static_web():
    return render_template("index.html")

app.run(debug= True)