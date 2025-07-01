import base64
import json
from google.cloud import storage
from datetime import datetime

def export_event(event, context):
    storage_client = storage.Client()
    bucket_name = 'shopsphere-data-lake'  # Replace with your actual bucket name
    bucket = storage_client.bucket(bucket_name)

    if 'data' in event:
        pubsub_message = base64.b64decode(event['data']).decode('utf-8')
        message_json = json.loads(pubsub_message)

        # Add current UTC timestamp inside the JSON
        message_json['event_timestamp'] = datetime.utcnow().isoformat()

        blob_name = f'events/event_{datetime.utcnow().strftime("%Y%m%dT%H%M%S")}.json'
        blob = bucket.blob(blob_name)

        # Upload the modified JSON with timestamp
        blob.upload_from_string(json.dumps(message_json), content_type='application/json')

        print(f"Event written to GCS with timestamp: {blob_name}")
    else:
        print('No data found in event')
