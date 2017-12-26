import os

VERSION = "0.0.2"
APPLICATION_ID = os.environ.get('NOTETAKER_APPLICATION_ID')

def handle(event, context):
    user_id = event['session']['user']['userId']
    type = event['request']['type']

    if "LaunchRequest" == type:
        return handle_launch_request(event)
    elif "IntentRequest" == type:
        return handle_intent_request(event)
    elif "SessionEndedRequest" == type:
        return handle_session_ended_request(event)
    else:
        return handle_unrecognized_request(event)

def handle_launch_request(event):
    r = new_response()
    return r

def handle_intent_request(event):
    note = event['request']['intent']['slots']['note']['value']
    text = event['request']['intent']['slots']['text']['value']
    r = new_response()
    r['response'] = {
        'outputSpeech': {
            "type": "PlainText",
            "text": f"I will add {text} to the note {note}"
        }
    }
    return r

def handle_session_ended_request(event):
    pass

def handle_unrecognized_request(event):
    r = new_response()
    r['outputSpeech'] = {
        "type": "PlainText",
        "text": f"I don't understand request type {event['request']['type']}"
    }
    return r

def new_response():
    return {
        "version": VERSION,
        "response": {}
    }

