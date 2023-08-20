FROM python:3.10
# quem mantem essa imagem
LABEL maintainer 'Dirlei <dirleiflsilva@dfls.eti.br>'

# setar variável de ambiente para não utilizar o buffer de saída
# com isto podemos visualizar as saídas do worker
ENV PYTHONUNBUFFERED 1

# como este arquivo vai substituir o work.sh
RUN pip install redis==4.0.2

ENTRYPOINT ["/usr/local/bin/python"]
