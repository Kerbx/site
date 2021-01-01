from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/bio')
def bio():
    return render_template("bio.html")


@app.route('/galery')
def galery():
    return render_template("galery.html")


if __name__ == "__main__":
    app.run(debug=True)
