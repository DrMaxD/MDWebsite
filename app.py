from flask import Flask, render_template

# Create a Flask app instance with the root directory as the template folder
app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/resume')
def resume():
    return render_template("templates/resume.html")

@app.route('/aboutme')
def aboutme():
    return render_template("templates/aboutme.html")

@app.route('/projects')
def projects():
    return render_template("templates/projects.html")

@app.route('/contactme')
def contactme():
    return render_template("templates/contactme.html")

if __name__ == "__main__":
    app.run(debug=True)