import json

with open("dados.json", encoding='utf-8') as vendas:
    dados = json.load(vendas)

valores = []
min = 0
max = 0
soma=0
media =0
dias = 0


for i in dados:
    valores.append(i['valor'])

for k in valores:
    if k>max:
       max = k
print("O maior Valor é : {}".format(max))

for l in valores:
    if l>0 and l<k:
        min = l
print("O menor Valor é : {}".format(min)) 


for j in valores:
    soma = soma+j
    media = (soma/len(valores))
print(f"A média é de : {media:.2f}")

for m in valores:
    if m>media:
        dias +=1
print("As vendas ficaram acima da media em {} dias".format(dias))
