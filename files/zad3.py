with open("litwo.txt","r", encoding="utf-8") as file:
   for i, line in enumerate(file, start=1):
       if i % 2 == 0:
           print(line.strip())

