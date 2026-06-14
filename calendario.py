#%%
import calendar

ano = int(input("Entre com o Ano: "))
mes = int(input("Entre com o Mês: "))

cal = calendar.month(ano, mes)
print(cal)