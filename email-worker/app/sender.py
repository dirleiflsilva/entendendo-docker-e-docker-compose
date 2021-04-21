# importando pacotes
import psycopg2
from bottle import route, run, request

# Data Source Name
# podemos identificar o host pelo IP ou pelo nome do serviço no Compose
DSN = 'dbname = email_sender user=postgres password=postgres host=db'

# query para inserir os dados
SQL = 'INSERT INTO emails (assunto, mensagem) VALUES (%s, %s)'

# método para conectar no PostgreSQL e gravar os dados
def register_message(assunto, mensagem):
    conn = psycopg2.connect(DSN)
    cur = conn.cursor()
    cur.execute(SQL, (assunto, mensagem))
    conn.commit()
    cur.close()
    conn.close()

    print('Mensagem registrada!')  

# criando uma rota no raiz, que atende requisições POST
@route('/', method='POST')

# método que irá chamar o método register_message e
# retornar uma mensagem formatada
def send():
    assunto = request.forms.get('assunto')
    mensagem = request.forms.get('mensagem')

    register_message(assunto, mensagem)
    
    return 'Mensagem enfileirada! Assunto: {} Mensagem: {}'.format(
      assunto, mensagem
    )

# chamando o método na porta 8080
if __name__ == '__main__':
    run(host='0.0.0.0', port=8080, debug=True)
