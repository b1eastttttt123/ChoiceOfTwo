user_number = int(input())

one_number = user_number // 1000
two_number = (user_number // 100) % 10
three_number = (user_number // 10) % 10
four_number = user_number % 10

one_and_four = one_number + four_number
two_and_three = two_number - three_number

if one_and_four == two_and_three:
    print('ДА')
else:
    print('НЕТ')
