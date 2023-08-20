# importando pacotes
import psycopg2
import redis
import json
import os # lib para ler variáveis de ambiente
from bottle import Bottle, request

# classe que vai herdar de Bottle
class Sender(Bottle):
    # criando inicializações
    def __init__(self):
        # super() nos permite sobrescrever métodos e alterar comportamentos
        super().__init__()
        self.route('/',method='POST',callback=self.send)
        
        # uso da variável de ambiente REDIS_HOST
        # se não for localizada a variável ou seu conteúdo
        # será utilizado um padrão, no caso <queue>
        redis_host = os.getenv('REDIS_HOST','queue')
        self.fila = redis.StrictRedis(host=redis_host, port=6379, db=0)
        
        # Diversas variáveis de ambiente (incluindo o DB_NAME)
        db_host = os.getenv('DB_HOST', 'db')
        db_user = os.getenv('DB_USER', 'postgres')
        db_psw = os.getenv('DB_PSW', 'postgres')
        db_name = os.getenv('DB_NAME','sender') 
        # note que db_name está diferente do usado até agora
        # mas em seguida vamos mostrar que esta variável será
        # exposta no <docker-compose.yaml>
 
        # Uso das variáveis de ambiente para conexão com o banco de dados
        dsn = f'dbname={db_name} user={db_user} password={db_psw} host={db_host}'
        print(dsn)
        self.conn = psycopg2.connect(dsn)
        
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
