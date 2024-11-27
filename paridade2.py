#funçao principal
def main():
    num = int(input("digite um numero:"))
    verificaçao(num)

def veificaçao(num):
    if num % 2 == 0:
        print("\no numero e par!")
    else:
        print("\no numero e impar")
main()
