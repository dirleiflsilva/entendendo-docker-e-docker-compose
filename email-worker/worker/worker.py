import redis
import json
from time import sleep
from random import randint

if __name__ == '__main__':
    r = redis.Redis(host='queue', port=6379, db=0)
    # laço para consumir as mensagens
    while True:
        # vamos pegar a mensagem na fila sender
        mensagem = json.loads(r.blpop('sender')[1])
        # simulando envio de e-mail ...
        print('Mandando a mensagem:',mensagem['assunto'])
        # calculando um randômico inteiro para o Sleep
        sleep(randint(15,35))
        print("Mensagem", mensagem['assunto'], '... enviada com sucesso!')
