print("OPERADORES ARITMETICOS")
print (10 + 4)
print (10-50)
print (10*110)
print (10/5)
print (10//3) # arredonda o resultado para baixo
print (10 % 2)  # retorna o resto da divisão, se sobrar restorna 1 se nao sobrar retorna 0
print (5 ** 2)

print("\n")

print("OPERADORES RELACIONAIS")
print (6 == 5)
print (6 != 5)
print (6 > 5)

print("\n")

print("OPERADORES LÓGICOS")
print (6 == 6 and 6 == 7)
print (6 == 8 or 6 > 5)
print (not 6 == 6)

print("\n")

print("OPERADORES DE ATRIBUIÇÃO  (  =, +=, -=, *=, /=, //=, %=.  )")

contador = 0
caminho = __file__
with open(caminho, 'r') as arquivo:
    linhas = arquivo.readlines()
for linha in linhas:
    if 'print' in linha:
        contador += 1 #Atribução
    else:
        pass
print ("Numero de print: ", contador)

print("\n")

print("OPERADORES DE IDENTIDADE E ASSOCIAÇÃO")

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print (a is c) # True (é o mesmo objeto)
print (a is b) # False (possui valores iguais mas não são o mesmo objeto)
print (a == b) # True (ocorre a comparação dos valores)
print (a is not b) #True (auto explicativo)

# Ordem de Execução
# A ordem geral, da maior para a menor prioridade, é: 
# expoente (**), 
# multiplicação/divisão (*, /, //, %), 
# adição/subtração (+, -), e 
# comparações (<, <=, >, >=, ==, !=).

print("\n")
# Verificadores

print("VERIFICADORES TRUE E FALSE")

print("123".isdigit()) # É formado só por números? true
print("Kaina123".isalpha()) # É formado só por letras? false
print("Kaina".startswith("K")) # Começa com esse texto? false
print("Kaina".endswith("a")) # Termina com esse texto? false

print("VERIFICADOR DE ALPHANUMERICOS")

print("Kaina314".isalnum())  # True
print("Kainã".isalnum())  # True
print("Kaina 3".isalnum())   # False (espaço não é alfanumérico)
print("Kaina@123".isalnum())   # False (símbolo @ não é alfanumérico)
print("".isalnum())           # False (string vazia)

print("\n")

print("Strings são iteráveis") # É possível desmembrar strings

for letra in "Kainã":
    print(letra) 