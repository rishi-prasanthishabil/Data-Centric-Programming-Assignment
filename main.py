import pandas as pd
import matplotlib.pyplot as plt

# Reading expense.csv
df = pd.read_csv("data/expense.csv")



# 1. Printing all transactions
print(df.to_string(index = False))



# 2. Printing total money spent
total_spent = df["Amount"].sum()

print(f"\n\nTotal spent = {total_spent}")



# 3. Printing total spent by each category
print("\n\nTotal Spent by Category")
category_spending = df.groupby("Category")["Amount"].sum()
print(category_spending.sort_values(ascending = False))



# 4. Printing total spent by store
print("\n\nTotal Spent by Store")
store_spending = df.groupby("Transaction_Name")["Amount"].sum()
print(store_spending.sort_values(ascending = False))



# 5. Printing total spent by transaction type
print("\n\nTotal Spent by Transaction Type")
type_spending = df.groupby("Type")["Amount"].sum()
print(type_spending.sort_values(ascending = False))



# 6. Sorting data by month
# Converting Date column into datetime
df["Date"] = pd.to_datetime(df["Date"], format = "%d/%m/%Y")

# Identifying available months
df["Month"] = df["Date"].dt.to_period("M")

months = df["Month"].unique()


# Analysing each month seperately
for month in months:
    month_df = df[df["Month"] == month]

    print(f"\n\n\nExpense report for {month}")


    # 1. Printing all transactions of a month
    print(month_df.to_string(index = False))

    # Printing total money spent of a month
    total_spent = month_df["Amount"].sum()
    print(f"\n\nTotal spent = {total_spent}")

    # CHART 1: Daily expenditure
    daily_spending = month_df.groupby("Date")["Amount"].sum()

    plt.figure(figsize=(10, 5))
    plt.plot(daily_spending.index, daily_spending.values, marker="o")
    plt.title(f"Daily Expenditure - {month}")
    plt.xlabel("Date")
    plt.ylabel("Amount Spent (€)")
    plt.xticks(rotation=35)
    plt.tight_layout()
    plt.show()



    # 2. Printing total spent by each category of a month
    print("\n\nTotal Spent by Category")
    category_spending = month_df.groupby("Category")["Amount"].sum()
    print(category_spending.sort_values(ascending = False))

    # CHART 2: Spending by category
    plt.figure(figsize=(7, 7))
    plt.pie(
        category_spending.values,
        labels=category_spending.index,
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title(f"Spending by Category - {month}")
    plt.tight_layout()
    plt.show()



    # 3. Printing total spent by store of a month
    print("\n\nTotal Spent by Store")
    store_spending = month_df.groupby("Transaction_Name")["Amount"].sum()
    print(store_spending.sort_values(ascending = False))

    # CHART 3: Spending by store
    store_spending = store_spending.sort_values(ascending = False)

    plt.figure(figsize=(10, 5))
    plt.bar(store_spending.index, store_spending.values)
    plt.title(f"Spending by Store - {month}")
    plt.xlabel("Stores")
    plt.ylabel("Amount Spent (€)")
    plt.xticks(rotation=35)
    plt.tight_layout()
    plt.show()



    # 4. Printing total spent by transaction type of a month
    print("\n\nTotal Spent by Transaction Type")
    type_spending = month_df.groupby("Type")["Amount"].sum()
    print(type_spending.sort_values(ascending = False))

    # CHART 4: Spending by transaction type
    plt.figure(figsize=(7,7))
    plt.pie(
        type_spending.values,
        labels=type_spending.index,
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title(f"Spending by Transaction Type - {month}")
    plt.tight_layout()
    plt.show()

