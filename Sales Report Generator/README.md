# Sales Report Generator

## Concepts
This project utilizes Python's `pandas` library for data manipulation and analysis. Key concepts include:

*   **CSV Reading/Writing:** Efficiently importing data from and exporting reports to CSV files.
*   **Data Aggregation:** Using `groupby()`, `sum()`, and `sort_values()` for calculating total sales per product and identifying top-selling products.
*   **Basic Data Analysis:** Performing fundamental data aggregation operations.

## Description
This script reads a CSV file containing sales data and generates various reports based on the user's input. It can calculate total sales per product and identify top-selling products. The results can either be printed to the console or saved to a new CSV file.

## How to Use

1.  **Prerequisites:**
    *   Ensure you have Python installed.
    *   Install the `pandas` library: `pip install pandas`

2.  **Place your CSV file:** Put your sales data CSV file in a location accessible by the script. When prompted, you will provide the full path to this file.

3.  **Run the script:**
    Navigate to the `Sales Report Generator` directory in your terminal:
    ```bash
    cd "D:\Data Analyst\Project\Sales Report Generator"
    ```
    Then, run the script:
    ```bash
    python main.py
    ```

4.  **Follow the prompts:**
    The script will ask you for:
    *   The path to your sales data CSV file (e.g., `D:\Games\Products.csv`).
    *   The exact name of the **Product Name column** (e.g., `Product Name`).
    *   The exact name of the **Sales Value column** (e.g., `Unit Price ($)`).

    After displaying the reports in the console, it will ask if you want to save the Product Sales Report and Top Products Report to separate CSV files. Enter a filename (e.g., `product_sales.csv`) or leave blank to skip.

## Example Usage (with example prompts)

```
python main.py
Please enter the path to your sales data CSV file: D:\Games\Products.csv
Please enter the name of the Product Name column (e.g., 'Product Name'): Product Name
Please enter the name of the Sales Value column (e.g., 'Unit Price ($)'): Unit Price ($)

--- Product Sales Report ---
# ... (product sales report output)

--- Top Products Report ---
# ... (top products report output)

Enter a filename to save the Product Sales Report (e.g., product_sales_report.csv), or leave blank to skip saving: product_report.csv
Report saved to product_report.csv
Enter a filename to save the Top Products Report (e.g., top_products_report.csv), or leave blank to skip saving: top_products.csv
Report saved to top_products.csv
```

## Enhancements (Future Possibilities)

*   **Handle Dates:** Implement logic to analyze sales trends over time using a 'Date' column.
*   **Calculate Profit Margins:** If 'Cost' and 'Selling Price' columns are available, calculate profit margins.
*   **More Complex Filtering:** Add options for users to filter data based on various criteria (e.g., sales within a specific date range, products above a certain sales value).
*   **Region Sales Report:** If a 'Region' or 'Location' column is available, add functionality to generate sales reports per region.