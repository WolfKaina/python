#Strings

print ("Hello World!")
print ('Hello World!')
print ('''Hello World!''')
hello = """Hello

separado do jeito que  o código está

World!"""
print (hello)


#Concatenar
nome = "Kainã"
sobrenome = "Santos"
nome_completo = nome + " " + sobrenome
print (nome_completo)

#Multiplicando string
eco = "Olá! " * 3
print  (eco)

#Acessando letras (Índice e Fatiamento)
palavra = "KAINÃ"

#pegando letra especíca usando colchetes:
print(palavra[0]) # K (Primeira Letra)
print(palavra[1]) # A (Segunda Letra)
print(palavra[2]) # I (Terceira Letra e segue sucessivamente)
print(palavra[3]) # I (Terceira Letra e segue sucessivamente)
print(palavra[-1]) # Ã (Ultima Letra)

#Fatiamento 
print(palavra [0:2]) # KA (Pega do 0 até o anterior ao índice 2)
print(palavra[2:]) # INÃ (Pega do 2 até o final)
print(palavra[::-1]) # ÃNIAK (Inverte a String inteira)

#Boas maneiras de escrita de string (f-strings)
frase = f"Oi, meu nome é {nome} {sobrenome}, é um prazer imenso conhece-lo"
print(frase)

#Formatações das strings
print("kainã".upper()) #Tudo maiusculo
print("KAINÃ".lower()) #Tudo minusculo
print("    kaInã    ".strip()) #Remove espaços do começo e fim
texto = "Kainã é programador " 
print(texto)
print(texto.replace("programador","garoto de programa")) #Troca um texto pelo outro
print("k,a,i,n,ã".split(",")) # Corta o texto e tranforma em lista
print("-".join(["K", "a", "i", "n", "ã"])) # Inverso do split
print(nome.find("K")) #Localiza o índice da esqueda para a direita

print("Ele disse \"Olá!\" para mim.") # Diz que as "" fazem parte string (\")
print("Ele disse: \n - Olá, Kainã.") # Pula uma linha (Enter)
print("Espaçamento grande, \t Tab") # Tab

#Imutabilidade (Não é possível alterar uma letra específica em uma variavel string... 
#...mas podemos criar outra variavel alterando a variavel desejada)
nome_novo = nome[:4] + "an"
print(nome_novo)


#Busca de palavras
mensagem = "Bem vindo ao sistema, Kainã!"

print("Kainã" in mensagem) #true
print("Geovanna" in mensagem) #false


#len() para contar quantos caracteres uma string possui
nome = "Kainã"
frase = "Kainã está aprendendo"
print(len(nome))
print(len(frase))


#.count() conta quantas vezes uma certa string aparece

texto = "paralelepipedo"
texto2 = "pneumoultramicroscopicossilicovulcanoconiotico"

print(texto.count("e"))
print(texto2.count("o"))


#.startswitch e endswitch | Verificando o começo e fim de uma string

arquivo = 'documento.pdf'
site = 'https://google.com'

print(arquivo.endswith('.pdf'))
print(site.startswith('https'))