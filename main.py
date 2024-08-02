url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"


#Sanatização da URL
#url = url.replace(" ", "") ou strip()
url = url.strip()

# Validação da URL
if url == "":
    raise ValueError("A URL está vazia! ")

# Separa base e os parâmetros
interrogacao = url.find('?')
url_base = url[:interrogacao]
url_parametros = url[interrogacao+1:]
print(url_parametros)

# Busca o valor de um pârametro
parametro_busca = 'moedaDestino'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)

if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor)