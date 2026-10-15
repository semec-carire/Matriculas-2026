import csv, json, sys
src, out = sys.argv[1], sys.argv[2]
rows = list(csv.reader(open(src, encoding='utf-8')))
SERIES = [  # (col idx, serie, ordem, etapa)
 (3,'Berçário',1,'Creche'),(4,'2 anos',2,'Creche'),(5,'3 anos',3,'Creche'),
 (6,'4 anos',4,'Pré-Escola'),(7,'5 anos',5,'Pré-Escola'),
 (8,'1º ano',6,'Anos Iniciais'),(9,'2º ano',7,'Anos Iniciais'),(10,'3º ano',8,'Anos Iniciais'),(11,'4º ano',9,'Anos Iniciais'),(12,'5º ano',10,'Anos Iniciais'),
 (13,'6º ano',11,'Anos Finais'),(14,'7º ano',12,'Anos Finais'),(15,'8º ano',13,'Anos Finais'),(16,'9º ano',14,'Anos Finais'),
 (17,'EJA I',15,'EJA'),(18,'EJA II',16,'EJA'),(19,'EJA III',17,'EJA'),(20,'EJA IV',18,'EJA'),
 (21,'CEJA Anos Finais',19,'CEJA'),(22,'CEJA Ensino Médio',20,'CEJA'),
]
ano = 2026
hdr = rows[0][1].strip()
if len(hdr) >= 4 and hdr[-4:].isdigit(): ano = int(hdr[-4:])
out_rows = []
for r in rows[1:]:
    name = (r[0] if r else '').strip()
    if not name or name.upper().startswith('TOTAL') or 'COM OS ANEXOS' in name.upper(): continue
    escola, unidade = name, name
    if name.upper().startswith('ADAUTA'):
        escola = 'ADAUTA M DE BARROS ROCHA'
        u = name.upper()
        unidade = ('Matriz (Tapuio)' if 'MATRIZ' in u else 'Flores (anexo)' if 'FLORES' in u else 'Lagoa de Fora (anexo)' if 'LAGOA' in u else 'Nossa Senhora (anexo)' if 'NOSSA SENHORA' in u else name)
    upd = r[29].strip().replace('\\','/') if len(r) > 29 else ''
    for idx, serie, ordem, etapa in SERIES:
        v = r[idx].strip() if idx < len(r) else ''
        n = int(float(v)) if v.replace('.','',1).isdigit() else 0
        out_rows.append({'ano_letivo': ano, 'escola': escola, 'unidade': unidade, 'serie': serie, 'ordem': ordem, 'etapa': etapa, 'matriculas': n, 'atualizado_escola': upd})
json.dump(out_rows, open(out,'w',encoding='utf-8'), ensure_ascii=False)
tot = sum(x['matriculas'] for x in out_rows)
print(len(out_rows), 'rows; total', tot, '; sem CEJA', sum(x['matriculas'] for x in out_rows if x['etapa']!='CEJA'))
