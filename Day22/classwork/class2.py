#3) მომხმარებელს შემოატანინეთ რიცხვი, შემდეგ კი დაბეჭდეთ ერთიდან ამ რიცხვამდე მხოლოდ ლუწი რიცხვების ჯამი ცალკე და მხოლოდ კენტი რიცვხების ჯამი ცალკე, გამოიყენეთ for loop




fff=int(input("Enter Your Number"))


sss=0

mmm=0

for i in range(fff):
    if i % 2 == 0:
        sss = sss + i

else:
    print(mmm)
