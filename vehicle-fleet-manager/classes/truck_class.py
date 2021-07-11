from classes.transporter_vehicle_class import TransporterVehicle

class Truck(TransporterVehicle):

    vehicle_type = 'truck'
    
    def __init__(self, id, hire_date, return_date, load_capacity, num_of_axles):
        super().__init__(id, hire_date, return_date, load_capacity)
        self.num_of_axles = num_of_axles