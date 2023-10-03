# Copyright (c) 2023, shuvo and contributors
# For license information, please see license.txt

import frappe
import googlemaps
import requests
from frappe.model.document import Document

class MyMaps(Document):
	pass
	

# Define the API endpoint URL
api_url = "https://maps.googleapis.com/maps/api/place/autocomplete/json"
url = "https://maps.googleapis.com/maps/api/js?key=YourKey&libraries=places"

# Define your API key (replace with your actual API key)
api_key = Your Key

# Define the parameters for your request


# Make a GET request to the API
@frappe.whitelist()
def get_response(user_inputs=None):
	params = {
    "input": user_inputs,
    "types": "establishment",
    "key": api_key
	}
	response = requests.get(api_url, params = params)
	data = response.json()
	names = []
	for prediction in data["predictions"]:
        # Access the road name from the structured_formatting dictionary
		road_name = prediction["description"]
		names.append(road_name)
	print(names)
	return names

