print "Welcome to the Vehicle Manager Program!"
print ""

class Carpool(object):
    def __init__(self, brand, model, actual_kilometers, service_date):
        self.brand = brand
        self.model = model
        self.actual_kilometers = actual_kilometers
        self.service_date = service_date

    def update_km(self, new_km):
        self.actual_kilometers = new_km

    def update_service(self, new_service):
        self.service_date = new_service

    def get_full_details(self):
        return " Brand: " + self.brand + "   Model: " + self.model + "   Kilometers: " + self.actual_kilometers + "   Last service date: " + self.service_date

def carpool_list(poolcars):
    if poolcars == []:
        print "You have not entered any cars to the list."
    else:
        count = 1
        for car in poolcars:
            print count, car.get_full_details()
            count += 1

def add_car(poolcars):
    try:
        brand = raw_input("Add brand of car: ")
        model = raw_input("Enter model of vehicle: ")
        actual_kilometers = raw_input("Enter current kilometers of car: ")
        service_date = raw_input("Enter last service date: ")

        new_car = Carpool(brand = brand, model = model, actual_kilometers = actual_kilometers, service_date = service_date)
        poolcars.append(new_car)
        print "You just added: ", brand, model, actual_kilometers, service_date

        return True

    except ValueError:
        return False

def km_change(poolcars):
    print carpool_list(poolcars)
    sel_id = raw_input("Enter number of car you would like to edit: ")
    print "Your selection is vehicle number " + sel_id + "."
    sel_car = poolcars[int(sel_id)-1]
    new_km = raw_input("Add new value for kilometers: ")
    sel_car.update_km(new_km)

def service_change(poolcars):
    print carpool_list(poolcars)
    sel_id = raw_input("Enter number of car you would like to edit: ")
    print "Your selection is vehicle number " + sel_id + "."
    sel_car = poolcars[int(sel_id)-1]
    new_service = raw_input("Add new service date: ")
    sel_car.update_service(new_service)

def main():
    poolcars = []
    with open ("carpool.txt", "r") as v_file:
        for line in v_file:
            try:
                brand, model, actual_kilometers, service_date = line.split(",")
                new_car = Carpool(brand = brand, model = model, actual_kilometers = actual_kilometers, service_date = service_date)
                poolcars.append(new_car)
            except ValueError:
                continue

    while True:
        print "Please select your choice:"
        print "  a --> to see all vehicles"
        print "  b --> to add a new vehicle"
        print "  c --> to edit kilometers for a vehicle"
        print "  d --> to edit service date for a vehicle"
        print "  e --> to exit the program"

        selection = raw_input("Please enter a,b,c,d or e: ")
        if selection == "a":
            carpool_list(poolcars)
        elif selection == "b":
            add_car(poolcars)
        elif selection == "c":
            km_change(poolcars)
        elif selection == "d":
            service_change(poolcars)
        elif selection == "e":
            print "Good Bye!"
            with open("carpool.txt", "w+") as v_file:
                for i in poolcars:
                    v_file.write("%s,%s,%s,%s\n" % (i.brand, i.model, i.actual_kilometers, i.service_date))
            break
        else:
            print "No valid input, please enter a letter from a to e: "

if __name__ == "__main__":
    main()