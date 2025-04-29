import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        response_json = response.json()
        
        if 'emotionPredictions' in response_json:
            emotions = response_json['emotionPredictions'][0]['emotion']
            # Extract and format emotions
            return json.dumps(emotions, indent=4)
        else:
            return "No emotions detected."
    else:
        return f"Error: {response.status_code}, {response.text}"
