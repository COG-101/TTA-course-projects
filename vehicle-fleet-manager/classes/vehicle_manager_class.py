from classes.vehicle_class import Vehicle
from classes.transporter_vehicle_class import TransporterVehicle
from classes.passenger_vehicle_class import PassengerVehicle
from classes.truck_class import Truck
from classes.car_class import Car
from classes.bicycle_class import Bicycle
from datetime import datetime

class VehicleManager():

    def __init__(self):
        pass

    def hire_vehicle(id, date):
        #Input: int=id, str=date (YYYY/MM/DD)
        #Output: New hire date attribute assigned
        #Parses string input into datetime format:
        datetime_object = datetime.strptime(date, '%Y/%m/%d').date() 
        count = 0
        on_hire = False
        hired_vehicle_id = 0

        #Iterating through vehicles to find ID input:
        for vehicle in Vehicle.all_vehicles: 
            if vehicle.id == id and vehicle.hire_date != None:
                on_hire = True
                hired_vehicle_id = vehicle.id
                count += 1
                break
            elif vehicle.id == id and vehicle.hire_date == None:
                vehicle.hire_date = datetime_object
                count += 1
                hired_vehicle_id = vehicle.id

        #handling results:
        if count == 0:
            raise ValueError(f'Vehicle (ID: {id}) not recognised. Please check ID.')
        elif count != 0 and on_hire == True:
            print(f'Vehicle (ID: {hired_vehicle_id}) is currently on hire!')
        else:
            print(f'Vehicle (ID: {hired_vehicle_id}) Hired!')


    def return_vehicle(id, date):
        #Input: int=id, str=date (YYYY/MM/DD)
        #Output: return date = date input, hire date = None
        datetime_object = datetime.strptime(date, '%Y/%m/%d').date()
        count = 0

        for vehicle in Vehicle.all_vehicles:
            if vehicle.id == id and vehicle.hire_date == None:
                count += 1
                print(f'Vehicle (ID: {str(vehicle.id)}) cannot be returned as it is not on hire!')
            elif vehicle.id == id:
                vehicle.hire_date = None
                vehicle.return_date = datetime_object
                count += 1
                print(f'Vehicle (ID: {str(vehicle.id)}) has been returned!')
        if count == 0:
            raise ValueError(f'Vehicle (ID: {id}) not recognised. Please check ID.')

    def available_trucks():
        #Prints a list of trucks identified by ID
        available_trucks = []
        for vehicle in Vehicle.all_vehicles:
            if vehicle.vehicle_type == 'truck' and vehicle.hire_date == None :
                available_trucks.append(vehicle)
        print('All Available Trucks:')
        for trucks in available_trucks:
            print(f'ID: {str(trucks.id)}')

    def available_cars():
        #Prints a list of cars identified by ID        
        available_cars = []
        for vehicle in Vehicle.all_vehicles:
            if vehicle.vehicle_type == 'car' and vehicle.hire_date == None :
                available_cars.append(vehicle)
        print('All Available Cars:')
        for cars in available_cars:
            print(f'ID: {str(cars.id)}')

    def available_bicycles():
        #Prints a list of bicycles identified by ID
        available_bicycles = []
        for vehicle in Vehicle.all_vehicles:
            if vehicle.vehicle_type == 'bicycle' and vehicle.hire_date == None :
                available_bicycles.append(vehicle)
        print('All Available Bicycles:')
        for bicycles in available_bicycles:
            print(f'ID: {str(bicycles.id)}')