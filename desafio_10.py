v = float(input("escreva o preço: "))
p = float(input("escreva a porcentagem do desconto: "))
r= (v/100*p)
vf = (v-r)
print(f"valor final: {vf}")