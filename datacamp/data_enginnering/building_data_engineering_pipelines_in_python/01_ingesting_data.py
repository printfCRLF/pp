import json 
import pprint 

database_address = {
  "host": "10.0.0.5",
  "port": 8456
}

# Open the configuration file in writable mode
with open("database_config.json", "w") as fh:
  # Serialize the object in this file handle
  json.dump(obj=database_address, fp=fh) 

# Complete the JSON schema
schema = {'properties': {
    'brand': {'type': 'string'},
    'model': {'type': 'string'},
    'price': {'type': 'number'},
    'currency': {'type': 'string'},
    'quantity': {'type': 'number', 'minimum': 1},  
    'date': {'type': 'string', 'format': 'date'},
    'countrycode': {'type': 'string', 'pattern': "^[A-Z]{2}$"}, 
    'store_name': {'type': 'string'}}}

# Write the schema
singer.write_schema(stream_name='products', schema=schema, key_properties=[])

def communicating_with_an_api(): 
    endpoint = "http://localhost:5000"

    # Fill in the correct API key
    api_key = "scientist007"

    # Create the web API’s URL
    authenticated_endpoint = "{}/{}".format(endpoint, api_key)

    # Get the web API’s reply to the endpoint
    api_response = requests.get(authenticated_endpoint).json()
    pprint.pprint(api_response)

    # Create the API’s endpoint for the shops
    shops_endpoint = "{}/{}/{}/{}".format(endpoint, api_key, "diaper/api/v1.0", "shops")
    shops = requests.get(shops_endpoint).json()
    print(shops)