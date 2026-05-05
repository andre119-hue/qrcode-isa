from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

SENHA = ["isabella", "Isabella"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/verificar", methods=["POST"])
def verificar():
    senha = request.form.get("senha")

    if senha in SENHA:
        return redirect(url_for("poema"))
    else:
        return "Senha incorreta 😢"

@app.route("/poema")
def poema():
    return render_template("poema.html")

if __name__ == "__main__":
    app.run(debug=True)
