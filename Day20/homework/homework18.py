#19)შეიყვანეთ რიცხვი და დაბეჭდეთ ყველა რიცხვი, რომელიც არის 3-ზე მეტია, მაგრამ 10-ზე ნაკლები.


a = int(input("num"))  

while a>=3:
    print(a)
    a+=1
    if a>10:
        break