num1 =0
num2 =1
num3 = 0
usuario = int(input("Qual numero deseja consultar"))

while usuario>num3:
    num3 = num1+num2
    num1 =num2
    num2 = num3
    
    if usuario == 0 or usuario ==1 or usuario == num3:
        print("O numero {} consta na sequencia".format(usuario))
        break
    else:
        print("O numero {} não consta na sequencia".format(usuario))
        
        


