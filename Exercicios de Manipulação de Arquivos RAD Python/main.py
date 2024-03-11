#Tirar os comentários e executar um por vez

'''
#1 - Vamos ler e abrir o arquivo

arquivo = open('nomes.txt', 'r')
print(arquivo)
print(arquivo.read())
'''

'''
#2 - Vamos criar e ler um arquivo

#Criando e Escrevendo
f  = open('teste.txt', 'w')
f.write('texto 1')
f.close()

#Lendo
f = open('teste.txt', 'r')
print(f.read())
f.close()
'''

'''
#3 - Criar e ler um arquivo com o with

#Criando e escrevendo
with open('teste.txt', 'w') as f:
    f.write('texto 1\n')
    f.write('texto 2')

#lendo o arquivo
with open('teste.txt', 'r') as f:
    print(f.read())
'''

'''
#4 - Ler linha de um arquivo com o readline()

f = open('nomes.txt','r')
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
f.close()
'''

'''
#5 - Ler linha de um arquivo com o readline()
f = open('nomes.txt', 'r')
print(f.readline(50))
f.close
'''

'''
#6 - Ler toda as linha de um arquivo com laço de repetição for:

f = open('nomes.txt', 'r')
for linha in f:
    print(linha)
f.close()
'''

'''
#7 - Ler as linha de um arquivo com o for e separar as palavras de cada linha com o método split():
f = open('nomes.txt', 'r')
for linha in f:
    print(linha.split())
f.close
'''

'''
#8 - Abrir um arquivo txt e escrever elemento de uma lista:
f = open('nomes.txt', 'w+')

texto = ['palavra 1', "palavra 2 ", "palavra 3"]

for linha in texto:
    f.write(linha)
    f.write("\n")
f.close()
'''

'''
#9 - É possivel ler cada linha diretamente do arquivo sem readline() e/ou readlines():

f = open('nomes.txt', 'r')

for linha in f:
    print(linha)
f.close()
'''

'''
#10 - Ler um arquivo com caracteres acentuados:

f = open('arquivo_portugues.txt','r', encoding = "utf-8")

print(f.read())
f.close()
'''
