def convert_int_to_str(num_1: int, num2: int):
    converted_int = str(num_1) + str(num2)
    return f'String: {converted_int}'
a = 5
b = 6
print(convert_int_to_str(a, b))

def convert_int_to_str_v2(num_1: int, num2: int):
    return f'{num_1}{num2}'

print(convert_int_to_str_v2(a, b))