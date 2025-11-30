class AddPerson:
    def __init__(self, names_list):
        self.names_list = names_list

class AddExpense(AddPerson):
    def __init__(self, names_list, paid_by, total, description):
        super().__init__(names_list)
        self.paid_by = paid_by
        self.total = total
        self.description = description

        if self.paid_by not in self.names_list:
            print("Recheck who paid the bill.......")
            return

        print(f"'{paid_by}' paid '${total}' for {description} "
              f"which is going to be equally split amongst {self.names_list}")

        with open("data.txt", "a") as f:
            f.write(f"{paid_by} paid ${total} for {description} split among {self.names_list}\n")
class calculateBalance(AddPerson):
    def __init__(self,a):
        self.total=a.total
        self.paid_by=a.paid_by
        self.names_list=a.names_list
        self.split=self.total/len(self.names_list)
        for i in self.names_list:
            if(i!=self.paid_by):
                print(f"{i} ki {self.paid_by} se {self.split:.2f} ki udhari hai ....")
                
        

participants = [] 

start = input("Do you want to start the splitting (y/n): ")

if start == 'y':
    while True:
        print("""
1.) Enter 1 to add participants 
2.) Enter 2 to add Expense details and description
3.) Enter 3 to Calculate Balance
4.) Enter 4 to view the details of the expense
5.) Save and Exit
        """)

        choice = int(input("Enter your choice: "))

    
        if choice == 1:
            count = int(input("How many participants do you want to add: "))
            for i in range(count):
                name = input("Enter the name: ").capitalize()
                if name in participants:
                    print("Name already exists..")
                else:
                    participants.append(name)

            person_obj = AddPerson(participants)
            print("Participants added:", participants)


        elif choice == 2:
            if len(participants) == 0:
                print("Add participants first!")
                continue

            paid_by = input("Who paid the bill? : ").capitalize()
            total = int(input("Total Amount that's been paid: "))
            desc = input("Description of the expense: ")

            a=AddExpense(participants, paid_by, total, desc)


        elif choice == 3:
            calculateBalance(a)

        elif choice == 4:
            print("\nExpense File ")
            try:
                with open("data.txt", "r") as f:
                    print(f.read())
            except:
                print("No data found.")


        elif choice == 5:
            print("Saving & Exiting...")
            break

        else:
            print("Invalid choice please enter a valid choice........")
