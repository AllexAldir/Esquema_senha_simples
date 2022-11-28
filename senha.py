
from colorama import Fore

print(Fore.LIGHTMAGENTA_EX + """
Digite seu usuario e sua senha:
Saiba que você somente tem 3 tentativas,
para ter acesso.

\n
""" + Fore.GREEN)



senha1 = (1)
# print(senha)

w = 0

# def valid_senha2 (senha):
#             try:
#                 senha = int(senha)

#                 if senha <0:
#                     x = 'Número menor que "0" tente novamente...'
#                     return x

#                 else:
#                     x = 'ok'
#                     return x
#             except:
#                 x = "Não foi possivel identificar esse número..."
#                 return x

def valid_senha (senha):

        if senha != senha1:
            x = 'Opssss.... Tente novamente'
            return x

        else:
            x =  "OK"
            return x


usuario = input("Digite aqui o usuário: ")

print("\n")

while w <3:

    senha = int(input("Digite a senha aqui: "))

    k = valid_senha(senha)

    if k == 'OK':
        print("Você passou")
        w = 3

    else:
        print("opss Tente novamente... senha incorreta")
        w = w + 1
        print(f"Restam: {3-w} tentativas")
