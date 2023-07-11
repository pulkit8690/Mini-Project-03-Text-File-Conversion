import csv
import json

def csv_to_json(csv_file, json_file):
    # Read the CSV file
    with open(csv_file, 'r') as file:
        csv_data = csv.DictReader(file)
        
        # Convert CSV data to a list of dictionaries
        data_list = []
        for row in csv_data:
            data_list.append(row)
    
    # Write the JSON file
    with open(json_file, 'w') as file:
        json.dump(data_list, file, indent=4)

# Provide the file paths
csv_file_path = 'annual-enterprise-survey-2021-financial-year-provisional-csv.csv'
json_file_path = 'output.json'

# Convert CSV to JSON
csv_to_json(csv_file_path, json_file_path)

print("Conversion completed successfully!")
