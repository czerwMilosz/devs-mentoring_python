def bmi_calc(weight: float, height: float, precision: int = 2) -> float:
    """Calculate the BMI based on a weight and height.

    Args:
        weight (float): Weight in kg
        height (float): Height in cm
        precision (int, optional): Number of decimal places to round to. Defaults to 2.
    Examples:
        >>> bmi_calc(80, 1.8)
        24.69
        """
    bmi = round((weight / height ** 2),precision)
    return bmi

user_weight = float(input('Podaj swoja wage [kg]: '))
user_height = float(input('Podaj swoj wzrost [m]: '))

print(f"Twoje BMI: {bmi_calc(user_weight, user_height)}")



'''
/usr/local/bin/python3.11 /Applications/PyCharm.app/Contents/plugins/python-ce/helpers/pydev/pydevconsole.py --mode=client --host=127.0.0.1 --port=64464 
import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['/Users/mc/devs-mentoring/Python'])
PyDev console: starting.
Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
0.2 + 0.1
0.30000000000000004
0.2 + 0.1 == 0.3
False
import math
math.isclose(0.2 + 0.1, 0.3)
True
from decimal import Decimal
Decimal("0.2") + Decimal("0.1") == Decimal("0.3")
True
Decimal("0.2") + Decimal("0.1")
Decimal('0.3')

'''