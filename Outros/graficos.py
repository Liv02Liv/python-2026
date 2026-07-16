
#%%

import matplotlib.pyplot as plt

mes = ["Jan", "Feb", "Mar", "Abr", "Mai"]
vendas = [250, 320, 280, 450, 390]

plt.plot(mes, vendas)
plt.grid(True)
plt.show()

#%%
import matplotlib.pyplot as plt

mes = ["Jan", "Feb", "Mar", "Abr", "Mai"]
vendas = [250, 320, 280, 450, 390]

plt.plot(mes, vendas, color= "green", linestyle= "--", marker= "o")
plt.grid(True)
plt.show

#%%
import matplotlib.pyplot as plt

mes = ["Jan", "Feb", "Mar", "Abr", "Mai"]
vendas = [250, 320, 280, 450, 390]

plt.plot(mes, vendas, label= "Vendas")
plt.xlabel("Mês")
plt.ylabel("Vendas")
plt.title("Vendas no Mês")
plt.legend()
plt.grid(True)
plt.show

#%%
import matplotlib.pyplot as plt

mes = ["Jan", "Feb", "Mar", "Abr", "Mai"]
vendas = [250, 320, 280, 450, 390]


plt.bar(mes, vendas, color= "skyblue")
plt.show

#%%
import matplotlib.pyplot as plt

marcas = [88, 92, 76, 95, 67, 81, 70, 85]

plt.hist(marcas, bins= 5, color= "orange")
plt.show

#%%
import matplotlib.pyplot as plt

idade = [21, 22, 20, 23, 21, 22]
marcas = [88, 92, 76, 95, 67, 81]

plt.scatter(idade, marcas, color="red")
plt.grid(True)
plt.show()

#%%
import matplotlib.pyplot as plt

tamanho = [40, 30, 20, 10]
rotulos = ["Python", "Java", "C++", "Other"]

plt.pie(tamanho, labels=rotulos, autopct="%1.1f%%")
plt.show()

#%%
import matplotlib.pyplot as plt

vendas_2023 = [250, 320, 280, 450, 390]
vendas_2024 = [300, 360, 310, 500, 420]
mes = ["Jan", "Feb", "Mar", "Abr", "Mai"]

plt.plot(mes, vendas_2023, label="2023")
plt.plot(mes, vendas_2024, label="2024")
plt.legend()
plt.grid(True)
plt.show()

#%%
import matplotlib.pyplot as plt

mes = ["Jan", "Feb", "Mar", "Abr", "Mai"]
vendas = [250, 320, 280, 450, 390]

plt.subplot(1, 2, 1)
plt.plot(mes, vendas)
plt.grid(True)
plt.subplot(1, 2, 2)
plt.bar(mes, vendas)
plt.show()

#%%
import matplotlib.pyplot as plt

mes = ["Jan", "Feb", "Mar", "Abr", "Mai"]
vendas = [250, 320, 280, 450, 390]

plt.style.use("ggplot")
plt.plot(mes, vendas)
plt.grid(True)
plt.show()

#%%
import matplotlib.pyplot as plt

mes = ["Jan", "Feb", "Mar", "Abr", "Mai"]
vendas = [250, 320, 280, 450, 390]

plt.figure(figsize=(8, 4))
plt.plot(mes, vendas)
plt.show()

#plt.savefig("sales_chart.png")