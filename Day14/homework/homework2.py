#2) გამოიყენეთ or ოპერატორი, რათა შეამოწმოთ, თუ მოცემული ციფრები არიან 10-ზე მეტი ან 50-ზე ნაკლები.

num1 = int(input("Enter Your Number"))

if num1 >= 10 or num1 <= 50 :
    print("es cifri aris 10 meti da 50 naklebi ") 

elif num1 < 10 :
    print("es aris 10 ze naklebi")

elif num1 > 50 :
    print("es aris 50 ze meti")