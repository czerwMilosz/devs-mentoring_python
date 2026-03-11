import requests
from pydantic import BaseModel, Field, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    bmi_api_key: str
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding = "utf-8")

def get_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input")
class UserMetrics(BaseModel):
    weight: float = Field(gt=0, le=300, description="Weight of the user")
    height: float = Field(gt=2.5, description="Height of the user")



def get_user_metrics() -> UserMetrics:
    while True:
        try:
            weight = get_float("Please enter your weight [kg]: ")
            height = get_float("Please enter your height [cm]: ")

            return UserMetrics(weight = weight, height=height)
        except ValidationError as e:
            print(e)



def get_bmi_from_api(weight: float, height: float):
    url = "https://api.apiverve.com/v1/bmicalculator"
    settings = Settings()
    api_key = settings.bmi_api_key
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
    metrics = get_user_metrics()
    api_data = get_bmi_from_api(metrics.weight, metrics.height)
    if api_data is None:
        print("Could not retrieve BMI data.")
        return None
    bmi = api_data["data"]["bmi"]
    category = api_data["data"]["category"]
    range_ideal_weight = api_data["data"]["idealWeightRange"]
    min_ideal_weight = range_ideal_weight["min"]
    max_ideal_weight = range_ideal_weight["max"]
    print(f"BMI: {bmi}"
          f"\nCategory: {category}"
          f"\nMinimum ideal weight: {min_ideal_weight}"
          f"\nMaximum ideal weight: {max_ideal_weight}")

if __name__ == "__main__":
    main()