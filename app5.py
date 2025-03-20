from collections import Counter 
import matplotlib.pyplot as plt 
from wordcloud import WordCloud


texto = """
Uma Word Cloud (ou nuvem de palavras, em português) é uma representação visual de palavras em que a frequência de cada palavra é indicada pelo seu tamanho: palavras mais frequentes aparecem em maior tamanho, enquanto palavras menos frequentes aparecem em tamanho menor. Essa técnica é usada para fornecer uma visão rápida de quais termos são mais recorrentes em um conjunto de textos." 

"""

palavras = texto.lower().replace(",", "").replace(".", "").split()

contagem = Counter(palavras)

palavras_mais_comuns = contagem.most_common(10)
palavras, frequencias = zip(*palavras_mais_comuns)

plt.figure(figsize=(10, 5))
plt.bar(palavras, frequencias, color="lightpink")
plt.title("Frequência das Palavras Mais Comuns", fontsize=16)
plt.xlabel("Palavras", fontsize=12)
plt.ylabel("Frequência", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
