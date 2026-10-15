"""Monta o index.html público: python3 build/build.py dados.json DD/MM/AAAA"""
import json, sys, os
here = os.path.dirname(os.path.abspath(__file__))
data = open(sys.argv[1], encoding='utf-8').read()
json.loads(data)  # valida
t = json.load(open(os.path.join(here, 'template.json'), encoding='utf-8'))
page = open(os.path.join(here, 'painel.html'), encoding='utf-8').read()
html = t['pre'] + data + t['mid'] + page + t['tail'].replace('__DATA_VERSAO__', sys.argv[2])
open(os.path.join(here, '..', 'index.html'), 'w', encoding='utf-8').write(html)
print('index.html', len(html), 'bytes')
