# Flask web app to easily label transactions as Categories

from flask import Flask, render_template, request
import pandas as pd
import openpyxl

app = Flask(__name__)

# Load the data from the spreadsheet into a Pandas DataFrame
file_path = '' # Replace with the actual path to your Excel file
df = pd.read_excel(file_path)

# Initialize a variable to keep track of the current row index
current_row = 0

@app.route('/', methods=['GET', 'POST'])
def label_data():
    global current_row

    if request.method == 'POST':
        category = request.form['category']
        # Update the "Category" column in the DataFrame with the selected category
        df.at[current_row, 'Category'] = category
        df.to_excel(file_path, index=False)  # Save the changes to the spreadsheet
        current_row += 1  # Move to the next row

    if current_row < len(df):
        row_data = df.at[current_row, 'Description']
        post_date = df.at[current_row, 'Post Date']
        amount = df.at[current_row, 'Credit']

        return render_template('template.html', row_data=row_data, post_date=post_date, amount=amount)
    else:
        return "All rows have been labeled."

if __name__ == '__main__':
    app.run(debug=True)
