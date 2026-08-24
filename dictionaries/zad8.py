CODES = { "V":"S001",
          "VI": "S002",
          "VII": "S001",
          "VIII": "S005",
          "IX":"S005",
          "X":"S009",
          "XI":"S007" }

unique_numbers = set()

for number, code in CODES.items():
    unique_numbers.add(code)

print(unique_numbers)
