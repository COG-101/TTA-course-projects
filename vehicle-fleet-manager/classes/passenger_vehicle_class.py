from classes.vehicle_class import Vehicle

class PassengerVehicle(Vehicle):

    vehicle_type = 'passenger vehicle'
    
    def __init__(self, id, hire_date, return_date, max_num_of_passengers):
        super().__init__(id, hire_date, return_date)
        self.max_num_of_passengers = max_num_of_passengers