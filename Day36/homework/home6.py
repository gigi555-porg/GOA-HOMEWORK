#     7) მომხმარებელს შეეკითხეთ რიცხვი შემდეგ შექმენით ფუნქცია რომელსაც ექნება პარამეტრი რომელსაც არგუმენტად გადაეცემა მომხლარებლის შემოტანილი რიცხვი შემდეგ კი დაბეჭდავს ეს რიცხვი ლუწია თუ კენტი



x = int(input("enter ur number:"))



def even_or_add(num) :
    if num % 2 == 0 :
        print("rezult: " , + str(num) + "Evenn") 
    else:
        print("rezult: " , + str(num) + "Odd")


even_or_add(x)


