#     7) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს შემდეგ კი დაბეჭდავს ეს რიცხვი ლუწია თუ კენტი



def num () :
    num = int(input("enter your number"))
    if num % 2 == 0 :
        print(num,"even")
    else:
        print("odd")

num()