#exercícios de Python no Exercism.

#%%

#(Olá, mundo!)

def hello():
    return "Hello, World!"
print(hello())

#%%

a = 1

while a <= 10:
    a = a + a
print(a)

#%%

def soma(a, b, c):
    return a + b + c

print(soma(2, 2, 2))
print(soma(3, 3, 3))

#%%
nome = str(input("Digite seu nome: "))

def boasvindas(nome):
    return f"Seja-Bem-Vinda, {nome}!"

print(boasvindas(nome))