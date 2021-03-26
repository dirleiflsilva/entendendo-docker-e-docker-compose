# importando pacote
from bottle import route, run, request

# criando uma rota no raiz, que atende requisições POST
@route('/', method='POST')

# método que irá gravar no banco dados, mas por enquanto 
# só vamos retornar uma mensagem formatada do formulário 
# submetido pelo front-end
def send():
    assunto = request.forms.get('assunto')
    mensagem = request.forms.get('mensagem')
    return 'Mensagem enfileirada! Assunto: {} Mensagem: {}'.format(
      assunto, mensagem
    )

# chamando o método na porta 8080
if __name__ == '__main__':
    run(host='0.0.0.0', port=8080, debug=True)
