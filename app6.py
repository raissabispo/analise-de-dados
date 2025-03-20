import pandas as pd
import matplotlib.pyplot as plt

arquivo_excel = "vendas_anuais.xlsx" 
df = pd.read_excel(arquivo_excel, sheet_name="Sheet1")
print(df.head())

x = df["Ano"]
y = df["Vendas"]

plt.figure(figsize=(8,5))

plt.plot(x,y,marker="o", linestyle="-", color="lightpink", label="Vendas")
plt.xlabel("Ano")
plt.ylabel("Vendas")
plt.title("Vendas por ano")
plt.legend()
plt.grid(True)

plt.show()

