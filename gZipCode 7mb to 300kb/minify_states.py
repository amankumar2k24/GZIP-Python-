# import json

# # File paths
# input_file = 'state.json'       # Your original JSON file
# output_file = 'newState.json'    # Minified output file

# # Step 1: Load the original JSON
# with open(input_file, 'r', encoding='utf-8') as f:
#     data = json.load(f)

# # Step 2: Write a minified version (no whitespace, indentation, or newlines)
# with open(output_file, 'w', encoding='utf-8') as f:
#     json.dump(data, f, separators=(',', ':'))

# print(f"Minified JSON saved as '{output_file}'")


# gZip code  || compressed ZIp file
import json
import gzip

input_file = 'states.json'
output_file = 'newState.json.gz'

# Load and minify the JSON
with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Save as gzip compressed JSON (minified)
with gzip.open(output_file, 'wt', encoding='utf-8') as gz:
    json.dump(data, gz, separators=(',', ':'))

print(f"✅ Compressed JSON saved as '{output_file}'")
