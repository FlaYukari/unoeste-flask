from flask import Flask, render_template, session, request, flash

app = Flask(__name__)

app.secret_key = "minha chave secreta"

def verificarUsuarioAutenticado(pagina): #1- servidor que tem que controlar se o usuário está ou não autenticado, de forma individual e não global
    #2-verificar se o id do usuário está armazenado na sessão
    if session.get('id_usuario') !=None:
        return render_template(pagina)
    else:
        return render_template('login.html')
    

#riqueisição do tipo GET ou POST
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        req_usuario = request.form['usuario'] #atributo name no login.html
        req_senha = request.form['senha'] #atributo name no login.html
        #acessar o banco de dados...
        if req_usuario == "jose" and req_senha == '123':
            session.clear()
            session['id_usuario'] = '123456'
            return render_template('menu.html')
        else:
            flash("Autenticação negada!")
            return render_template('login.html')


@app.route("/menu")
def menu():
    #se o usuário estiver autenticado, então mostre a página menu.html
    return verificarUsuarioAutenticado('menu.html') #2
    #2-return render_template('menu.html')
    #senão mostre ao usuário a págia login.html


@app.route("/cadastroCliente")
def cadCliente():
    #se o usuário estiver autenticado, então mostre a página menu.html
    return verificarUsuarioAutenticado('cadastroClientes.html') #2
    #2-return render_template('cadastroClientes.html')
    #senão mostre ao usuário a págia login.html


@app.route("/cadastroPet")
def cadPet():
    #se o usuário estiver autenticado, então mostre a página menu.html
    return verificarUsuarioAutenticado('cadastroPets.html') #2
    #2-return render_template('cadastroPets.html')
    #senão mostre ao usuário a págia login.html


@app.route("/cadastroProduto")
def cadProduto():
    #se o usuário estiver autenticado, então mostre a página menu.html
    return verificarUsuarioAutenticado('cadastroProdutos.html') #2
    #2-return render_template('cadastroProdutos.html')
    #senão mostre ao usuário a págia login.html


@app.route("/logout")
def logout():
    session.clear()
    return render_template('login.html')


app.run("127.0.0.1", port=5000)

