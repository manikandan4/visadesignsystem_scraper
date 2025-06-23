import json

# Path to the input JSON file
input_file_path = "input/nova-react-2.5.4.json"

# Path to the output JSON file
output_file_path = "input/pretty_printed.json"

# Read and parse the JSON file
with open(input_file_path, 'r') as file:
    data = json.load(file)

# Parse the 'body' field as JSON
if 'body' in data:
    data['body'] = json.loads(data['body'])

# Write the pretty-printed JSON to the output file
with open(output_file_path, 'w') as file:
    json.dump(data, file, indent=4)

print(f"Pretty-printed JSON has been saved to {output_file_path}")
