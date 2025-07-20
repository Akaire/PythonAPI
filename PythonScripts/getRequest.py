import requests

url = "https://apichallenges.eviltester.com/sim/entities"

response = requests.get(url)

if response.status_code == 200:
  data = response.json()

  entities = data.get('entities', [])

 # ordenação dos dados por ID
  entities_sorted = sorted(entities, key=lambda x: x["id"])

 # print dos dados ordenados
  for entity in entities_sorted:
    print(f"ID: {entity['id']} | Nome: {entity.get('name', 'N/A')} | Descrição: {entity.get('description', 'N/A')}")