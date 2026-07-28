#Nessa aula, vamos aprender como criar estruturas condicionais aninhadas, 
#usando os comandos if.. elif.. else em programas Python.

#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

#%%
print("DESAFIO 036")

casa = float(input("Valor da casa: R$"))
salario = float(input("Salário do comprador: R$"))
anos = int(input("Quantos anos de finacimento? "))

prestacao = casa / (anos * 12)
minimo = salario * 30 / 100

print(f"Para pagar uma casa de R${casa} em {anos}", end=" ")
print(f"a prestação será de R${prestacao:.2f}")

if prestacao <= minimo:
    print("Empréstimo pode ser CONCEDIDO!")
else:
    print("Empréstimo NEGADO!")