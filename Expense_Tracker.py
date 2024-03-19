import csv

# Function jo record krega expenses ho
def expense(date, category, amount):
    with open('expenses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

# # Function jo show krega expenses ho
def view():
    with open('expenses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Date: {row[0]}, Category: {row[1]}, Amount: {row[2]}₹!")

def main():
    while True:
        print("\nExpense Tracking System")
        print("1. Record Expense")
        print("2. View All Expenses")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter date (DD-MM-YYYY): ")
            category = input("Enter expense category: ")
            amount = input("Enter expense amount: ")
            expense(date, category, amount)
            print("Expense recorded successfully!")
        elif choice == '2':
            print("\nAll Expenses:")
            view()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
