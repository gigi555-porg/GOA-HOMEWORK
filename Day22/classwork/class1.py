#2) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი ერთიდან ამ რიცხვამდე დაბეჭდეთ მხოლოდ ლუწი რიცხვების ჯამი, გამოიყენეთ for loop




ggg=int(input("Enter Your Number"))

mmm=0


for i in range(ggg):
    if i % 2 == 0 : 
        mmm = mmm + i 

print(mmm)