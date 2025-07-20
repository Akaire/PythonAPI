import requests

url = "https://apichallenges.eviltester.com/sim/entities"

 # request post
response = requests.post(
    url,
    json={"name": "New Entity", "description": "This is a new entity"}
)

if response.status_code == 201:
    data = response.json()
    print(f"Entity created with ID: {data.get('id', 'N/A')}")
