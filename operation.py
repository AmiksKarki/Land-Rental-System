import read
import datetime
import random
import write

# List to store information about all rented lands
rented_lands = []
returned_lands=[]
def displayLands():
    print("╔","═"*100,"╗",sep='')
    print("║",' '*40,"Lands that we have",' '*42,'║', sep='')
    print("╚",'═'*100,'╝',sep='')
    print("╔","═"*100,"╗",sep='')
    print("║","Kitta Number","║"," "*4,"City"," "*4,"║","Face(Moda)","║","Area(Anna)","║","Price Per Anna","║"," "*3,"Available Status"," "*2,'║',)
    print("╚",'═'*100,'╝',sep='')
    for row in read.landList():
        print("║",row[0]+" "*(13-len(row[0]))+"  ",row[1]+" "*(15-len(row[1]))+"  ",row[2]+" "*(12-len(row[2]))+"  ",row[3]+" "*(10-len(row[3]))+"  ",row[4]+" "*(9-len(row[4]))+" "*5,row[5]+" "*(21-len(row[5])),"║")#prints the each row of the list
    print("╚",'═'*100,'╝',sep='')


def calculateFine(actual_rented_duration, initial_duration):
    if actual_rented_duration>initial_duration:
        durationDifference=actual_rented_duration-initial_duration
    else:
      durationDifference=0
    fine=(10/100)*durationDifference
    return fine


def rent_land():
    kittaValidated=False
    while not kittaValidated:
        try:
            kitta_number = input("Enter kitta number of the land you want to rent: ")
            land_info=read.landList()
            if int(kitta_number) <= 0:
                print("╔","═"*100,"╗",sep='')
                print(' '*30,"Kitta Number must be a positive integer!!!")
                print("╚",'═'*100,'╝',sep='')
            else:
                for land in land_info:
                    if land[0].strip() == kitta_number:
                            if land[5].strip() == 'Available':
                                land[-1] = 'Not Available'
                                kittaValidated=True
                            else:
                                print("╔","═"*100,"╗",sep='')
                                print(' '*20,"The land with kitta number:",land[0],"is not available!!!")
                                print("╚",'═'*100,'╝',sep='')
                            break  # breaks the loop and does not compare any other land kitta number if one kitta is validated     
                else:
                    '''The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
                        The else block will NOT be executed if the loop is stopped by a break statement.'''
                    print("╔","═"*100,"╗",sep='')
                    print(' '*10,"The kitta number does not match please enter the kitta number present in the list")
                    print("╚",'═'*100,'╝',sep='')
                while kittaValidated:
                    try:
                        duration = int(input("Enter duration of rent (in months): "))
                        if(duration<=0):
                            print("╔","═"*100,"╗",sep='')
                            print(' '*20,"Duration must be greater than 0!!!")
                            print("╚",'═'*100,'╝',sep='')
                        else:
                            write.update_land_status(kitta_number, 'Not Available')  # Update land status
                            rented_lands.append((kitta_number, duration)) #adding the rented land details
                            break
                    except ValueError as e:
                        print("╔","═"*100,"╗",sep='')
                        print(' '*30,"Invalid data type entered!!!")
                        print("╚",'═'*100,'╝',sep='')
        except ValueError as e:
            print("╔","═"*100,"╗",sep='')
            print(' '*30,"Invalid data type entered!!!")
            print("╚",'═'*100,'╝',sep='')

def return_land():
    kittaValidated=False
    while not kittaValidated:
        try:
            kitta_number = input("Enter kitta number of the land you want to return: ")
            land_info=read.landList()
            if int(kitta_number) <= 0:
                print("╔","═"*100,"╗",sep='')
                print(' '*30,"Kitta Number must be a positive integer!!!")
                print("╚",'═'*100,'╝',sep='')
            else:
                for land in land_info:
                    if land[0].strip() == kitta_number:
                            if land[5].strip() == 'Not Available':
                                land[-1] = 'Available'
                                kittaValidated=True
                                break
                            else:
                                print("╔","═"*100,"╗",sep='')
                                print(" "*20,"The land with kitta number:",land[0],"is not rented! Please rent it first to return!!!")
                                print("╚",'═'*100,'╝',sep='')
                                break
                else:
                    '''The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
                        The else block will NOT be executed if the loop is stopped by a break statement.'''
                    print("╔","═"*100,"╗",sep='')
                    print(' '*10,"The kitta number does not match please enter the kitta number present in the list!!!")
                    print("╚",'═'*100,'╝',sep='')
                while kittaValidated:
                    try:
                        initial_duration=int(input("Enter the duration that you initially rented the lands for (in months): "))
                        actual_rented_duration = int(input("Enter duration that you actually rented the lands for (in months): "))
                        if(actual_rented_duration<=0 or initial_duration<=0):
                            print("╔","═"*100,"╗",sep='')
                            print(' '*20,"Duration must be greater than 0!!!")
                            print("╚",'═'*100,'╝',sep='')
                        else:
                            write.update_land_status(kitta_number, 'Available')  # Update land status
                            fine = calculateFine(actual_rented_duration, initial_duration)
                            returned_lands.append((kitta_number, actual_rented_duration,fine)) #adding the rented land details
                            break
                    except ValueError as e:
                        print("╔","═"*100,"╗",sep='')
                        print(' '*30,"Invalid data type entered!!!")
                        print("╚",'═'*100,'╝',sep='')
        except ValueError as e:
            print("╔","═"*100,"╗",sep='')
            print(' '*30,"Invalid data type entered!!!")
            print("╚",'═'*100,'╝',sep='')



