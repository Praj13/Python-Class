from importing import func2,func,check_prime
number = int(input("Enter a number to check prime"))
value_of_check_prime = check_prime(number)
if value_of_check_prime:
    func2(number)
else:
    func(number)




