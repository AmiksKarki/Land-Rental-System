import operation
import read
import write

def main():
    print("╔","═"*100,"╗",sep='')
    print("║",' '*40,"Techno Property Nepal",' '*39,'║', sep='')
    print("╚",'═'*100,'╝',sep='')

    keepRunning=True
    while keepRunning==True:
        print("╔","═"*100,"╗",sep='')
        print("║",'.'*40,"Type 1 to Rent Land",'.'*41,'║', sep='')
        print("║",'.'*40,"Type 2 to Return Land",'.'*39,'║', sep='')
        print("║",'.'*40,"Type 3 to Exit the System",'.'*35,'║', sep='')
        print("╚",'═'*100,'╝',sep='')
        try:
            userOption=int(input("Enter the value from above mentioned options: "))

            if userOption==1:
                operation.displayLands()
                askInput=True
                while askInput==True:
                # display land information, ask kitta number, validate kitta number, month validate
                    operation.rent_land()#the 2 parameters returned here are used to print the invoice
                    askMore=True
                    while askMore:
                        userInput=input("Do you want to Rent more lands???(yes/no): ")
                        if userInput.upper()=="NO":
                            askInput=False
                            askInvoice=True
                            askMore=False
                            while askInvoice:
                                invoiceInput=input("Do you want to print the invoice now?(yes/no): ")
                                if(invoiceInput.upper()=="YES"):
                                    write.print_rent_invoice()
                                    askInvoice=False
                                    keepRunning=True
                                elif(invoiceInput.upper()=="NO"):
                                    print("╔","═"*100,"╗",sep='')
                                    print(' '*40,"You are exiting the Rental system now!!")
                                    print("╚",'═'*100,'╝',sep='')
                                    askInvoice=False
                                    askInput=False
                                    keepRunning=True
                                else:
                                    print("╔","═"*100,"╗",sep='')
                                    print(' '*40,"Enter the Valid Input(yes/no): ")
                                    print("╚",'═'*100,'╝',sep='')
                        elif userInput.upper()=="YES":
                            askInput=True
                            askMore=False
                        else:
                            print("╔","═"*100,"╗",sep='')
                            print(' '*40,"Enter the Valid Input!! Enter -> (yes or no) ")
                            print("╚",'═'*100,'╝',sep='')

            elif userOption==2:
                operation.displayLands()
                askInput=True
                while askInput==True:
                # display land information, ask kitta number, validate kitta number, month validate
                    operation.return_land()#the 2 parameters returned here are used to print the invoice
                    askMore=True
                    while askMore:
                        userInput=input("Do you want to Return more lands???(yes/no): ")
                        if userInput.upper()=="NO":
                            askInput=False
                            askInvoice=True
                            askMore=False
                            while askInvoice:
                                invoiceInput=input("Do you want to print the invoice now?(yes/no): ")
                                if(invoiceInput.upper()=="YES"):
                                    write.print_return_invoice()
                                    askInvoice=False
                                    keepRunning=True
                                elif(invoiceInput.upper()=="NO"):
                                    print("╔","═"*100,"╗",sep='')
                                    print(' '*40,"You are exiting the Return System")
                                    print("╚",'═'*100,'╝',sep='')
                                    askInvoice=False
                                    askInput=False
                                    keepRunning=True
                                else:
                                    print("╔","═"*100,"╗",sep='')
                                    print(' '*40,"Enter the Valid Input(yes/no): ")
                                    print("╚",'═'*100,'╝',sep='')
                        elif userInput.upper()=="YES":
                            askMore=False
                            askInput=True
                        else:
                            print("╔","═"*100,"╗",sep='')
                            print(' '*40,"Enter the Valid Input(yes/no)",'~'*34)
                            print("╚",'═'*100,'╝',sep='')
            elif userOption==3:
                print("╔","═"*100,"╗",sep='')
                print("║",'~'*40,"You are exiting the System.",'~'*33,'║', sep='')
                print("╚",'═'*100,'╝',sep='')
                keepRunning=False
            else:
                print("╔","═"*100,"╗",sep='')
                print("║",'~'*40,"Enter the Valid Input(1-3)",'~'*34,'║', sep='')
                print("╚",'═'*100,'╝',sep='')
        except ValueError as e:
            print("Invalid data type entered")
main()