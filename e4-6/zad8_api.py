import requests
from dotenv import load_dotenv
import os
load_dotenv()


def get_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input")

def get_user_weight() -> float:
    while True:
        weight = get_float("Please enter your weight [kg]: ")
        if weight <= 0:
            print("Weight must be greater than 0")
        elif weight > 300:
            print("Please enter values in kilograms.")
        else:
            return weight

def get_user_height() -> float:
    while True:
        height = get_float("Please enter your height [cm]: ")
        if height <= 0:
            print("Height must be greater than 0")
        elif height < 2.5:
            print("Please enter values in cm.")
        else:
            return height


def get_bmi_from_api(weight: float, height: float):
    url = "https://api.apiverve.com/v1/bmicalculator"
    api_key = os.getenv("BMI_API_KEY")
    if not api_key:
        raise ValueError("BMI_API_KEY not found")

    headers = {'x-api-key': api_key,
               "Content-Type": "application/json"}
    params = {'weight': weight, 
              'height': height, 
              "unit": "metric"}

    try:
        response = requests.get(url, params=params, headers=headers,timeout=5)
        response.raise_for_status()
        data = response.json()
        if data["status"] != "ok":
            print("Invalid API response")
            return None

        return data

    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        return None


def main():
    weight = get_user_weight()
    height = get_user_height()
    api_data = get_bmi_from_api(weight, height)
    if api_data is None:
        print("Could not retrieve BMI data.")
        return None
    bmi = api_data["data"]["bmi"]
    category = api_data["data"]["category"]
    min_ideal_weight = api_data["data"]["idealWeightRange"]["min"]
    max_ideal_weight = api_data["data"]["idealWeightRange"]["max"]
    print(f"BMI: {bmi}"
          f"\nCategory: {category}"
          f"\nMinimum ideal weight: {min_ideal_weight}"
          f"\nMaximum ideal weight: {max_ideal_weight}")

if __name__ == "__main__":
    main()