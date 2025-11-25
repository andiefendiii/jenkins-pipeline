import requests
import pytest
import json
import jsonpath
import random
import os
from pathlib import Path
import requests
import allure



baseUrl = "https://reqres.in/"

#### Example code ####

@allure.feature("Products API")
@allure.story("Get Product List")
@allure.title("Get Product List Hepi flow dah")
@allure.description("Memastikan GET /products mengembalikan daftar produk dengan response 200 dan struktur JSON yang valid.")
@allure.severity(allure.severity_level.CRITICAL)
def test_list_user():
    global tokenLogin
   
    path ="api/users?page=2"
    headers = {
        'Content-Type':'application/json'
        } 
    with allure.step(f"Kirim request GET ke {baseUrl} pake params {headers}"):
        response = requests.get(url=baseUrl+path, headers=headers)

    with allure.step("Validasi status code 200"):    
        assert response.status_code == 200
        
    print(response.text)