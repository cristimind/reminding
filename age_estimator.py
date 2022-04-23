current_year = 2022
born_age  = int(input('Anul nasterii --->') )

if born_age < 1900 or born_age > 2022:
    print('invalid answer')
else:
    age = current_year - born_age
    print ( age , 'years old', end=' ' ,)
    if age <= 3:
        print ('baby')
    elif age <= 9:
        print('kid')
    elif age <= 18:
        print('teen')
    elif age <= 50:
        print ('adult')
    else:
        print('old')


