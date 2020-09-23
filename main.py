giriş = """
(1) topla
(2) çıkar
(3) çarp
(4) böl
(5) karesini hesapla
(6) karekök hesapla
"""

print(giriş)
def sum(number1,number2):
    suum=number1+number2
    return suum

def ext(number1,number2):
    exxt=number1-number2
    return exxt
def mptl(number1,number2):
    mpptl=number1*number2
    return mpptl
def dvs(number1,number2):
     dvvs=number1/number2
     return dvvs

key=1
while key ==1:
    question=input("Yapmak istediğiniz işlemin numarasını girin:(cıkmak için=q): ")
    if question=="q":
        print("Cıkılıyor...")
        key=0
    elif question=="1":
        number1=int(input("Toplama için ilk sayıyı girin: "))
        number2=int(input("Toplama için ikinci sayıyı girin: "))
        print("Toplama işleminin sonucu: ",sum(number1,number2))
    elif question=="2":
        number1 = int(input("Cıkarma için ilk sayıyı girin: "))
        number2 = int(input("Cıkarma için ikinci sayıyı girin: "))
        print("Cıkarma işleminin sonucu: ",ext(number1, number2))
    elif question=="3":
        number1 = int(input("Çarpma için ilk sayıyı girin: "))
        number2 = int(input("Çarpma için ikinci sayıyı girin: "))
        print("Çarpma işleminin sonucu: ",mptl(number1, number2))
    elif question=="4":
        number1 = int(input("Bölme için ilk sayıyı girin: "))
        number2 = int(input("Bölme için ikinci sayıyı girin: "))
        print("Bölme işleminin sonucu: ",dvs(number1, number2))