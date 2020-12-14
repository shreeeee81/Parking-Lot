from ParkingLot import ParkingLot
import fileinput
print("---------------------PARKING LOT---------------------")
print("Use the commands below to run this PARKING LOT System")
print("Create_parking_lot 6")
print("Park KA-01-HH-1234 driver_age 21")
print("Park PB-01-HH-1234 driver_age 21")
print("Slot_numbers_for_driver_of_age 21")
print("Park PB-01-TG-2341 driver_age 40")
print("Slot_number_for_car_with_number PB-01-HH-1234")
print("Leave 2")
print("Park HR-29-TG-3098 driver_age 39")
print("Vehicle_registration_number_for_driver_of_age 18")
print("---------------ENTER COMMAND NOW--------------------")


for line in fileinput.input():

    '''here reading command one by one'''
    if 'Create_parking_lot' in line:
       data = line.split()
       parkingLot=ParkingLot(int(data[1]))
    if 'Park ' in line:
        data = line.split()
        slotflag = parkingLot.isSlotAvailable()
        if slotflag == True:
           slotNumber=parkingLot.getAvailableSlot()
           parkingLot.parkThePark(slotNumber,data[1],data[3])
        else:
            print("Sorry, parking lot is full")
    if 'Leave' in line:
        data = line.split()
        parkingLot.leaveTheCar(int(data[1]))
    if 'Status' in line:
        parkingLot.showParkingStatus()
    if 'Slot_numbers_for_driver_of_age' in line:
       data = line.split()
       parkingLot.Slot_numbers_for_driver_of_age(data[1])
    if 'Vehicle_registration_number_for_driver_of_age' in line:
       data = line.split()
       parkingLot.Vehicle_registration_number_for_driver_of_age(data[1])
    if 'Slot_number_for_car_with_number' in line:
       data = line.split()
       parkingLot.getSlotNumberForRegistrationNumber(data[1])
