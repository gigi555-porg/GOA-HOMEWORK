#8) გააკეთეთ Sum Of Odd Numbers. მიზანი: შეკრიბეთ ყველა კენტი რიცხვი და შეინახეთ სიაში შემდეგ ეგ სია დაპრინტეთ 10 ჯერ


num = [1,2,3,4,5,6,7,8,9,10,]

sum_of_odd_number = 0

for i in range(len(num)):
    if num[i] % 2 != 0 :
        sum_of_odd_number += num[i] 
    print(sum_of_odd_number)