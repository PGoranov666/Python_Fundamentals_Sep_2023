def calcilate_the_fractoral(number):
    for current_number in range(1, number):
        number *= current_number
    return number


first_number = int(input())
second_number = int(input())
first_number_fractorial = calcilate_the_fractoral(first_number)
second_number_fractoral = calcilate_the_fractoral(second_number)
result = first_number_fractorial / second_number_fractoral
print(f"{result:.2f}")
