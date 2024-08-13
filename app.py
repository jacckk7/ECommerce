from flask import Flask

# Instanciando aplicação
app = Flask(__name__)

# Definindo uma rota raiz (página inicial) e a função que será executada ao requisitar
@app.route('/')
def hello_world():
    return 'Hello World'

# Roda a aplicação apenas se for a primeria instância (evita redundância)
if __name__=='__main__':
    app.run(debug=True)