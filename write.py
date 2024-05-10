import read
import random
import datetime
import operation

def update_land_status(kitta_number, status):
    try:
        land_info = read.landList()  # Call the function from read.py to get the list
        file=open("landList.txt", "w")#opening file in write mode truncates the file, meaning it removes all existing content.
        for data in land_info:
            if data[0] == kitta_number:
                data[-1] = status
            file.write(','.join(data) + '\n')  # Write the modified data back to the file
    except FileNotFoundError:
        print("File not found.")

def print_rent_invoice():

    # Generate a random invoice number
    invoice_number = ''.join(random.choices('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=8))#random choices returns a list from the given choices so we convert it into string using join
    # Assuming the customer's name is obtained through input
    customer_name = input("Enter your name: ")
    # Current date and time
    rent_time = datetime.datetime.now()
    # Write invoice to a .txt file
    invoice = "Rent_Invoice_" + invoice_number + "_" + customer_name + ".txt"

    try:
        invoice_file = open(invoice, "w")
        invoice_file.write("╔"+"═"*100+"╗"+"\n")
        invoice_file.write("║"+' '*47+"Invoice"+' '*46+'║'+"\n")
        invoice_file.write("║"+"═"*100+"║"+"\n")

        invoice_file.write("║"+" "*62+"Invoice Number:" + invoice_number+" "*15+"║"+"\n")
        invoice_file.write("║"+" "*62+"Rented Date:"+str(rent_time)+"║"+"\n")
        invoice_file.write("║"+"Customer Name:"+customer_name+" "*(86-len(customer_name))+"║"+"\n")
        
        invoice_file.write("║"+"═"*100+"║"+"\n")
        invoice_file.write("║"+"Kitta Number"+"║"+" "*4+"City"+" "*4+"║"+" "*1+"Face(Moda)"+" "*1+"║"+" "*1+"Area(Anna)"+" "*1+"║"+" "*1+"Duration"+" "*1+"║"+" "*1+"Rate(Rs)"+" "*1+"║"+" "*1+"Amount(Rs)"+" "*15+'║'+"\n")
        invoice_file.write("║"+"═"*100+"║"+"\n")
        subTotal=0
        totalAmt=0
        for kitta_number, duration in operation.rented_lands:
            #we created a new list land_info which stores the list which has the kitta number of the rented land
            land_info = []
            for land in read.landList():
                if land[0]==kitta_number:
                    land_info=land
                    break
        
            # Extract required information
            city = land_info[1]
            direction = land_info[2]
            area = land_info[3]
            price=int(land_info[4])
            # Calculate total amount based on duration and land area
            rent_amount = int(area) * duration * int(price) # Assuming the rate is 1000 NPR per anna per month
            subTotal+=rent_amount
            invoice_file.write(" "+str(kitta_number)+" "*(13-len(str(kitta_number)))+city+" "*(15-len(city))+direction+" "*(12-len(direction))+str(area)+" "*(13-len(str(area)))+str(duration)+" "*(10-(len(str(duration))))+str(price)+" "*(12-len(str(price)))+str(rent_amount)+" "*(13-len(str(rent_amount)))+" "*10+"\n")
        totalAmt=subTotal+(13/100)*subTotal
        invoice_file.write("║"+"═"*100+"║"+"\n")
        invoice_file.write(" "*62+"Sub Total:"+str(subTotal)+" "*(30-len(str(subTotal)))+"\n") #we are converting int to again str cause int does not have length so counting spaces is not possible
        invoice_file.write(" "*62+"Total Amount(13% VAT):"+str(totalAmt)+" "*(19-len(str(totalAmt)))+"\n")
        invoice_file.write("╚"+'═'*100+'╝'+"\n")   
        print("Invoice generated successfully:", invoice)
        invoice_file.close()
    except Exception as e:
        print("An error occurred while generating the invoice:", e)
    # to display the invoice in the console
    file=open(invoice,"r")
    print(file.read())

def print_return_invoice():
    # Generate a random invoice number
    invoice_number = ''.join(random.choices('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=8))#random choices returns a list from the given choices so we convert it into string using join
    # Assuming the customer's name is obtained through input
    customer_name = input("Enter your name: ")
    # Current date and time
    rent_time = datetime.datetime.now()
    # Write invoice to a .txt file
    invoice = "Return_Invoice_" + invoice_number + "_" + customer_name + ".txt"

    try:
        invoice_file = open(invoice, "w")
        invoice_file.write("╔"+"═"*120+"╗"+"\n")
        invoice_file.write("║"+' '*57+"Invoice"+' '*56+'║'+"\n")
        invoice_file.write("║"+"═"*120+"║"+"\n")
        invoice_file.write("║"+" "*80+"Invoice Number:" + invoice_number+" "*17+"║"+"\n")
        invoice_file.write("║"+" "*80+"Returned Date:"+str(rent_time)+"║"+"\n")
        invoice_file.write("║"+"Customer Name:"+customer_name+" "*(106-len(customer_name))+"║"+"\n")
        invoice_file.write("║"+"═"*120+"║"+"\n")
        invoice_file.write("║"+"Kitta Number"+"║"+" "*4+"City"+" "*4+"║"+" "*1+"Face(Moda)"+" "*1+"║"+" "*1+"Area(Anna)"+" "*1+"║"+" "*1+"Duration"+" "*1+"║"+" "*1+"Rate(Rs)"+" "*1+"║"+" "*1+"Amount(Rs)"+" "*1+"║"+" "*1+"Fine Amount(Rs)"+" "*17+'║'+"\n")
        invoice_file.write("║"+"═"*120+"║"+"\n")
        subTotal=0
        totalAmt=0
        for kitta_number, duration, fine in operation.returned_lands:
            #we created a new list land_info which stores the list which has the kitta number of the rented land
            land_info = []
            for land in read.landList():
                if land[0]==kitta_number:
                    land_info=land
                    break
        
            # Extract required information
            city = land_info[1]
            direction = land_info[2]
            area = land_info[3]
            price=land_info[4]
            
            # Calculate total amount based on duration and land area
            rent_amount = int(area) * duration * int(price) # Assuming the rate is 1000 NPR per anna per month
            fineAmount=fine*int(area)*int(price)
            subTotal=subTotal+rent_amount+fineAmount
            invoice_file.write(" "+str(kitta_number)+" "*(13-len(str(kitta_number)))+city+" "*(15-len(city))+direction+" "*(12-len(direction))+str(area)+" "*(13-len(str(area)))+str(duration)+" "*(10-(len(str(duration))))+str(price)+" "*(12-len(str(price)))+str(rent_amount)+" "*(13-len(str(rent_amount)))+str(fineAmount)+" "*(13-len(str(fineAmount)))+" "*18+"\n")
        totalAmt=subTotal+(13/100)*subTotal
        invoice_file.write("║"+"═"*120+"║"+"\n")
        invoice_file.write(" "*82+"Sub Total:"+str(subTotal)+" "*(30-len(str(subTotal)))+"\n") #we are converting int to again str cause int does not have length so counting spaces is not possible
        invoice_file.write(" "*82+"Total Amount(13% VAT):"+str(totalAmt)+" "*(19-len(str(totalAmt)))+"\n")
        invoice_file.write("╚"+'═'*120+'╝'+"\n")   
        print("Invoice generated successfully:", invoice)
        invoice_file.close()
    except Exception as e:
        print("An error occurred while generating the invoice:", e)
    # to display the invoice in the console
    file=open(invoice,"r")
    print(file.read())
