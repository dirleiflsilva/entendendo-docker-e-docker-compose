#!/bin/sh

# instalando dependência
pip install bottle==0.12.25 psycopg2==2.9.1 redis==4.0.2

# subindo nossa aplicação
python -u sender.py