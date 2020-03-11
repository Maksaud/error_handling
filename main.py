from food import *
orders = []
user_input = ''
count = 0
amount_of_orders = int(input('How many times do you want to order '))
while count < amount_of_orders:

    user_input = input("what would you like to order ")
    count += 1
    user_input.capitalize()
    append_order(user_input, orders)
    print(orders)
    write_order('order.txt', user_input, count)

print('Enjoy, your meal')