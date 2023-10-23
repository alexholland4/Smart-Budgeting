# Script to take in raw transaction export file from Bank, clean it, and split it into Credit and Debit transactions

import pandas as pd

# Step 1: Read the Excel file into a DataFrame
file_path = ''  # Replace with the actual path to your Excel file
df = pd.read_excel(file_path)
print('Original File Read In')
clean_df = df.drop(columns=['Account Number', 'Check', 'Status', 'Balance'], axis=1, errors='ignore') # Change to columns you want to drop

# Step 2: Create separate DataFrames for 'Debit' and 'Credit'
debit_df = clean_df[clean_df['Debit'].notna()]
credit_df = clean_df[clean_df['Credit'].notna()]

# Step 3: Remove unnecessary columns from DataFrames
credit_df = credit_df.drop(columns=['Debit'])
debit_df = debit_df.drop(columns=['Credit'])

# Step 4: Save the separate DataFrames to new Excel files
debit_df.to_excel('checkings_debit_transactions.xlsx', index=False)
print('Debit File Created')
credit_df.to_excel('checkings_credit_transactions.xlsx', index=False)
print('Credit File Created')
