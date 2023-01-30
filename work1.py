# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 10:26:25 2023

@author: borucigin
"""

import requests
import pandas as pd

# GET the list of people from the API endpoint /people/
header = {'Authorization': 'Bearer fFz8Z7OpPTSY7gpAFPrWntoMuo07ACjp'}
response = requests.get('https://challenge-automation-engineer-xij5xxbepq-uc.a.run.app/people/', headers=header)
people_data = response.json()

# I transformed "Contact" object schema
contacts = list()
for person in people_data:
    first_name = person['fields']['firstName'].strip()
    last_name = person['fields']['lastName'].strip()
    birthdate = person['fields']['dateOfBirth']
    email = person['fields']['email']
    lifetime_value = float(person['fields']['lifetime_value'][1:])
    # print(first_name)#program output control
    contact = {
        "first_name": first_name,
        "last_name": last_name,
        "birthdate": birthdate,
        "email": email,
        "custom_properties": {
            "airtable_id": person['id'],
            "lifetime_value": lifetime_value
        }
    }
    contacts.append(contact)
    
# I posted each contact to the API endpoint "/contacts/"
auth = requests.auth.HTTPBasicAuth('datacose', '196D1115456D7')
for contact in contacts:
    # print(contact)#program output control
    response = requests.post('https://challenge-automation-engineer-xij5xxbepq-uc.a.run.app/contacts/', auth=auth, json=contact)
    print(response)
    if response.status_code != 200:
        print(f"Failed to POST contact: {contact}. Response: {response.text}")
    else:
        print(f"Successfully posted contact: {contact}")
