import pandas as pd
import matplotlib.pyplot as plt
import subprocess


# Clearing terminal function
def clear_terminal():
    subprocess.run("cls", shell=True)



# Main Menu function
def main_menu():
    print("\n\nEXPENSE TRACKER")
    print("Main Menu")
    print("1. View dashboard")
    print("2. Monthly expense report")
    print("3. Exit program")

    option = int(input("\nSelect an option: "))

    clear_terminal()

    return option



# Month Menu function
def month_menu():
    i = 1

    print("\nList of Months:")
    for month in months:
        print(f"{i}. {month}")
        i += 1

    month_option = int(input("Select a month to analyse: "))

    clear_terminal()

    return months[month_option - 1]



# Function dashboard()
# Displays a summary of your expenses
#
def dashboard():
    month_total = df.groupby("Month")["Amount"].sum()
    average = month_total.sum() / len(month_total)

    # Displaying average monthly spending
    print(f"\n\nAverage monthly spending = €{average:.2f}")

    # Displaying last 5 transactions
    print("\nLast 5 Transactions")
    print(df.tail(5).iloc[::-1].to_string(index = False))

    # CHART: Monthly expenditure
    plt.figure(figsize=(10, 5))
    plt.plot(month_total.index.astype(str), month_total.values, marker="o")
    plt.title("Monthly Expenditure Trend")
    plt.xlabel("Month")
    plt.ylabel("Amount Spent (€)")
    plt.xticks(rotation=35)
    plt.tight_layout()
    plt.show()

    clear_terminal()



# Function monthly_transaction()
# Lists all of the transactions in a month and displays a trend chart
#
def monthly_transaction(month_df, selected_month):

    print(f"\n\n\nAll transactions for {selected_month}")


    # Printing all transactions of a month
    print(month_df.to_string(index = False))

    # Printing total money spent of a month
    total_spent = month_df["Amount"].sum()
    print(f"\n\nTotal spent = {total_spent}")

    # CHART: Daily expenditure
    daily_spending = month_df.groupby("Date")["Amount"].sum()

    plt.figure(figsize=(10, 5))
    plt.plot(daily_spending.index, daily_spending.values, marker="o")
    plt.title(f"Daily Expenditure - {selected_month}")
    plt.xlabel("Date")
    plt.ylabel("Amount Spent (€)")
    plt.xticks(rotation=35)
    plt.tight_layout()
    plt.show()

    clear_terminal()



# Function monthly_store()
# Displays total spending in a month by store with a bar chart
#
def monthly_store(month_df, selected_month):

    print(f"\n\nTotal Spent by Store during {selected_month}")

    store_spending = month_df.groupby("Transaction_Name")["Amount"].sum()
    print(store_spending.sort_values(ascending = False))
    
    # CHART: Spending by store
    store_spending = store_spending.sort_values(ascending = False)
    
    plt.figure(figsize=(10, 5))
    plt.bar(store_spending.index, store_spending.values)
    plt.title(f"Spending by Store - {selected_month}")
    plt.xlabel("Stores")
    plt.ylabel("Amount Spent (€)")
    plt.xticks(rotation=35)
    plt.tight_layout()
    plt.show()

    clear_terminal()



# Function monthly_category()
# Displays total spending in a month by category with a pie chart
#
def monthly_category(month_df, selected_month):

    print(f"\n\nTotal Spent by Category during {selected_month}")

    category_spending = month_df.groupby("Category")["Amount"].sum()
    print(category_spending.sort_values(ascending = False))

    # CHART: Spending by category
    plt.figure(figsize=(7, 7))
    plt.pie(
        category_spending.values,
        labels=category_spending.index,
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title(f"Spending by Category - {selected_month}")
    plt.tight_layout()
    plt.show()

    clear_terminal()



# Function monthly_type()
# Displays total spending in a month by transaction type with a pie chart
#
def monthly_type(month_df, selected_month):

    print(f"\n\nTotal Spent by Transaction Type during {selected_month}")

    type_spending = month_df.groupby("Type")["Amount"].sum()
    print(type_spending.sort_values(ascending = False))

    # CHART: Spending by transaction type
    plt.figure(figsize=(7,7))
    plt.pie(
        type_spending.values,
        labels=type_spending.index,
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title(f"Spending by Transaction Type - {selected_month}")
    plt.tight_layout()
    plt.show()

    clear_terminal()



# Monthly analysis menu
def monthly_analysis_menu(selected_month):

    # Create a dataframe for the selected month
    month_df = df[df["Month"] == selected_month]

    while True:
        print(f"\n\nYou selected {selected_month}")
        print(f"What do you wish to see from {selected_month}?")
        print("1. View all transaction this month")
        print("2. View total spent by store")
        print("3. View total spent by category")
        print("4. View total spent by transaction type")
        print("5. Go back to Main Menu")

        option = int(input("\nSelect an option: "))
        clear_terminal()

        if option == 1:
            monthly_transaction(month_df, selected_month)
        
        elif option == 2:
            monthly_store(month_df, selected_month)
        
        elif option == 3:
            monthly_category(month_df, selected_month)
        
        elif option == 4:
            monthly_type(month_df, selected_month)
        
        elif option == 5:
            break

        else:
            print("\nWrong input! Try again")
            monthly_analysis_menu(selected_month)



# Selecting functions from the menu
def menu_selection():
    selected_option = main_menu()

    if selected_option == 1:
        dashboard()

    elif selected_option == 2:
        selected_month = month_menu()
        monthly_analysis_menu(selected_month)

    elif selected_option == 3:
        print("\nYou chose to exit program")
        exit()
    
    else:
        print("\nWrong input! Try again")



#*********************************************************************
# Main program
#
# Reading expense.csv
df = pd.read_csv("data/expense.csv")


# Converting Date column into datetime
df["Date"] = pd.to_datetime(df["Date"], format = "%d/%m/%Y")

# Sorting date by months
df["Month"] = df["Date"].dt.to_period("M")

months = df["Month"].unique()

while True:
    menu_selection()


