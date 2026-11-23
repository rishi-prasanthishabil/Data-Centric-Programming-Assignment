import pandas as pd

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

    # Printing all transactions of a month
    print(month_df.to_string(index = False))

    # Printing total money spent of a month
    total_spent = month_df["Amount"].sum()
    print(f"\n\nTotal spent = {total_spent}")

    # Printing total spent by each category of a month
    print("\n\nTotal Spent by Category")
    category_spending = month_df.groupby("Category")["Amount"].sum()
    print(category_spending.sort_values(ascending = False))

    # Printing total spent by store of a month
    print("\n\nTotal Spent by Store")
    store_spending = month_df.groupby("Transaction_Name")["Amount"].sum()
    print(store_spending.sort_values(ascending = False))

    # Printing total spent by transaction type of a month
    print("\n\nTotal Spent by Transaction Type")
    type_spending = month_df.groupby("Type")["Amount"].sum()
    print(type_spending.sort_values(ascending = False))


