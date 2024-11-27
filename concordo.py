def main():
    resposta = input("voce concorda? ").lower()
    concordo(resposta)
def concordo(resposta):
    if resposta == "sim" or resposta == "s" or resposta == "si":
        print("eu concordo")
    elif resposta == "n" or resposta == "no" or resposta == "nao":
        print("eu nao concordo")

main()
