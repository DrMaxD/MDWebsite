from flask import render_template

from db.server import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/resume')
def resume():
    return render_template("resume.html")

@app.route('/aboutme')
def aboutme():
    return render_template("aboutme.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.route('/contactme')
def contactme():
    return render_template("contactme.html")

if __name__ == "__main__":
    app.run(debug=True)