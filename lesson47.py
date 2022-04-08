user = input("введите число: ") # 315830
count = 0
for element in user:
    if element == "1":
        count += 2
    elif element == "2":
        count += 5
    elif element == "3":
        count += 5
    elif element == "4":
        count += 4
    elif element == "5":
        count += 5
    elif element == "6":
        count += 6
    elif element == "7":
        count += 3
    elif element == "8":
        count += 7
    elif element == "9":
        count += 6
    elif element == "0":
        count += 6
print(count, "leds")