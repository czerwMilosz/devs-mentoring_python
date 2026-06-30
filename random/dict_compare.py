import random
import time
import pandas as pd
N = 1_000_000

users = {
    i: {
        "name": f"user_{i}",
        "score": random.randint(0, 100)
    }
    for i in range(N)
}
df = pd.DataFrame({
    "id": range(N),
    "name": [f"user_{i}" for i in range(N)],
    "score": [random.randint(0, 100) for _ in range(N)]
})

lookup_ids = [random.randint(0, N - 1) for _ in range(100_000)]

start = time.perf_counter()

total = 0

for uid in lookup_ids:
    total += users[uid]["score"]

end = time.perf_counter()

print("DICT TIME:", end - start)
print(total)


start = time.perf_counter()
df = df.set_index("id")
total = 0

for uid in lookup_ids:
    row = df.loc[uid]
    total += row["score"]

end = time.perf_counter()

print("PD TIME:", end - start)
print(total)


# ---------------------------------------------

# N = 10_000_000
#
# data = {i: i for i in range(N)}
#
# start = time.perf_counter()
#
# for k in data:
#     data[k] = data[k] * 2 + 5
#
# end = time.perf_counter()
#
# print("DICT TIME:", end - start)
#
# df = pd.DataFrame({
#     "x": range(N)
# })
#
# start = time.perf_counter()
#
# df["x"] = df["x"] * 2 + 5
#
# end = time.perf_counter()
#
# print("PANDAS TIME:", end - start)

# ---------------------------------------------
# N = 5_000_000
# df = pd.DataFrame({
#     "country": [random.choice(["PL", "DE", "FR", "US"]) for _ in range(N)],
#     "sales": [random.randint(1, 100) for _ in range(N)]
# })
#
# start = time.perf_counter()
#
# result = df.groupby("country")["sales"].sum()
#
# end = time.perf_counter()
#
# print(result)
# print("PANDAS:", end - start)
#
#
#
# rows = [
#     {
#         "country": random.choice(["PL", "DE", "FR", "US"]),
#         "sales": random.randint(1, 100)
#     }
#     for _ in range(N)
# ]
#
# start = time.perf_counter()
#
# result = {}
#
# for row in rows:
#     c = row["country"]
#
#     if c not in result:
#         result[c] = 0
#
#     result[c] += row["sales"]
#
# end = time.perf_counter()
#
# print(result)
# print("DICT:", end - start)