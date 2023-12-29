# tipos de saídas de dados


n1 = int(input("DIGITE UM NÚMERO: "))
n2 = int(input("DIGITE OUTRO NÚMERO: "))

soma = n1 + n2


# print("{}".format(n1) , "+" ,"{}".format(n2) , "= {}".format(soma))

#ou de uma maneira mais fácil

print("{} + {} = {}".format(n1,n2,soma))








# int = número inteiro
# float = número flutuante ou com casas decimais
#bool = valores boleanos, true or false
#str  = string/caracteres 

# format visto no documento anterios é um método de interpolação passando um valor vazio para as "{}" e dizendo que essas chaves tera o valor de .format(variavél desejada)

# em javascrip
# var msg = `ola`
# msg = `${mensagem},Eduardo`

# em python seria 
# msg = `olá`
# print("{}, Eduardo".format(msg))