import pandas as pd
import os

def split_csv(input_file, output_dir, max_rows=99):
    # Load the CSV file
    df = pd.read_csv(input_file)

    # Remove the header
    df = df.iloc[1:]

    # Replace entire Column A with "TWITTER"
    df.iloc[:, 0] = "TWITTER"

    # Keep only columns A and C
    df = df.iloc[:, [0, 2]]

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Split into multiple CSV files
    num_files = len(df) // max_rows + 1
    for i in range(num_files):
        start_idx = i * max_rows
        end_idx = min((i + 1) * max_rows, len(df))
        output_file = os.path.join(output_dir, f"output_{i+1}.csv")
        df[start_idx:end_idx].to_csv(output_file, index=False, header=False)

# Usage
input_file = "input.csv"
output_dir = "output"

split_csv(input_file, output_dir)
