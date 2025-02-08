#5)შეამოწმეთ, თუ ერთ-ერთი ციფრი უფრო დიდია 10-ზე ან მეორე ციფრი ნაკლებია 50-ზე.

num = int(input("Enter Your Num"))

if num > 10 and num < 50 :
    print("this number is > 10 < 50")

elif num < 10 or num > 50 :
    print("this  number not >10 and <50 ")