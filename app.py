from flask import Flask, redirect, render_template, request


app = Flask(__name__)

app.secret_key = "banana3"

lista_de_comentario = []

@app.route("/")
def pagina_principal():
    return render_template("principal.html")

@app.route("/sobremim", methods= ["GET"])
def pagina_sobremim():
    return render_template("sobremim.html")

@app.route("/login", methods= ["GET"])
def pagina_login():
    return render_template("login.html")

@app.route("/login", methods= ["POST"])
def login_post():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")

    if usuario == "Carlos" and senha == "123":
        sesssio[usuario] = "Carlos"
        return redirect("/comentarios")
    else:
        return redirect("/login")


    
@app.route("/comentarios", methods= ["GET"])
def pagina_comentarios():
    if "email" in session:

        return render_template("comentarios.html", lista_de_comentario = lista_de_comentario)
    else:
        return redirect("/login.html")


@app.route("/adicionarcomentarios", methods= ["POST"])
def adicionar_comentarios():
    comentario = request.form.get("cmt")
    lista_de_comentario.append(comentario)
    print(lista_de_comentario)
    return redirect("/comentarios")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")