# importando pacotes
import psycopg2
import redis
import json
from bottle import Bottle, request

# classe que vai herdar de Bottle
class Sender(Bottle):
    # criando inicializações
    def __init__(self):
        # super() nos permite sobrescrever métodos e alterar comportamentos
        super().__init__()
        self.route('/',method='POST',callback=self.send)
        # utilizamos o nome do serviço para identificar o host
        self.fila = redis.StrictRedis(host='queue', port=6379, db=0)
        
        # Data Source Name
        # podemos identificar o host pelo IP ou pelo nome do serviço no Compose
        DSN = 'dbname = email_sender user=postgres password=postgres host=db'
        self.conn = psycopg2.connect(DSN)

    # método para conectar no PostgreSQL e gravar os dados
    def register_message(self, assunto, mensagem):
        # query para inserir os dados
        SQL = 'INSERT INTO emails (assunto, mensagem) VALUES (%s, %s)'

        cur = self.conn.cursor()
        cur.execute(SQL, (assunto, mensagem))
        self.conn.commit()
        cur.close()

        # inserir no Redis através do atributo msg  
        msg = {'assunto': assunto, 'mensagem': mensagem}
        # mandando para a fila sender no formato json
        self.fila.rpush('sender', json.dumps(msg))

        print('Mensagem registrada!')  

    # método que irá chamar o método register_message e
    # retornar uma mensagem formatada
    def send(self):
        assunto = request.forms.get('assunto')
        mensagem = request.forms.get('mensagem')

        self.register_message(assunto, mensagem)

        return 'Mensagem enfileirada! Assunto: {} Mensagem: {}'.format(
          assunto, mensagem
        )

# chamando o método na porta 8080
if __name__ == '__main__':
    # criando instancia
    sender = Sender()
    sender.run(host='0.0.0.0', port=8080, debug=True)
