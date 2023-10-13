import requests

endpoint = 'https://api.indiankanoon.org/search/'

fi = input("Enter the parameter 1 : ")
fi2 = input("Enter the parameter 2:")
header = {
    "Authorization": "Token 7f3806c7b5c89ade186c2e1df6c861d0a2e75d11"
}
parameters = {
    "formInput": fi,
    "pagenum": fi2
}
sheet_response = requests.post(
    endpoint,
    params=parameters,
    headers=header
)

print(sheet_response.json())
