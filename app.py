import argparse
import requests
import json

TYPESENSE_SERVER = 'http://localhost:8108'
API_KEY = 'your_api_key'
HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {API_KEY}'
}

def create_schema(schema_name, fields):
    schema_definition = {
        'name': schema_name,
        'fields': fields
    }
    
    response = requests.post(f'{TYPESENSE_SERVER}/schemas', headers=HEADERS, json=schema_definition)
    print(response.text)

def delete_schema(schema_name):
    response = requests.delete(f'{TYPESENSE_SERVER}/schemas/{schema_name}', headers=HEADERS)
    print(response.text)

def populate_data(schema_name, data):
    response = requests.post(f'{TYPESENSE_SERVER}/collections/{schema_name}/documents', headers=HEADERS, json=data)
    print(response.text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Interact with TypeSense')
    parser.add_argument('action', choices=['create', 'delete', 'populate'], help='Action to perform')
    parser.add_argument('schema', help='Schema or collection name')
    args = parser.parse_args()
    
    if args.action == 'create':
        # Define schema and field definitions
        fields = [
            {'name': 'id', 'type': 'string', 'facet': False},
            {'name': 'name', 'type': 'string', 'facet': False},
            {'name': 'price', 'type': 'float', 'facet': False},
            # Add more fields here as needed
        ]
        create_schema(args.schema, fields)
    elif args.action == 'delete':
        delete_schema(args.schema)
    elif args.action == 'populate':
        # Sample data to populate
        sample_data = [
            {'id': '1', 'name': 'Product A', 'price': 19.99},
            {'id': '2', 'name': 'Product B', 'price': 29.99},
            # Add more data entries here as needed
        ]
        populate_data(args.schema, sample_data)
