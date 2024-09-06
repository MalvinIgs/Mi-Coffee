print("Welcome to the Mi Coffee")
print("What would you like to try?")
print("We have some several menu")
print(" 1. Caramel latte \t [ 20.000 ] \n 2. Vanilla latte \t [ 25.000 ] \n 3. Cappucino \t \t [ 20.000 ] \n 4. Americano \t \t [ 20.000 ] \n 5. Caramel machiato \t [ 25.000 ]")
menu = ["Caramel latte", "Vanilla latte", "Cappucino", "Americano", "Caramel machiato" ]
cl  = 20000
c  = 20000
a  = 20000
vl = 25000
clo = 25000
nama = input("Put your order here : ")
jumlah = int(input("How much is your order : "))
if nama == "Caramel latte":
    harga = jumlah * cl 
    print(f"Okay , so we got all your order right here : \n {jumlah} cup of {nama}")
    print(f"The total amount of your order is {harga}")
elif nama == "Vanilla latte":
    harga = jumlah * vl 
    print(f"Okay , so we got all your order right here : \n {jumlah} cup of {nama}")
    print(f"The total amount of your order is {harga}")
elif nama == "Cappucino":
    harga = jumlah * c 
    print(f"Okay , so we got all your order right here : \n {jumlah} cup of {nama}")
    print(f"The total amount of your order is {harga}")
elif nama == "Americano":
    harga = jumlah * a 
    print(f"Okay , so we got all your order right here : \n {jumlah} cup of {nama}")
    print(f"The total amount of your order is {harga}")
elif nama == "Caramel machiato":
    harga = jumlah * clo
    print(f"Okay , so we got all your order right here : \n {jumlah} cup of {nama}")
    print(f"The total amount of your order is Rp.{harga}")
else:
    print("Im sorry, your order is not on the list maybe you should check other restaurant and comeback later ! ")   

print("But before you pay the total price of your order,\nWe would like to offer you to answer our question through the discount \nThat we have for 79th Indonesian Indepedence Event \nIf you can answer the question you will get 15% discount of the total price")


dsoal = [
    {
    "soal" : "Who is the president of Indonesia (Full name) ?",
    "key" : "Joko Widodo"
    },
    {
    "soal" : "The root of 400 ?",
    "key" : "20"
    },
    {
    "soal" : "The planet closest to the sun is ?",
    "key" : "Mercury"
    },
    {
    "soal" : "The multiple of 2 by 50 gives ?",
    "key" : "100"
    },
]

def quiz(soaldiskon):
    diskon = 0
    info = 0
    for soal in soaldiskon:
        print(soal["soal"])
        answer = input("Put your answer here : ")
        if answer == soal["key"]:
            diskon = diskon + (harga * 0.125)
            info = info + 12.5
            print(f"Congratulation !!!\nYour answer is true !!\nYou got {info}% discount of your total order")
        else:
            print(f"Wrong !, the correct answer is {soal['key']}")
    print(f"The total amount of your order is Rp.{harga - diskon}")

quiz(dsoal)   