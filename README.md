SALES DATA ANALYZER APP:
-
Description:
-
Sales Data Analyzer is an interactive web app built with Streamlit that allows users to analyze,
visualize, and manage sales data. It simulates a 30-day sales dataset for different products, lets
users add new sales entries, and provides insightful analytics such as total revenue, average sales,
and best-selling products, along with clear visualizations.

Features:
-
-Simulates 30 days of sales data for multiple products.
-Add new sales entries dynamically.
-Reset data to original simulated values.
-Displays tabular sales data with highlights.
-Shows key analytics: total revenue, average sales, best-selling product.
-Visualizes daily sales trends and total sales by product with graphs.

Technologies Used:
-
-Python
-Streamlit (for interactive UI)
-Pandas (for data handling)
-NumPy (for data generation)
-Matplotlib (for plotting charts)

Installation (Terminal):
-
1. Clone the repository:

git clone https://github.com/yasminsheikh3125/sales-analyzer-app.git
cd sales-data-analyzer

2. Create and activate a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install required packages:

pip install -r requirements.txt
OR
pip install streamlit pandas numpy matplotlib

Usage:
-
Run the app locally with:
streamlit run app.py

Once the app launches in your browser, you can:
-View and interact with the initial sales data
-Add new sales entries using the form
-Reset the data to original simulated values
-Explore analytics and visual sales trends

License:
-
This project is licensed under the MIT License — see the LICENSE file for details.
