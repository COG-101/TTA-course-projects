from datetime import datetime

from classes.vehicle_class import Vehicle
from classes.transporter_vehicle_class import TransporterVehicle
from classes.passenger_vehicle_class import PassengerVehicle
from classes.truck_class import Truck
from classes.car_class import Car
from classes.bicycle_class import Bicycle
from classes.vehicle_manager_class import VehicleManager

 
#Instantiation
truck1 = Truck(100, None, None, 500, 2)
truck2 = Truck(200, None, None, 600, 4)

car1 = Car(300, None, None, 5, 5)
car2 = Car(400, None, None, 5, 5)

bike1 = Bicycle(500, None, None, 1, 'road')
bike2 = Bicycle(600, None, None, 1, 'mountain')


#-------------------------------------------------------
#FUNCTIONS
#Printing all vehicles
print('------------------')
Vehicle.print_all_vehicles(Vehicle.all_vehicles)
print('------------------')

#Printing all cars
VehicleManager.available_cars()
print('------------------')

#Printing all trucks
VehicleManager.available_trucks()
print('------------------')

#Printing all bicycles
VehicleManager.available_bicycles()
print('------------------')



#DEMONSTRATING HIRING AND RETURNING FUNCTIONS:
#Hiring vehicle
VehicleManager.hire_vehicle(100, '1990/10/10')
print('------------------')

#Trying to hire a vehicle currently on hire
VehicleManager.hire_vehicle(100, '1990/10/10')
print('------------------')

#Demonstrating the hire date
print(f'Hired Vehicle:\nID: {str(truck1.id)} \nHire Date: {str(truck1.hire_date)}')
print('------------------')

#Hired vehicle is no longer in the list of available vehicles
VehicleManager.available_trucks()
print('------------------')

#Returning the vehicle
VehicleManager.return_vehicle(100, '2000/10/12')

print('------------------')

#Returning a vehicle which is not currently on hire
VehicleManager.return_vehicle(100, '2000/10/12')
print('------------------')

#Returned vehicle is now back in the available vehicle list
VehicleManager.available_trucks()
print('------------------')



#CATCHING ERRORS - REMOVE COMMENT TO TEST:

#Entering an invalid bicycle classification.
#bike3 = Bicycle(700, None, None, 1, 'unicycle')

#Hiring a vehicle with unrecognised ID
#VehicleManager.hire_vehicle(999, '1990/10/10')

#Returning a vehicle with an unrecognised ID
#VehicleManager.return_vehicle(84798237489237, '2000/10/12')