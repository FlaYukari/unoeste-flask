from flask import Flask, render_template, session, request, flash
from Modelo.Pet import Pet #6
from Servidor.Modelo.Cliente import Cliente #6
from Servidor.Persistencia.PetBD import PetBD #7
from Servidor.Persistencia.ClienteBD import ClienteBD #7
from Servidor.Utilitarios.metodosAuxiliares import ehvalidoDadosPet
from Servidor.Utilitarios.metodosAuxiliares import ehvalidoDadosCliente

app = Flask(__name__)

app.secret_key = "minha chave secreta"

def verificarUsuarioAutenticado(): #1- servidor que tem que controlar se o usuário está ou não autenticado, de forma individual e não global
    #2-verificar se o id do usuário está armazenado na sessão
    #3-retorna Verdadeiro ou Falso
    if session.get('id_usuario') !=None:
        #4-return render_template(pagina). pagina estava no def()
        return True
    else:
        #4-return render_template('login.html')
        return False
    

#riquisição do tipo GET ou POST
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

#requisição
@app.route("/menu")
def menu():
    #se o usuário estiver autenticado, então mostre a página menu.html
    #4-return verificarUsuarioAutenticado('menu.html') #2
    #2-return render_template('menu.html')
    #senão mostre ao usuário a págia login.html
    if verificarUsuarioAutenticado(): #4
        return render_template('menu.html')
    else:
        return render_template('login.html')

#requisição
@app.route("/cadastroCliente")
def cadCliente():
    #se o usuário estiver autenticado, então mostre a página menu.html
    #4-return verificarUsuarioAutenticado('cadastroClientes.html') #2
    #2-return render_template('cadastroClientes.html')
    #senão mostre ao usuário a págia login.html
    if verificarUsuarioAutenticado(): #4
        if request.method == "GET": # quer consultar a página
            return render_template('cadastroClientes.html')
        elif request.method == "POST": # quer submeter os dados para o servidor, quer consultar dados, recuperar dados vindos do formulário
            #5-pass
            #nome, rg, cpf, dataNasc, endereco, num, complemento, bairro, cep, cidade, uf, telFixo, telCel
            nomeCliente         = request.form['nomeCliente']
            rgCliente      = request.form['rgCliente']
            cpfCliente         = request.form['cpfCliente']
            dataNascCliente     = request.form['dataNascCliente']
            enderecoCliente          = request.form['enderecoCliente']
            numCliente = request.form['numCliente']
            complementoCliente          = request.form['complementoCliente']
            bairroCliente      = request.form['bairroCliente']
            cepCliente      = request.form['cepCliente']
            cidadeCliente      = request.form['cidadeCliente']
            ufCliente      = request.form['ufCliente']
            telFixoCliente      = request.form['telFixoCliente']
            telCelCliente      = request.form['telCelCliente']
            
            novoCliente = Cliente(0, nomeCliente, rgCliente, cpfCliente, dataNascCliente, enderecoCliente, numCliente, complementoCliente, bairroCliente, cepCliente, cidadeCliente, ufCliente, telFixoCliente, telCelCliente) #6-importou

            #7PRECISAMOS CONDICIONAR A INCLUSÃO DE UM NOVO PET DESDE QUE OS DADOS ESTEJAM VALIDADOS
            
            if ehvalidoDadosCliente(novoCliente):
                clienteBD = ClienteBD() #7-importou
                clienteBD.incluir(novoCliente) #7-importou
                return render_template('cadastroClientes.html')
            else:
                flash('Os dados informados estão inválidos.')
                return render_template('cadastroClientes.html')
    else:
        return render_template('login.html')


@app.route("/cadastroPet")
def cadPet():
    #se o usuário estiver autenticado, então mostre a página menu.html
    #4-return verificarUsuarioAutenticado('cadastroPets.html') #2
    #2-return render_template('cadastroPets.html')
    #senão mostre ao usuário a págia login.html
    if verificarUsuarioAutenticado(): #4
        if request.method == "GET": # quer obter a página
            return render_template('cadastroPets.html')
        elif request.method == "POST": # quer submeter os dados para o servidor, quer consultar dados, recuperar dados vindos do formulário
            #5-pass
            #nome, especie, raca, cor, dataNasc, numMicrochip, rga
            nomePet         = request.form['nomePet']
            especiePet      = request.form['especiePet']
            racaPet         = request.form['racaPet']
            corPet          = request.form['corPet']
            dataNascPet     = request.form['dataNascPet']
            numMicrochipPet = request.form['numMicrochipPet']
            rgaPet          = request.form['rgaPet']

            novoPet = Pet(0, nomePet, especiePet, racaPet, corPet, dataNascPet,         numMicrochipPet, rgaPet) #6-importou
     
            #7-PRECISAMOS CONDICIONAR A INCLUSÃO DE UM NOVO PET DESDE QUE OS DADOS ESTEJAM VALIDADOS ->criacao da parta metodosAuxiliares
            if ehvalidoDadosPet(novoPet):
                petBD = PetBD() #7-importou
                petBD.incluir(novoPet) #7-importou
                return render_template('cadastroPets.html')
            else:
                flash('Os dados informados estão inválidos.')
                return render_template('cadastroPets.html')
            
    else:
        return render_template('login.html')


@app.route("/cadastroProduto")
def cadProduto():
    #se o usuário estiver autenticado, então mostre a página menu.html
    #4-return verificarUsuarioAutenticado('cadastroProdutos.html') #2
    #2-return render_template('cadastroProdutos.html')
    #senão mostre ao usuário a págia login.html
    if verificarUsuarioAutenticado(): #4
        if request.method == "GET": # quer consultar a página
            return render_template('cadastroProdutos.html')
        elif request.method == "POST": # quer submeter os dados para o servidor, quer gravar dados
            pass
    else:
        return render_template('login.html')


@app.route("/logout")
def logout():
    session.clear()
    return render_template('login.html')


app.run("127.0.0.1", port=5000)

