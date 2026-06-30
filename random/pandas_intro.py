users = [
    {"name": "Tomasz", "age": 25},
    {"name": "Adam", "age": 45},
    {"name": "Bartek", "age": 35}
]
#wiecej niz 32 lata, zwrocic liste uzytkownikow
new_users = []
for user in users:
    if user["age"] > 32:
        new_users.append(user)

print(new_users)

import etl_pipeline as pd
df = pd.DataFrame(users)
print(df["age"]) # seria
print(df[df["age"] > 32]["age"].mean())

df2 = pd.DataFrame({"city": ["Warszawa", "Krakow", "Warszawa", "Krakow", "Gdansk"],
                    "sales": [100, 200, 150, 300, 400],
                    "products": ["laptop", "telefon", "laptop", "telefon", "laptop"]})
print(df2.head(2)) # limit
print(df2.groupby("city")["sales"].sum())
print(df2.groupby("city").size()) #taki count jakby
print(df2.groupby("city").value_counts())
print(df2.groupby("city")["sales"].agg(["sum", "mean", "max"]))
print(df2[df2["sales"] > 200].groupby(["city", "products"])["sales"].agg(["sum", "mean", "max"]).sort_values(["city", "products"], ascending=False))

weather = pd.read_csv("weather.csv")
print(weather.head(10))
print(weather["date"].dtype)
weather["date"] = pd.to_datetime(weather["date"])
print(weather["date"].dtype)
print(weather.head(10))
print(weather["date"].dt.year)
weather["year"] = weather["date"].dt.year
print(weather.groupby("year")["temp_max"].mean())

weather = weather.set_index("date")
print(weather)
print(weather.loc["2012-01-01": "2012-01-15"].groupby("weather")["wind"].mean())







