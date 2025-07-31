import pandas as pd

def generate_sales_report(file_path, report_type='product_sales', output_file=None, product_col=None, sales_col=None):
    """
    Generates a sales report based on the specified type.

    Args:
        file_path (str): Path to the CSV file containing sales data.
        report_type (str): Type of report to generate.
                           Options: 'product_sales', 'region_sales', 'top_products'.
        output_file (str, optional): Path to save the report as a CSV.
                                     If None, the report will be printed.
        product_col (str, optional): The name of the column containing product names.
        sales_col (str, optional): The name of the column containing sales values.
    """
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return

    if product_col not in df.columns or sales_col not in df.columns:
        print(f"Error: Required columns '{product_col}' or '{sales_col}' not found in the CSV file.")
        return

    if report_type == 'product_sales':
        report = df.groupby(product_col)[sales_col].sum().reset_index()
        report.rename(columns={sales_col: 'Total Sales', product_col: 'Product'}, inplace=True)
        title = "Total Sales per Product"
    elif report_type == 'region_sales':
        # This part assumes a 'Region' column would exist if region reports were enabled.
        # For now, it will print an error as the user indicated no 'Region' column.
        print("Error: 'Region' column not found in data. Cannot generate region sales report.")
        return
    elif report_type == 'top_products':
        report = df.groupby(product_col)[sales_col].sum().sort_values(ascending=False).reset_index()
        report.rename(columns={sales_col: 'Total Sales', product_col: 'Product'}, inplace=True)
        title = "Top Selling Products"
    else:
        print("Invalid report type. Choose from 'product_sales', 'region_sales', 'top_products'.")
        return

    if output_file:
        report.to_csv(output_file, index=False)
        print(f"Report saved to {output_file}")
    else:
        print(f"\n--- {title} ---")
        print(report)

if __name__ == "__main__":
    # Ask the user for the CSV file path
    file_path = input("Please enter the path to your sales data CSV file: ")
    product_column = input("Please enter the name of the Product Name column (e.g., 'Product Name'): ")
    sales_column = input("Please enter the name of the Sales Value column (e.g., 'Unit Price ($)'): ")

    print("--- Product Sales Report ---")
    generate_sales_report(file_path, 'product_sales', product_col=product_column, sales_col=sales_column)

    print("\n--- Top Products Report ---")
    generate_sales_report(file_path, 'top_products', product_col=product_column, sales_col=sales_column)

    output_file_product_sales = input("\nEnter a filename to save the Product Sales Report (e.g., product_sales_report.csv), or leave blank to skip saving: ")
    if output_file_product_sales:
        generate_sales_report(file_path, 'product_sales', output_file_product_sales, product_col=product_column, sales_col=sales_column)

    output_file_top_products = input("Enter a filename to save the Top Products Report (e.g., top_products_report.csv), or leave blank to skip saving: ")
    if output_file_top_products:
        generate_sales_report(file_path, 'top_products', output_file_top_products, product_col=product_column, sales_col=sales_column)