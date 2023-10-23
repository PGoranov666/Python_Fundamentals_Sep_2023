def odd_even_sums(some_number: str):
    sum_of_odds = 0
    sum_of_evens = 0
    for digit in some_number:
        if int(digit) % 2 == 0:
            sum_of_evens += int(digit)
        else:
            sum_of_odds += int(digit)
    return sum_of_odds, sum_of_evens


number = input()
sum_of_odds, sum_of_evens = odd_even_sums(number)
print(f"Odd sum = {sum_of_odds}, Even sum = {sum_of_evens}")
