class Vehicle:

    all_vehicles = []

    def __init__(self, id, hire_date, return_date):
        self.id = id
        self.hire_date = hire_date
        self.return_date = return_date
        #Every instance is auto-added to the list of all vehicles:
        self.all_vehicles.append(self) 

    def print_all_vehicles(list_of_vehicles):
        #Prints all vehicles identified by ID number:
        print('All Vehicles in System:')
        for vehicles in list_of_vehicles:
            print(f'ID: {str(vehicles.id)}')
