import requests
import json
import webbrowser
import random

def list_breeds():
    api_endpoint = "https://dog.ceo/api/breeds/list/all"
    response = requests.get(api_endpoint)
    dog_breeds = json.loads(response.text)
    dog_breeds = list(dog_breeds["message"].keys())
    return dog_breeds


def get_random_dog_pic(breed_name):
    api_endpoint = f"https://dog.ceo/api/breed/{breed_name}/images"
    response = requests.get(api_endpoint)
    json_response = json.loads(response.text)
    choice = random.randrange(0, len(json_response["message"]))
    webbrowser.open(json_response["message"][choice])


breed_check = list_breeds()
breed = input("What breed of dog would you like to see a picture of? \n")

while breed != "quit":
    if breed.lower() in breed_check:
        get_random_dog_pic(breed.lower())
        breed = input("\nWhat breed of dog would you like to see a picture of? \nType \"quit\" to quit:\n")
    else:
        print("\nSorry, we don't have pictures of that breed. Try removing the spaces in the breed name or another breed.")
        breed = input("What breed of dog would you like to see a picture of? \nType \"quit\" to quit:\n")