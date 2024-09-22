import AllergyConstants
import VerificationStatusConstants
import ClinicalStatusConstants
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AzureOpenAI

def isClinicalStatusActive(allergy):
    if AllergyConstants.CLINICAL_STATUS in allergy:
        if AllergyConstants.CODING in allergy[AllergyConstants.CLINICAL_STATUS]:
            if len(allergy[AllergyConstants.CLINICAL_STATUS][AllergyConstants.CODING]) >= 1:
                if ClinicalStatusConstants.ACTIVE == allergy[AllergyConstants.CLINICAL_STATUS][AllergyConstants.CODING][0] :
                    return True
    return False

def isVerifiedOrPresumedOrUnconfirmed(allergy):
    if AllergyConstants.VERIFICATION_STATUS in allergy:
        if AllergyConstants.CODING in allergy[AllergyConstants.VERIFICATION_STATUS]:
            if len(allergy[AllergyConstants.VERIFICATION_STATUS][AllergyConstants.CODING]) >= 0:
                if AllergyConstants.CODE in allergy[AllergyConstants.VERIFICATION_STATUS][AllergyConstants.CODING][0]:
                    if VerificationStatusConstants.CONFIRMED == allergy[AllergyConstants.VERIFICATION_STATUS][AllergyConstants.CODING][0][AllergyConstants.CODE] or \
                        VerificationStatusConstants.PRESUMED == allergy[AllergyConstants.VERIFICATION_STATUS][AllergyConstants.CODING][0][AllergyConstants.CODE] or \
                                VerificationStatusConstants.UNCONFIRMED == allergy[AllergyConstants.VERIFICATION_STATUS][AllergyConstants.CODING][0][AllergyConstants.CODE] :
                                    return True
    return False

def isElegibleAlergy(allergyResource):
    return isClinicalStatusActive(allergyResource) or isVerifiedOrPresumedOrUnconfirmed(allergyResource)

# New section

def getResourceType(allergy):
    if AllergyConstants.RESOURCE_TYPE in allergy:
        return f"{{{AllergyConstants.RESOURCE_TYPE}: {allergy[AllergyConstants.RESOURCE_TYPE]}}}"
    return ""

def getClinicalStatus(allergy):
    if AllergyConstants.CLINICAL_STATUS in allergy:
        return f"{{{AllergyConstants.CLINICAL_STATUS}: {allergy[AllergyConstants.CLINICAL_STATUS]}}}"
    return ""

def getVerificationStatus(allergy):
    if AllergyConstants.VERIFICATION_STATUS in allergy:
        return f"{{{AllergyConstants.VERIFICATION_STATUS}: {allergy[AllergyConstants.VERIFICATION_STATUS]}}}"
    return ""

def getCategory(allergy):
    if AllergyConstants.CATEGORY in allergy:
        return f"{{{AllergyConstants.CATEGORY}: {allergy[AllergyConstants.CATEGORY]}}}"
    return ""

def getCriticality(allergy):
    if AllergyConstants.CRITICALITY in allergy:
        return f"{{{AllergyConstants.CRITICALITY}: {allergy[AllergyConstants.CRITICALITY]}}}"
    return ""

def getCode(allergy):
    if AllergyConstants.CODE in allergy:
        return f"{{{AllergyConstants.CODE}: {allergy[AllergyConstants.CODE]}}}"
    return ""

def getReaction(allergy):
    if AllergyConstants.REACTION in allergy:
        return f"{{{AllergyConstants.REACTION}: {allergy[AllergyConstants.REACTION]}}}"
    return ""

def getEligibleTextToGetAllergySummary(allergyResource):
    allergyText = ""
    allergyText += getResourceType(allergyResource)
    allergyText += getClinicalStatus(allergyResource)
    allergyText += getVerificationStatus(allergyResource)
    allergyText += getCategory(allergyResource)
    allergyText += getCriticality(allergyResource)
    allergyText += getCode(allergyResource)
    allergyText += getReaction(allergyResource)

    return allergyText

# Here starts main
import json

# Open and read the JSON file
with open('C:\\Connectathon37\\Samples\\AllergiesDevTest.json', 'r') as file:
    data = json.load(file)

# We just want entries
data = data["entry"]

allergiesText = ""
# Iterate over each resource in the list
for resource in data:
    print("----> Checking ")
    print(resource["fullUrl"])
    if (isElegibleAlergy(resource["resource"])):
        print("PASSED")
        allergiesText += "{" + getEligibleTextToGetAllergySummary(resource["resource"]) + "}"

print(allergiesText)

# Request
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
)

client = AzureOpenAI(
    api_version="2024-02-15-preview",
    azure_endpoint="https://abigailnopenai.openai.azure.com/",
    azure_ad_token_provider=token_provider
)

# Prepare the input text for the model
input_text = "Can you summarize in small paragraph per each allergy?:\n" + allergiesText

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