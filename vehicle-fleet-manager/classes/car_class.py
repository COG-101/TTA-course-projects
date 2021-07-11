from classes.passenger_vehicle_class import PassengerVehicle

class Car(PassengerVehicle):

    vehicle_type = 'car'
    
    def __init__(self, id, hire_date, return_date, max_num_of_passengers, num_of_doors):
        super().__init__(id, hire_date, return_date, max_num_of_passengers)
        self.num_of_doors = num_of_doors