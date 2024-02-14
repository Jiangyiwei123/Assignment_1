import pandas as pd
import sys

def clean_data(input1, input2, output):
    # Step 1: Merge the two input data files based on the ID value
    data1 = pd.read_csv('respondent_contact.csv')
    data2 = pd.read_csv('respondent_other.csv')
    merged_data = pd.merge(data1, data2, on='respondent_id')

    # Step 2: Drop any rows with missing values
    merged_data = merged_data.dropna()

    # Step 3: Drop any rows if their job value contains 'insurance' or 'Insurance'
    merged_data = merged_data[~merged_data['job'].str.contains('insurance|Insurance')]

    # Step 4: Save the cleaned data to the specified output file
    merged_data.to_csv(output, index=False)
    print(f"Cleaned data saved to {output}")


if __name__ == "__main__":
    # Check if all 3 required arguments are provided
    if len(sys.argv) != 4:
        print("Please provide 3 required arguments: input1, input2, and output")
        sys.exit(1)

    # Extract the arguments
    input1 = sys.argv[1]
    input2 = sys.argv[2]
    output = sys.argv[3]

    # Call the clean_data function with the provided arguments
    clean_data(input1, input2, output)