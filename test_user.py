import requests
import pytest
import json
import jsonpath
import random
import os
from pathlib import Path




baseUrl = "https://reqres.in/"

#### Example code ####
def test_list_user():
    global tokenLogin
   
    path ="api/users?page=2"
    headers = {
        'Content-Type':'application/json'
        } 
    
    response = requests.get(url=baseUrl+path, headers=headers)
    assert response.status_code == 200
    print(response.text)