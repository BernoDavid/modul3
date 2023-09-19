for k in range(10):
    text = input("Skriv in något: ")
    print(text)

for i in range(1, 11):
    print(i)

y = int(input("Ange ett heltal y: "))
for i in range(1, y + 1):
    print(i)

for i in range(1, 11):
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)