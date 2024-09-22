# Connectathon37
This is a playground to get summarized text given Allergies

Given a Bundle of Allergies, this script will take the active or confirmed allergies and get the summary of them.

Let say you send this:
```json
{
    "fullUrl": "https://hapi.fhir.org/baseR4/AllergyIntolerance/53342",
    "resource": {
    "resourceType": "AllergyIntolerance",
    "id": "53342",
    "meta": {
        "versionId": "1",
        "lastUpdated": "2019-11-01T21:53:29.077+00:00",
        "source": "#1l3hYmrDBOUuDZ2f"
    },
    "verificationStatus": {
        "coding": [
        {
            "system": "http://hl7.org/fhir/ValueSet/allergyintolerance-verification",
            "code": "confirmed",
            "display": "Confirmed"
        }
        ],
        "text": " AllergyIntoleranceVerificationStatusCodes"
    },
    "type": "allergy",
    "code": {
        "coding": [
        {
            "system": "2.16.840.1.113883.6.96",
            "code": "419511003",
            "display": "Propensity to adverse reaction to drug"
        }
        ]
    },
    "patient": {
        "reference": "Patient/53373",
        "type": "Patient"
    },
    "onsetPeriod": {
        "start": "1980-05-01"
    },
    "reaction": [
        {
        "substance": {
            "coding": [
            {
                "system": "2.16.840.1.113883.6.88",
                "code": "81953",
                "display": "Ampicillin"
            }
            ]
        },
        "manifestation": [
            {
            "coding": [
                {
                "system": "2.16.840.1.113883.6.96",
                "code": "247472004",
                "display": "Hives"
                }
            ]
            }
        ]
        }
    ]
    },
    "search": {
    "mode": "match"
    }
}
```
Then, using Chatgp4 youw will get:

**The patient has a confirmed allergy to the drug Ampicillin, which is associated with a propensity for adverse reactions. This allergic reaction specifically manifests as hives, indicating an immune response that results in an itchy, bumpy rash on the skin.**