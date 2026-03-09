from decimal import Decimal

BMI_CATEGORIES = {
    "Niedowaga": (0, 18.5),
    "Waga normalna": (18.5, 24),
    "Lekka nadwaga": (24, 26.5),
    "Nadwaga": (26.5, 30),
    "Otyłość I stopnia": (30, 35),
    "Otyłość II stopnia": (35, 40),
    "Otyłość III stopnia": (40, float("inf"))
}

def get_user_data() -> dict:
    while True:
        try:
            height = float(input("Height [m]: "))
            weight = float(input("Weight [kg]: "))

            if height <= 0 or weight <= 0:
                print("Values must be greater than 0.")
                continue
            elif height > 2.5 or weight > 250:
                print("Please enter values in meters and kilograms.")
                continue
            else:
                return {"height": height, "weight": weight}
        except ValueError:
            print("Invalid input")

def calculate_bmi(body_data:dict) -> float:
    height = body_data["height"]
    weight = body_data["weight"]
    return round(Decimal(weight) / Decimal(height ** 2),2)


def classify_bmi_category(bmi):
    for category, (min_bmi, max_bmi) in BMI_CATEGORIES.items():
        if min_bmi <= bmi < max_bmi:
            return category

def main():
    body_data = get_user_data()
    bmi = calculate_bmi(body_data)
    category = classify_bmi_category(bmi)
    print(f"BMI: {bmi}, \nKategoria: {category}")

if __name__ == "__main__":
    main()