def ft_count_harvest_recursive():
    def day_recursive(num):
        if (num > 0):
            day_recursive(num - 1)
            print('Day', num)
    user_input = input('Days until harvest: ')
    day_recursive(int(user_input))
    print('Harvest time!')
