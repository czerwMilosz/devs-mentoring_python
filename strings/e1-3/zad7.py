def bmi_calc(weight: float, height: float):
    bmi = round((weight / height ** 2),2)
    return f'Twoje BMI: {bmi}'

user_weight = float(input('Podaj swoja wage [kg]: '))
user_height = float(input('Podaj swoj wzrost [m]: '))

print(bmi_calc(user_weight, user_height))
