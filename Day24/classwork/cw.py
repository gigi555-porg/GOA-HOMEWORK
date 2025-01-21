#    1) გააკეთეთ სარეგისტრაციო, მომხმარებელს შემოატანიეთ სახელი და პაროლი, რეგისტრაციის შემდეგ მოხმარებელი უნდა შევიდეს ექაუნთზე, შეეკითხეთ სახელი და პაროლი მომხარებელს რათა შევიდეს ექაუნთზე სანამ მომხმარებელი არ შეიტანს იმ ინფორმაციას რაც შეიყვანა რეგისტრაციის დროს მანამ დაიბეჭდოს რომ შეტანილი ინფორმაცია არასწორია და შეეკითხოს თავიდან, ხოლო თუ მომხმარებელმა ყველაფერი სწორად შეიყვანა დაიბეჭდოს welcome


re_name= input("Enter Your Name")
re_password= input("Enter your password")





print("Login: ") 


log_name = input("Enter Your Namme: ")
log_password = input("Enter Your Password: ") 

while log_name != re_name or log_password != re_password : 
    print("inccorect password, or name Please Try Again: ")
    log_name = input("Please Enter correct Name: ")
    log_password = input("Please Enter The correct Password: ")


print("Welcome")