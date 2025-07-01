import base64
import json
from google.cloud import firestore

def process_event(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic."""
    try:
        # Decode the Pub/Sub message
        pubsub_message = base64.b64decode(event['data']).decode('utf-8')
        print(f"Received message: {pubsub_message}")

        # Parse the JSON payload
        data = json.loads(pubsub_message)

        # Initialize Firestore
        db = firestore.Client()

        # Write to Firestore collection
        doc_ref = db.collection('sales_events').document()
        doc_ref.set(data)

        print("Data written to Firestore successfully.")

    except Exception as e:
        print(f"Error processing event: {str(e)}")
