from classes.vehicle_class import Vehicle

class TransporterVehicle(Vehicle):

    vehicle_type = 'transporter vehicle'
    
    def __init__(self, id, hire_date, return_date, load_capacity):
        super().__init__(id, hire_date, return_date)
        self.load_capacity = load_capacity