def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit)**num_digits for digit in num_str)
    return sum_of_powers == num
number_to_check = 153
result = is_armstrong(number_to_check)
if result:
    print(f"{number_to_check} is an Armstrong number.")
else:
    print(f"{number_to_check} is not an Armstrong number.")