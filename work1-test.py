# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 10:45:40 2023

@author: yardi
"""

import pytest

def transform_data(people_data):
    # I transformed "Contact" object schema
    contacts = list()
    for person in people_data:
        first_name = person['fields']['firstName'].strip()
        last_name = person['fields']['lastName'].strip()
        birthdate = person['fields']['dateOfBirth']
        email = person['fields']['email']
        lifetime_value = float(person['fields']['lifetimeValue'][1:])

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
    return contacts

def test_transform_data():
    people_data = [{
        "id": "person_1",
        "fields": {
          "firstName": "  John  ",
          "lastName": "Doe",
          "dateOfBirth": "01-01-2000",
          "email": "john.doe@example.com",
          "lifetimeValue": "$100.00"
        }
    }]
    expected_output = [{
        "first_name": "John",
        "last_name": "Doe",
        "birthdate": "01-01-2000",
        "email": "john.doe@example.com",
        "custom_properties": {
            "airtable_id": "person_1",
            "lifetime_value": 100.0
        }
    }]
    assert transform_data(people_data) == expected_output

if __name__ == '__main__':
    pytest.main()