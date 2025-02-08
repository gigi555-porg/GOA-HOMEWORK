#5) გააკეთეთ Find Minimum და გამოიყენეთ for loop. მიზანი: სიაში უნდა იპოვოთ მინიმალური ინტეჯერი მაგალითად: [1, 546, 456 ,123] => [1]


num = [1, 546, 456, 123,] 


mux_num = [0]

for i in num:
     if i > max_num:
        max_num = i
print(max_num)