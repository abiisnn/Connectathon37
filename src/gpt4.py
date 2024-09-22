# docs: https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/chatgpt?tabs=python-new
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AzureOpenAI

# JSON data
json_data = '''
{
    "resourceType": "AllergyIntolerance",
    "id": "example",
    "identifier": [
      {
        "system": "http://example.org/identifiers",
        "value": "12345"
      }
    ],
    "clinicalStatus": "active",
    "verificationStatus": "confirmed",
    "type": "allergy",
    "category": [
      "food"
    ],
    "criticality": "high",
    "code": {
      "coding": [
        {
          "system": "http://snomed.info/sct",
          "code": "195967001",
          "display": "Cashew nut"
        }
      ]
    },
    "patient": {
      "reference": "Patient/example"
    },
    "onsetDateTime": "2023-01-01T00:00:00Z",
    "recordedDate": "2023-01-02T00:00:00Z",
    "note": [
      {
        "text": "Patient has a severe allergy to cashew nuts."
      }
    ]
  }
  
  {
    "resourceType": "AllergyIntolerance",
    "id": "example2",
    "clinicalStatus": {
      "coding": [
        {
          "system": "http://terminology.hl7.org/CodeSystem/allergyintolerance-clinical",
          "code": "active"
        }
      ]
    },
    "verificationStatus": {
      "coding": [
        {
          "system": "http://terminology.hl7.org/CodeSystem/allergyintolerance-verification",
          "code": "confirmed"
        }
      ]
    },
    "type": "allergy",
    "category": [
      "medication"
    ],
    "criticality": "high",
    "code": {
      "coding": [
        {
          "system": "http://snomed.info/sct",
          "code": "372756007",
          "display": "Aspirin"
        }
      ]
    },
    "patient": {
      "reference": "Patient/example"
    },
    "reaction": [
      {
        "manifestation": [
          {
            "coding": [
              {
                "system": "http://snomed.info/sct",
                "code": "39579001",
                "display": "Anaphylaxis"
              }
            ]
          }
        ]
      }
    ]
  }
'''

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
)

client = AzureOpenAI(
    api_version="2024-02-15-preview",
    azure_endpoint="https://abigailnopenai.openai.azure.com/",
    azure_ad_token_provider=token_provider
)

# Prepare the input text for the model
input_text = "Can you summarize in small paragraph per each allergy?:\n" + json_data

# Call the Azure OpenAI API to summarize the text
response = client.chat.completions.create(
    model="gpt4", # model = "deployment_name".
    messages=[
        {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
        {"role": "user", "content": input_text}
    ]
)

print(response)
print(response.model_dump_json(indent=2))
print(response.choices[0].message.content)