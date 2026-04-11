# HARI
# Importing required libraries
import pandas as pd

# -----------------------------
# EMPLOYEE DATA
# -----------------------------
employee_details = pd.DataFrame({
    'EmployeeID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Department': ['HR', 'Engineering', 'Engineering', 'HR', 'Marketing']
})

employee_salaries = pd.DataFrame({
    'EmployeeID': [101, 102, 103, 104, 105],
    'Salary': [50000, 70000, 80000, 55000, 60000]
})

# -----------------------------
# SALES DATA
# -----------------------------
sales_region_1 = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
    'Region': ['North'] * 5,
    'Sales': [250, 300, 200, 400, 350]
})

sales_region_2 = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
    'Region': ['South'] * 5,
    'Sales': [300, 320, 280, 360, 310]
})

# -----------------------------
# DISPLAY
# -----------------------------
print("Employee Details:\n", employee_details)
print("\nEmployee Salaries:\n", employee_salaries)
print("\nSales Region 1:\n", sales_region_1)
print("\nSales Region 2:\n", sales_region_2)

# -----------------------------
# GROUPING
# -----------------------------
avg_salary_per_dept = employee_details.merge(employee_salaries, on='EmployeeID') \
                                      .groupby('Department')['Salary'].mean()

print("\nAverage Salary per Department:\n", avg_salary_per_dept)

# -----------------------------
# MERGING
# -----------------------------
merged_data = pd.merge(employee_details, employee_salaries, on='EmployeeID')

print("\nMerged Employee Data:\n", merged_data)

# -----------------------------
# JOINING
# -----------------------------
stock_prices = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
    'Price': [150, 155, 152, 158, 160]
}).set_index('Date')

market_volume = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
    'Volume': [1000, 1100, 1050, 1150, 1200]
}).set_index('Date')

print("\nStock Prices Data:\n", stock_prices)
print("\nMarket Volume Data:\n", market_volume)

joined_data = stock_prices.join(market_volume)

print("\nJoined Stock Prices and Market Volume Data:\n", joined_data)

# -----------------------------
# CONCATENATION
# -----------------------------
consolidated_sales = pd.concat([sales_region_1, sales_region_2])

print("\nConsolidated Sales Data:\n", consolidated_sales)
