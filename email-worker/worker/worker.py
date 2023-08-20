import redis
import json
import os # lib para ler variáveis de ambiente
from time import sleep
from random import randint

if __name__ == '__main__':
    # uso da variável de ambiente REDIS_HOST
    redis_host = os.getenv('REDIS_HOST','queue')
    r = redis.Redis(host=redis_host, port=6379, db=0)

    # apenas para que possamos visualizar a chamada ao serviço
    print('Aguardando mensagens...')

    # laço para consumir as mensagens
    while True:
        # vamos pegar a mensagem na fila sender
        mensagem = json.loads(r.blpop('sender')[1])
        # simulando envio de e-mail ...
        print('Mandando a mensagem:',mensagem['assunto'])
        # calculando um randômico inteiro para o Sleep
        sleep(randint(15,35))
        print("Mensagem", mensagem['assunto'], '... enviada com sucesso!')
