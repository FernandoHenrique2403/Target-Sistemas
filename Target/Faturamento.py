sp = 67836.43
rj = 36678.55
mg = 29229.88
es = 27165.48
outros= 19849.53

total = (sp+rj+mg+es+outros)
print(f"O total de vendas é : R$ {total}")

sp2 = ((sp/total)*100)
rj2 = ((rj/total)*100)
mg2 = ((mg/total)*100)
es2 = ((es/total)*100)
outros2 = ((outros/total)*100)

print(f'Porcentagem de SP {sp2:.2f}')
print(f'Porcentagem de RJ {rj2:.2f}')
print(f'Porcentagem de MG {mg2:.2f}')
print(f'Porcentagem de ES {es2:.2f}')
print(f'Porcentagem de OUT {outros2:.2f}')