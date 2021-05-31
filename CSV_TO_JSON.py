import csv
import json

# Alterar os nomes dos aquivos finais dos notebook's (os aquivos csv's) e rodar o programa!
csvfile = open('C:/Users/2104624262/Downloads/volume_vendas_b5.csv', 'r', encoding='UTF-8')
jsonfile = open('C:/Users/2104624262/Downloads/volume_vendas_b5.json', 'w')

fieldnames = ('Pub','idskureferencia','idlojista','estado','nomedepartamento','nomesetor','qtd')
reader = csv.DictReader(csvfile, fieldnames)
out = json.dumps( [row for row in reader ] )
jsonfile.write(out)
