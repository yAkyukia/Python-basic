real = float(input("quantos reais você possue: "))
dolar = 5.15
conversao = (real//dolar)
troco = (real%dolar)
print(f"com {real} reais você consegue {conversao} dolares e lhe sobra {troco}")

