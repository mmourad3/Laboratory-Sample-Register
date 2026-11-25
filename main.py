from sample import Sample
from sample_register import SampleRegister

#For testing purposes
def main():
    register=SampleRegister()

    while True:
        print("\n1. Register sample")
        print("2. Change sample status")
        print("3. View samples")
        print("4. Add reading")
        print("5. View statistics")
        print("6. Exit")

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
                newStatus=input("Enter new status (P/C): ").strip().lower()

                match newStatus:
                    case "p" | "processing":
                        newStatus="Processing"
                    case "c" | "completed":
                        newStatus="Completed"
                    case _:
                        print("Invalid status")
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
                    print("Invalid reading")

            case "5":
                ID=input("Enter sample ID: ").strip().lower()
                print(register.get_Statistics(ID))

            case "6":
                print("Goodbye")
                break

            case _:
                print("Invalid choice")
main()