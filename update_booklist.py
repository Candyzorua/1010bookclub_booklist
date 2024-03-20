import argparse
import csv

OUTPUT_FILE_NAME = "README.md"

"""
Parses csv file and sorts alphabetically by title
"""
def process_csv_file(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        data = sorted(reader, key=lambda row: row['Title'])
        return data

"""
Generate markdown for table
"""
def generate_markdown_with_code_table(output_file, data):
    with open(output_file, 'w') as outfile:
        # Write the Markdown header
        outfile.write("# Booklist\n\n")
        
        # Write the table header
        outfile.write("| Title | Author |\n")
        outfile.write("|-------|--------|\n")

        # Write each row of data
        for row in data:
            outfile.write(f"| `{row['Title']}` | {row['Author']} |\n")
            

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process a CSV file.')
    parser.add_argument('file_path', type=str, help='Path to the CSV file')
    args = parser.parse_args()

    data = process_csv_file(args.file_path)
    generate_markdown_with_code_table(OUTPUT_FILE_NAME, data)
    