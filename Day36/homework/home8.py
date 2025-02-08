#9) მომხმარებელს შეეკითხეთ რიცხვი შემდეგ შექმენით ფუნქცია რომელსაც ექნება პარამეტრი რომელსაც არგუმენტად გადაეცემა მომხლარებლის შემოტანილი რიცხვი შემდეგ კი თუ 18 ზე უთხრას რომ სრულწლოვანია თუარადა არარის


x = int(input("enter ur age")) 

def age (num) :
    if num >= 18 :
        print("asaki " , + str(num) + "srulwlovna")
    else:
        print("asaki ", + str(num) + "ar xar srulwlovani")

age(x)