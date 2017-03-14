print "Welcome to the menu generator"

menu_file = open ("menu.txt", "w+")
menu = {}

while True:
    dish = raw_input ("Enter name of dish: ")
    price = raw_input ("Enter price of dish: ")
    print dish, price

    menu [dish] = price

    end = raw_input ("Would you like to add another dish? (y/n): ")
    if end == "n":
        break

print "Gesamte Speisekarte:"
menu_file.write("Gesamte Speisekarte:" + "\n")
count = 1

for i in menu:
    print count, i, "EUR", menu[i]
    menu_file.write(str(count) + " " + i + " EUR " + menu[i] + "\n")
    count = count + 1



