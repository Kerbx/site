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


@app.route("/st")
def st():
    return render_template('st.html')


@app.route("/1")
def s1():
    return render_template('1.html')


@app.route("/2")
def s2():
    return render_template('2.html')


@app.route("/3")
def s3():
    return render_template('3.html')


@app.route("/4")
def s4():
    return render_template('4.html')


if __name__ == "__main__":
    app.run(debug=True)
