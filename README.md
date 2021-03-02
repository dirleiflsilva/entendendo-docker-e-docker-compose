# Entendendo Docker e Docker Compose

O que um desenvolvedor de software precisa saber sobre Docker e Docker Compose?

Não tenho a intenção de explicar o que é Docker ou Docker Compose, muito menos de demonstrar como essas ferramentas são instaladas. As páginas de documentação das mesmas já o fazem de maneira simples e objetiva, então te convido a visitar os links abaixo e verificar como isto pode ser realizado no seu sistema operacional.

Página de documentação do [Docker](https://docs.docker.com/).

Página de documentação do [Docker Compose](https://docs.docker.com/compose/).

Vou tentar trazer as informações de maneira prática e objetiva, mas aumentando a complexidade das coisas aos poucos, como nós programadores aprendemos: precisamos abstrair a complexidade do problema a ser resolvido, ou seja, vamos dividir um problema "grandão" em pequenos problemas e resolvê-los por partes.

Mas para isso precisamos primeiro definir qual é o nosso problema e como vamos usar as ferramentas que temos disponíveis para chegar ao nosso objetivo.

Então vamos começar!

Antes de mais nada, não sou especialista em nenhuma das ferramentas que serão utilizadas neste "projeto", esta é uma forma que tenho para aprender mais e entender como as coisas funcionam. Teoria é importante, mas é vazia sem colocar o que você aprendeu em prática. 

E por que fazer tudo isso? 

Já faz um tempo que brinco com Docker, mas a algumas semanas atrás fiz um [bootcamp de Engenheria de Dados no IGTI](https://www.igti.com.br/custom/engenharia-de-dados/), onde foi apresentado o [Apache Airflow](https://airflow.apache.org/) pelo [Prof. Neylson Crepalde](https://www.linkedin.com/in/neylsoncrepalde/), com múltiplos containers. fiquei entusiasmado com aquilo.

Mas nada disso saiu do zero, há algum tempo eu adquiri um [curso de Docker do Prof. Leonardo Leitão da Cod3r](https://www.cod3r.com.br/courses/docker) , acho que você já notou que adoro fazer cursos e aprender coisas novas, e meu entusiasmo com o Airflow me fez agilizar meu aprendizado de Docker e Docker Compose.

## Coordenando múltiplos containers

Vamos exemplificar a criação de uma aplicação com múltiplos serviços utilizando o Docker e o Docker Compose para orquestrar os mesmos. Então nosso primeiro passo é definir quais serão esses serviços e qual o objetivo desta aplicação.

Nosso projeto será uma aplicação simples para envio de e-mails com Workers, na realidade vamos criar a estrutura e simular esse envio. Para isso precisamos criar os componentes abaixo:

* Banco de Dados
* Servidor Web
* Gerenciador de filas
* Workers para envio de e-mail
* Aplicação principal

Podemos visualizar a estrutura desses serviços conforme segue.

![Componentes](images/app-docker-compose.png)

O Docker Compose usa um arquivo de configuração no padrão [YAML](https://yaml.org), que tem sua especificação neste [link](https://github.com/compose-spec/compose-spec/blob/master/spec.md).

## Iniciando com o banco de dados

Vamos utilizar o PostgreSQL 9.6 para persistir nosso dados, um detalhe no desenvolvimento de um projeto com vários serviços é utilizar uma versão específica dos componentes, isto vai evitar que sua aplicação quebre, pois no Docker, quando não é informada a versão será utilizada a mais recente, com a tag *latest*.

~~~yaml
version: '3'
services:
  db:
    image: postgres:9.6
~~~

Aqui temos a estrutura básica do docker-compose.yml, onde declaramos que estamos utilizando a versão 3, definindo as capacidades do docker-compose, este detalhe tentaremos explorar mais a fundo em outro momento.

Para que a mágica aconteça, só precisamos digitar o comando abaixo, que levanta o serviço em modo *daemon*:

~~~bash
docker-compose up -d
~~~

Para verificar se o serviço subiu podemos usar ...

~~~bash
docker-compose ps
~~~

... similar ao *docker ps**, mas restrito apenas aos serviços indicados no docker-compose.yml.

De forma similar, podemos executar um comando interno do PostgreSQL no container:

~~~bash
docker-compose exec db psql -U postgres -c '\l'
~~~

E finalmente podemos parar o(s) serviço(s) e remover o(s) container(s), que foram declarados no docker-compose.yml como o comando abaixo:

~~~bash
docker-compose down
~~~



