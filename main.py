from sample import Sample
from sample_register import SampleRegister

#For testing purposes
def main():
    register=SampleRegister()

    while True:
        print("\n1. Register sample")
        print("2. Change sample status")
        print("3. View samples")
        print("4. Exit")

        choice=input("Enter your choice: ").strip()

        match choice:
            case "1":
                ID=input("Enter sample ID: ").strip().lower()
                Type=input("Enter sample type: ").strip().lower()

                if ID=="":
                    print("ID cannot be empty")
                elif Type=="":
                    print("Type cannot be empty")
                else:
                    sample=Sample(ID,Type)
                    print(register.registerSample(sample))

            case "2":
                ID=input("Enter sample ID: ").strip().lower()
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
                print("Goodbye")
                break

            case _:
                print("Invalid choice")
main()