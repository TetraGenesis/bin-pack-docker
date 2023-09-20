import requests
from typing import Dict, Union 

# Test newproblem endpoint
print("Testing newproblem endpoint")
api_command: str = 'newproblem'

response: requests.Response = requests.get('http://localhost:5000/'+ api_command)

jsonResponse: Dict[str, Union[int, str]] = response.json()
print(jsonResponse)

# Get the problem ID from the response
problemID: int = jsonResponse['ID']

# Test placeitem endpoint
print("Testing placeitem endpoint")
api_command: str = 'placeitem'
size: int = 10

response: requests.Response = requests.get('http://localhost:5000/'+ api_command + '/' + str(problemID) + '/' + str(size))

jsonResponse: Dict[str, Union[int, str]] = response.json()
print(jsonResponse)

print("Testing placeitem endpoint with another item")
size: int = 44

response: requests.Response = requests.get('http://localhost:5000/'+ api_command + '/' + str(problemID) + '/' + str(size))

jsonResponse: Dict[str, Union[int, str]] = response.json()
print(jsonResponse)

print("Testing placeitem endpoint with a third item too big for one bin")
size: int = 77

response: requests.Response = requests.get('http://localhost:5000/'+ api_command + '/' + str(problemID) + '/' + str(size))

jsonResponse: Dict[str, Union[int, str]] = response.json()
print(jsonResponse)

# Test placeitem endpoint with an invalid problem ID
print("Testing placeitem endpoint with an invalid problemID")
api_command: str = 'placeitem'
size: int = 10
invalidProblemID: int = 123456789

response: requests.Response = requests.get('http://localhost:5000/'+ api_command + '/' + str(invalidProblemID) + '/' + str(size))

jsonResponse: Dict[str, Union[int, str]] = response.json()
print(jsonResponse)

# Test placeitem endpoint with an invalid size
print("Testing placeitem endpoint with an invalid size")
api_command: str = 'placeitem'
size: int = 101

response: requests.Response = requests.get('http://localhost:5000/'+ api_command + '/' + str(problemID) + '/' + str(size))

jsonResponse: Dict[str, Union[int, str]] = response.json()
print(jsonResponse)

# Test endproblem endpoint
print("Testing endproblem endpoint")
api_command: str = 'endproblem'

response: requests.Response = requests.get('http://localhost:5000/'+ api_command + '/' + str(problemID))

jsonResponse: Dict[str, Union[int, str]] = response.json()
print(jsonResponse)

# Test endproblem endpoint with an invalid problem ID
print("Testing endproblem endpoint with an invalid problemID")
invalidProblemID: int = 123456789

response: requests.Response = requests.get('http://localhost:5000/'+ api_command + '/' + str(invalidProblemID))

jsonResponse: Dict[str, Union[int, str]] = response.json()
print(jsonResponse)

# Test subsequent request using placeitem on an ended problem
print("Testing placeitem endpoint on an ended problem")
api_command: str = 'placeitem'
response: requests.Response = requests.get('http://localhost:5000/'+ api_command + '/' + str(problemID) + '/' + str(size))

jsonResponse: Dict[str, Union[int, str]] = response.json()
print(jsonResponse)