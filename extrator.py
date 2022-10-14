import fitz

#Abrir o arquivo pdf aqui
with fitz.open("x") as pdf:
    texto = ""
    
    for pagina in pdf:
        texto += f'{pagina.getText()}\n'

print(texto)