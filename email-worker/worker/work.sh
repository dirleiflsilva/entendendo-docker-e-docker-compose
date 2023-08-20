#!/bin/bash

# instalando dependência
pip install redis==4.0.2

# subindo o worker
python -u worker.py