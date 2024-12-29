def clean_file(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            # Read the content of the file
            content = infile.readlines()
        
        # Process the content to remove spaces, dollar signs, and tabs
        cleaned_content = [line.replace(" ", "").replace("$", "").replace("\t", "") for line in content]
        
        # Write the cleaned content to a new file
        with open(output_file, 'w') as outfile:
            outfile.writelines(cleaned_content)
        
        print(f"File processed successfully. Cleaned file saved as: {output_file}")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage example
input_file = "income.txt"  # Replace with your input file name
output_file = "income_clean.txt"  # Replace with your desired output file name

clean_file(input_file, output_file)
