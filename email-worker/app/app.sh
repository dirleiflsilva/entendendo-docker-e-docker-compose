#!/bin/sh

# instalando dependência
pip install bottle==0.12.13 psycopg2==2.7.4 redis==2.10.5

# subindo nossa aplicação
python -u sender.py