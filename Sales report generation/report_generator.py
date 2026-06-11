import pandas as pd

# LOAD DATA

df = pd.read_csv("superstore dataset.csv", encoding='latin1')

print("DATA PREPROCESSING RESULTS")

# Dataset shape before cleaning
print("\nRows before cleaning:", len(df))
print("Columns before cleaning:", len(df.columns))

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate rows count
duplicates = df.duplicated().sum()
print("\nDuplicate Rows:", duplicates)

# Remove duplicates
df = df.drop_duplicates()

# Remove missing values
df = df.dropna()

print("\nRows after cleaning:", len(df))

# Validation
if df.isnull().sum().sum()==0:
    print("Validation Status: PASSED")
else:
    print("Validation Status: FAILED")


print("\n")
print("AUTOMATED SALES REPORT")

# KPI CALCULATIONS

total_sales = df["Sales"].sum()

average_sales = df["Sales"].mean()

top_region = (
    df.groupby("Region")["Sales"]
    .sum()
    .idxmax()
)

top_category = (
    df.groupby("Category")["Sales"]
    .sum()
    .idxmax()
)

highest_sale = df["Sales"].max()

total_orders = len(df)

print("\nTotal Orders:", total_orders)

print("Total Sales: $", round(total_sales,2))

print("Average Sales: $", round(average_sales,2))

print("Highest Single Sale: $", round(highest_sale,2))

print("Top Performing Region:", top_region)

print("Top Selling Category:", top_category)

# EXPORT REPORT

report = {
    "Metric":[
        "Total Orders",
        "Total Sales",
        "Average Sales",
        "Highest Single Sale",
        "Top Region",
        "Top Category"
    ],

    "Value":[
        total_orders,
        round(total_sales,2),
        round(average_sales,2),
        round(highest_sale,2),
        top_region,
        top_category
    ]
}

report_df=pd.DataFrame(report)

report_df.to_excel(
    "Sales_Report.xlsx",
    index=False
)

print("\nExcel report generated successfully")

