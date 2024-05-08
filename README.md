# FiveCast Onyx Mass Twitter Account Tool

## Overview

This tool is designed to assist with mass-importing important Twitter accounts into FiveCast Onyx for monitoring purposes. It takes a CSV file containing Twitter account data and splits it into multiple CSV files, each containing a maximum of 99 rows (import limit). Additionally, it performs the following operations on the data:

1. Removes the header that names each column.
2. Replaces the entire Column A with the text "TWITTER".
3. Deletes columns B, D, E, F, G, H, I, and J, leaving only columns A and C.

(This is due to the original document having the following Columns. Count, Profile_Photo, Username, UserID, Full Name, Added To List On, URL, Notes, Active, Archived. this is specific to my use case and may need to be updated for your own)

## Requirements

- Python 3.x
- pandas library (`pip install pandas`)

## Usage

1. Place your input CSV file in the same directory as the Python script.
2. Update the `input_file` variable in the script to point to your input CSV file.
3. Run the script.

## Output

The script will generate multiple output CSV files, each containing a maximum of 99 rows of data. The output filenames will follow the format `output_<sequential_number>.csv`, where `<sequential_number>` represents the order of the output files.

Each output CSV file will contain two columns:
- Column A: Contains the text "TWITTER" for each row. (This is because all accounts are on Twitter to be Mass Imported)
- Column C: Contains the text from Column C of the original CSV file.

## Example

Suppose you have an input CSV file named `input.csv` with 300 rows of Twitter account data. After running the script, it will generate four output CSV files:

- `output_1.csv` (containing rows 1-99)
- `output_2.csv` (containing rows 100-198)
- `output_3.csv` (containing rows 199-297)
- `output_4.csv` (containing rows 298-300)

## Notes

- Ensure that the input CSV file follows the specified format and does not contain any additional headers beyond the first row.
- This tool is specifically tailored for use with FiveCast Onyx and may require adjustments for use with other applications or purposes.
- Always review the output files to ensure that the data is processed correctly before importing it into FiveCast Onyx.

