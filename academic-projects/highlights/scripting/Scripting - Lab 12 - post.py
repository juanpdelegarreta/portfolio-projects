import requests

api_endpoint="https://reqres.in/api/users"
response = requests.post(api_endpoint,data={"name":"John Doe","job":"Private Detective"})
if response.status_code == 201:
    print(response.text)
else:
    print(f"API call failed with reason: {response.reason}")
