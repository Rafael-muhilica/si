from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def inicio():
    return render_template("inicio.html")
@app.route("/sobre")
def sobre():
    return render_template("sobre.html")
@app.route("/sobre")
def base():
    return render_template("base.html")
@app.route("/contato")
def contacto():
    return render_template("contato.html")
if __name__ == "__main__":
    app.run(debug = True)