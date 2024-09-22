import requests

print("Sending request")
# Set your endpoint and key
endpoint = "https://connectathontest.cognitiveservices.azure.com/"
api_key = "88793b6497cb401989ce3110810301fa"

url = "https://connectathontest.cognitiveservices.azure.com/language/analyze-text/jobs?api-version=2023-04-01"
headers = {
    "Content-Type": "application/json",
    "Ocp-Apim-Subscription-Key": "88793b6497cb401989ce3110810301fa"
}
data = {
    "displayName": "Text Extractive Summarization Task Example",
    "analysisInput": {
        "documents": [
            {
                "id": "1",
                "language": "en",
                "text": "allergy - medication - Criticality: High, Substance with penicillin structure and antibacterial mechanism of action (substance) (373270004). - - Criticality: undefined undefined (no-known-food-allergies)"
            }
        ]
    },
    "tasks": [
        {
            "kind": "AbstractiveSummarization",
            "taskName": "Query-based Abstractive Summarization",
            "parameters": {
                "query": "XYZ-code",
                "summaryLength": "short"
            }
        }
    ]
}

response = requests.post(url, headers=headers, json=data)
responseText = response.text
size = len(responseText)
print(response.headers)
print(type(response.headers))
print(response.headers['operation-location'])

# get response
url = response.headers['operation-location']
headers = {
    "Ocp-Apim-Subscription-Key": "88793b6497cb401989ce3110810301fa"
}
response = requests.get(url, headers=headers, json=data)
print(response.json())

#https://connectathontest.cognitiveservices.azure.com/language/analyze-text/jobs/76df4e98-fda4-499e-b28d-f74c6427213b?api-version=2023-04-01