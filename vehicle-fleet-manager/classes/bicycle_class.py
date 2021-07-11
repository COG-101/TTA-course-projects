from classes.passenger_vehicle_class import PassengerVehicle

class Bicycle(PassengerVehicle):

    vehicle_type = 'bicycle'
    
    def __init__(self, id, hire_date, return_date, max_num_of_passengers, classification):
        super().__init__(id, hire_date, return_date, max_num_of_passengers)
        self.classification = classification
        list_of_classifications = ['road', 'mountain', 'folding', 'electric']
        #Validating classification:
        if classification not in list_of_classifications:
            raise ValueError('Bicycle classification not valid')