# user_input = ''
# count = 0
# amount_of_orders = int(input('How many times do you want to order'))
# while count <= amount_of_orders:
#
#     user_input = input("what would you like to order")
#     count += 1

def append_order(user_input, orders):
    orders.append(user_input)

def write_order(file, user_input, count):
    try:
        with open(file, 'a') as file_to_write:
            file_to_write.write(str(count) + '-' + user_input + '\n')

    except FileNotFoundError as err:
        print('File not found')
        print(err)

    finally:
        print('mhm')
