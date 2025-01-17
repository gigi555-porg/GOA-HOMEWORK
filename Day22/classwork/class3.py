
#4) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი ერთიდან ამ რიცხვამდე დაბეჭდეთ მხოლოდ 5 ის ჯერადი რიცხვების ჯამი ცალკე და მხოლოდ 3ის ჯერადი რიცხვების ჯამი ცალკე, გამოიყენეთ while loop



fff=int(input("Enter Your Number"))



sum1=0

sum2=0

i=0  


while i < fff:
    if i % 5 == 0 :
        sum1 = sum1 + i 
    elif i % 3 == 0 :
        sum2 = sum2 + i
    i = i + 1 

print(sum1)
print(sum2)