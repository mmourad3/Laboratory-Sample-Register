from sample import Sample
from sample_register import SampleRegister

def checkStatus(status): #Helper function to check and format the status input
    match status.strip().lower():
        case "r"|"received":
            return "Received"
        case "p"|"processing":
            return "Processing"
        case "c"|"completed":
            return "Completed"
        case _:
            return None
def main():
    register=SampleRegister()
    print(register.loadSamples()) #automatically load from the file when program starts

    while True:
        print("\n1. Register sample")
        print("2. Change sample status")
        print("3. View all samples")
        print("4. Add reading")
        print("5. View statistics")
        print("6. Count out of range readings and find longest streak")
        print("7. View filtered samples")
        print("8. Save")
        print("9. Load")
        print("10. Exit")

        choice=input("Enter your choice: ").strip()

        match choice:
            case "1":
                ID=input("Enter sample ID: ").strip().lower()
                error=register.validateID(ID,False)
                if error:
                    print(error)
                    continue
                Type=input("Enter sample type: ").strip().lower()
                if Type=="":
                    print("Type cannot be empty")
                    continue
                sample=Sample(ID,Type)
                print(register.registerSample(sample))

            case "2":
                ID=input("Enter sample ID: ").strip().lower()
                error=register.validateID(ID)
                if error:
                    print(error)
                    continue
                newStatus=checkStatus(input("Enter new status (P/C): "))
                if newStatus==None or newStatus=="Received": #cannot change status to Received
                    print("Invalid status. Enter P or C")
                    continue
                print(register.change_status(ID,newStatus))

            case "3":
                if not register.samples:
                    print("No samples registered")
                else:
                    print("\nRegistered samples:")
                    for sample in register.samples.values():
                        print(sample)

            case "4":
                ID=input("Enter sample ID: ").strip().lower()
                error=register.validateID(ID)
                if error:
                    print(error)
                    continue
                try:
                    reading=float(input("Enter reading: "))
                    print(register.add_Reading(ID,reading))
                except ValueError:
                    print("Invalid reading. Must be numeric value")

            case "5":
                ID=input("Enter sample ID: ").strip().lower()
                print(register.get_Statistics(ID))

            case "6":
                ID=input("Enter sample ID: ").strip().lower()
                error=register.validateID(ID)
                if error:
                    print(error)
                    continue
                sample=register.samples[ID]
                if not sample.getReadings(): #Check if the sample has any readings before asking for limits
                    print("Sample has no readings")
                    continue
                try:
                    lower=float(input("Enter lower limit: "))
                    upper=float(input("Enter upper limit: "))
                    error=sample.validateLimits(lower,upper) #validate the limits before counting and finding longest streak
                    if error:
                        print(error)
                        continue
                    res=register.count_out_of_range(ID, lower, upper)
                    streak=register.longest_out_of_range(ID, lower, upper)
                    print(f'Number of readings out of range: {res}')
                    print(f'Longest out of range readings streak: {streak}')
                except ValueError:
                    print("Invalid limit values. Must be numeric values")
                    
            case "7":
                if not register.samples: #check if there are any registered samples before filtering
                    print("No samples registered")
                    continue
                filterChoice=input("Enter filtering option (T/S): ").strip().lower()
                match filterChoice:
                    case "t"|"type":
                        t=input("Enter type:").strip().lower()
                        matches=register.filter("type", t) #Get the samples that match the type entered by the user
                    case "s"|"status":
                        status=checkStatus(input("Enter status (R/P/C):"))
                        if status==None:
                            print("Invalid status. Enter R, P or C")
                            continue
                        matches=register.filter("status", status) #get the samples that match the status entered by the user
                    case _:
                        print("Invalid filtering option. Enter T or S")
                        continue
                if not matches: #check if the returned list is empty
                    print("No match found")
                else:
                    for sample in matches: #display each matching sample
                        print(sample)
            case "8":
                print(register.saveSamples())
            case "9":
                confirm=input("Any unsaved changes will be lost. Continue? (Y/N): ").strip().lower()
                if confirm=="y" or confirm=="yes":
                    print(register.loadSamples())
                elif confirm=="n" or confirm=="no":
                    print("Load cancelled")
                else:
                    print("Invalid choice. Enter Y/Yes or N/No")
            case "10":
                print("Goodbye")
                break

            case _:
                print("Invalid choice. Enter a number from 1 to 10")
                
if __name__=="__main__":
    main()