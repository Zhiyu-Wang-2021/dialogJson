import json

import data
from data import *


# "intents":[
#     {
#         "intent": "business_address",
#         "examples":
#         [
#             {
#                 "text": "What is the address of your @business ?"
#             }, ...
#         ],
#         "description": "Addresses for the business"
#     }, ...
# ],
def intents():
    result = [
        intent(
            "hours_info",
            IntentExamples.hour_info
        ),
        intent(
            "location_info",
            IntentExamples.location_info
        )
    ]
    return '"intents": ' + json.dumps(result) + ','


def intent(name, examples, description='-'):
    return {
        "intent": name,
        "examples": list(map(lambda s: {
            "text": s
        }, examples)),
        "description": description
    }


# "entities": [
#     {
#         "entity": "business",
#         "values": [
#             {
#                 "type": "synonyms",
#                 "value": "business",
#                 "synonyms":[
#                     "agency",
#                     "bureau",
#                     "firm",
#                     "office",
#                     "shop"
#                 ]
#             }
#         ],
#         "fuzzy_match": true
#     }
# ],
def entities():
    result = [
        entity(
            "uk_location",
            data.EntityValues.location,
        )
    ]
    return '"entities": ' + json.dumps(result) + ','


def entity(name, values, fuzzy_match=True):
    return {
        "entity": name,
        "values": list(map(lambda location_tuple: {
            "type": "synonyms",
            "value": location_tuple[0],
            "synonyms": location_tuple[1]
        }, values)),
        "fuzzy_match": fuzzy_match
    }


# "dialog_nodes": [{
#     "type": "standard",
#     "title": "Business address",
#     "output": {
#         "generic": [
#             {
#             "values": [
#                 {
#                     "text": "Our business is located in ‘Watson Square 5, NY 10040’ and ‘Discovery Avenue, AZ 85010′"
#                 }
#             ],
#             "response_type": "text",
#                 "selection_policy": "sequential"
#             }
#         ]
#     },
#     "conditions": "#business_address",
#     "dialog_node": "Business_Address",
#     "previous_sibling": "Welcome"
# }, ...],
def dialog_nodes():
    result = [
        welcome_node(),
        dialog_node(
            "Location Info", "You are here", "#location_info", "Welcome"
        ),
        dialog_node(
            "Hours Info", "It's time", "#hours_info", "Location Info"
        ),
        else_node("Hours Info")
    ]
    return '"dialog_nodes": ' + json.dumps(result) + ','


def dialog_node(reference, output, condition, previous_sibling, node_type='standard'):
    return {
        "type": node_type,
        "title": reference,
        "output": {
            "generic": [
                {
                    "values": [
                        {
                            "text": output
                        }
                    ],
                    "response_type": "text",
                    "selection_policy": "sequential"
                }
            ]
        },
        "conditions": condition,
        "dialog_node": reference,
        "previous_sibling": previous_sibling
    }


def welcome_node(greeting="Hello, how can I help you?"):
    return {
        "type": "standard",
        "title": "Welcome",
        "output": {
            "generic": [
                {
                    "values": [
                        {
                            "text": greeting
                        }
                    ],
                    "response_type": "text",
                    "selection_policy": "sequential"
                }
            ]
        },
        "conditions": "welcome",
        "dialog_node": "Welcome"
    }


def else_node(previous_sibling, response="Can you reword your statement? I'm not understanding."):
    return {
        "type": "standard",
        "title": "Anything else",
        "output": {
            "generic": [
                {
                    "values": [
                        {
                            "text": response
                        },
                    ],
                    "response_type": "text",
                    "selection_policy": "sequential"
                }
            ]
        },
        "conditions": "anything_else",
        "dialog_node": "Anything else",
        "previous_sibling": previous_sibling,
        "disambiguation_opt_out": True
    }


def other():
    return """
            "metadata": {
            "api_version": {
              "major_version": "v2",
              "minor_version": "2021-11-27"
            }
            },
            "counterexamples": [],
            "system_settings": {
            "nlp": {
              "model": "latest"
            },
            "off_topic": {
              "enabled": true
            },
            "disambiguation": {
              "prompt": "Did you mean:",
              "enabled": false,
              "randomize": true,
              "max_suggestions": 5,
              "suggestion_text_policy": "title",
              "none_of_the_above_prompt": "None of the above"
            },
            "system_entities": {
              "enabled": true
            },
            "human_agent_assist": {
              "prompt": "Did you mean:"
            },
            "spelling_auto_correct": true
            },
            "learning_opt_out": false,
            "name": "Generated Skill",
            "language": "en",
            "description": ""
        """.replace("\n", '').replace(" ", "")


#
def get_json():
    with open("chatbot.json", "w") as f:
        f.write("{" + intents() + entities() + dialog_nodes() + other() + "}")
        print('json generated')
        return 'success'
