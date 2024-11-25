import json
import os

# Define the path to the JSON file
json_file_path = 'data/schacon.repos.json'

# Check if the file exists
if not os.path.exists(json_file_path):
    print(f"Error: The file {json_file_path} does not exist.")
    exit(1)

# Open and load the JSON data
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Now you can work with the data
# For example, printing the entire data or just a specific part

# Let's print out the first few repositories (or all of them)
print("Repository Data:")
for repo in data[:5]:  # Assuming `data` is a list of repositories
    print(f"- {repo.get('name', 'Unknown name')}: {repo.get('html_url', 'No URL')}")


