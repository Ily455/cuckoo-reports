import json

# Read JSON data from a file
with open('F:/cuckoo/16/reports/report.json', 'r') as file:
    json_data = json.load(file)

# Extract the "data" object from the JSON
extracted_object = json_data["behavior"]["processes"][1]["calls"]

# Print the extracted "data" object
# print("Person Object:", extracted_object)

output_filename = 'F:/cuckoo/16/reports/extracted_data.json'
with open(output_filename, 'w') as output_file:
    json.dump(extracted_object, output_file, indent=4)
