import json
import requests;

# This script fetches a post from a JSON placeholder API and prints its details.
# Get operation
url ="https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)
data = response.json()

# data manipulattion operation
for key, value in data.items():
    print(f"{key}: {value}")

# Print the entire JSON response in a pretty format
print("Response from GET request:")
print(json.dumps(data, indent=4))

if response.status_code == 200:
    data = response.json()
    print("Title:", data['title'])
    print("Body:", data['body'])
else:
    print("Error:", response.status_code)
    print("Message:", response.text)


# Post operation
# This script creates a new post using the JSON placeholder API and prints the response.
payload = {
    "title": "foo", "body": "bar", "userId": 1}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
if response.status_code == 201:
    print("Post created successfully.")
    print("Response:", response.json())

print(data)




