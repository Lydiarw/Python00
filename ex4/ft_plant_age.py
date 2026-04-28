def ft_plant_age():
    user_input = input('Enter plant age in days: ')
    if int(user_input) > 60:
        print('Plant is ready to harvest!')
    else:
        print('Plant needs more time to grow.')
