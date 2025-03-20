from wordcloud import WordCloud
import matplotlib.pyplot as plt 

texto = "Uma Word Cloud (ou nuvem de palavras, em português) é uma representação visual de palavras em que a frequência de cada palavra é indicada pelo seu tamanho: palavras mais frequentes aparecem em maior tamanho, enquanto palavras menos frequentes aparecem em tamanho menor. Essa técnica é usada para fornecer uma visão rápida de quais termos são mais recorrentes em um conjunto de textos."

nuvem = WordCloud(width=800, height = 400, background_color="white").generate(texto)

plt.figure(figsize=(10,5))

plt.imshow(nuvem, interpolation="bilinear")

plt.axis("off")

plt.show()