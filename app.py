from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  # Profile selection page

@app.route("/homepage")
def homepage():
    return render_template("homepage.html")  # Homepage

@app.route("/profile")
def profile():
    return render_template("profile.html")  # Profile page

@app.route("/works")
def works():
    return render_template("works.html")  # Works page

if __name__ == "__main__":
    app.run(debug=True)
