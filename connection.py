import mysql.connector
from flask import Flask, render_template, request

app = Flask(__name__)
app.url_map.strict_slashes = False

conexao = mysql.connector.connect(database='db_usuario', user='root', password='rootroot')
criar_tabela_sql = """CREATE TABLE IF NOT EXISTS tb_usuarios(
                        id int(11) NOT NULL AUTO_INCREMENT,
                        nome VARCHAR(255) NOT NULL,
                        email VARCHAR(255) NOT NULL,
                        senha VARCHAR(255) NOT NULL,
                        PRIMARY KEY (id))"""


cursor = conexao.cursor()
cursor.execute(criar_tabela_sql)
print("Tabela criada com sucesso")


@app.route('/')
def main():
    return render_template('connection.html')


@app.route("/adicionar_usuario", methods=['POST', 'GET'])
def incluir_usuario():
    cursor = conexao.cursor()
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    cursor.execute("""INSERT INTO tb_usuarios(nome, email, senha) VALUES(%s, %s, %s)""", (nome, email, senha))
    conexao.commit()
    cursor.close()
    conexao.close()
    return render_template('connection.html')
    

if __name__ == '__main__':
    app.run(host='localhost', port=5003, debug=True)