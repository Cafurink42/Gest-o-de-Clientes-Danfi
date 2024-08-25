from flask import Blueprint
from flask import render_template,request
from database.cliente import CLIENTES
#blueprint agrupa rotas

client_route = Blueprint("client", __name__)

"""
Rota de Clientes 

/clientes/ (GET) - Listar os clientes
/clintes/ (POST) - Inserir o cliente no servidor
/clientes/new (GET) - Renderizar o formulário par criar um cliente
/clientes/<id> (GET)- Obter os dados de um cliente
/cliente/<id>/edit (GET) - Renderizar um formulário para editar um cliente
/clientes/<id>/update (PUT) - Atualizar os dados do clientes 
/clientes/<id>/delete (DELETE) - Deleta o registro do usuário

"""

@client_route.route("/")
def lista_clientes():
    return render_template("lista_clientes.html", clientes=CLIENTES) ##passando o banco de dados temporario 
##/clientes/ (GET) - Listar os clientes

@client_route.route("/" , methods = ['POST'] ) 
def  inserir_cliente():
     data  = request.json  ##retornando do front-end
     novo_usuario = {
          "id": len(CLIENTES) + 1, ##tamanho da lista + 1
          "nome": data['nome'],
          "email": data['email'],
     }
     
     CLIENTES.append(novo_usuario) ##adicionar novo usuário 

     return render_template("item_cliente.html", cliente = novo_usuario)

##/clintes/ (POST) - Inserir o cliente no servidor

@client_route.route("/new") #por padrão as rotas são get
def  form_cliente():
    return render_template("form_cliente.html")
    pass
##/clientes/new (GET) - Renderizar o formulário par criar um cliente

@client_route.route('/<int:cliente_id>')
def  detalhe_cliente(cliente_id):
    return render_template("detalhe_cliente.html")
    pass
##/clientes/<id> (GET)- Obter os dados de um cliente

@client_route.route('/<int:cliente_id>/edit')
def  form_edit_cliente(cliente_id):
        return render_template("form_edit_cliente.html")

##/cliente/<id>/edit (GET) - Renderizar um formulário para editar um cliente

@client_route.route('/<int:cliente_id>/update', methods = ['PUT'])
def  update_cliente(cliente_id):
    pass
##/clientes/<id>/update (PUT) - Atualizar os dados do clientes 


@client_route.route('/<int:cliente_id>/update', methods = ['DELETE'])
def  delete_cliente(cliente_id):
    global CLIENTES
    CLIENTES = [c for c in CLIENTES if c['id'] != cliente_id]
    return {"deleted": 'ok'}
##/clientes/<id>/delete (DELETE) - Deleta o registro do usuário