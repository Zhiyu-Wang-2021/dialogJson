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
    result_raw = [
        welcome_node(),
        dialog_node_multi_condition(
            "Location Info",
            {
                "handler": "@uk_location",
                "enter": "#location_info",
                "output": [
                    ("true", "Our store is at ..."),
                    ("$location", "Our $location store is at ...")
                ]
            },
            "$location",
            "Welcome"
        ),
        dialog_node_standard(
            "Hours Info", "It's time", "#hours_info", "Location Info"
        ),
        else_node("Hours Info")
    ]
    result = []
    for r in result_raw:
        if isinstance(r, list):
            result.extend(r)
        else:
            result.append(r)
    return '"dialog_nodes": ' + json.dumps(result) + ','


# multiple responds node
# handler -> slot
# frame
# response_condition
# {
#     "type": "event_handler",
#     "output": {},
#     "parent": "slot_handler_parent",
#     "event_name": "focus",
#     "dialog_node": "handler_focus",
#     "previous_sibling": "handler_uk_location"
# },
# {
#     "type": "event_handler",
#     "output": {},
#     "parent": "slot_handler_parent",
#     "context": {
#         "location": "@uk_location"
#     },
#     "conditions": "@uk_location",
#     "event_name": "input",
#     "dialog_node": "handler_uk_location"
# },
# {
#     "type": "slot",
#     "parent": "Location Info",
#     "variable": "$location",
#     "dialog_node": "slot_handler_parent",
#     "previous_sibling": "response_without_location"
# },
# {
#     "type": "frame",
#     "title": "Location Info",
#     "metadata": {
#         "_customization": {
#             "mcr": true
#         }
#     },
#     "conditions": "#location_info",
#     "dialog_node": "Location Info",
#     "previous_sibling": "Welcome"
# },
# {
#     "type": "response_condition",
#     "output": {
#         "generic": [
#             {
#                 "values": [
#                     {
#                         "text": "Our store is at ..."
#                     }
#                 ],
#                 "response_type": "text",
#                 "selection_policy": "sequential"
#             }
#         ]
#     },
#     "parent": "Location Info",
#     "conditions": "true",
#     "dialog_node": "response_without_location",
#     "previous_sibling": "response_with_location"
# },
# {
#     "type": "response_condition",
#     "output": {
#         "generic": [
#             {
#                 "values": [
#                     {
#                         "text": "Our $location store is at ..."
#                     }
#                 ],
#                 "response_type": "text",
#                 "selection_policy": "sequential"
#             }
#         ]
#     },
#     "parent": "Location Info",
#     "conditions": "$location",
#     "dialog_node": "response_with_location"
# }
def dialog_node_multi_condition(reference, condition_dict, slot_var, previous_sibling):

    handler_condition = condition_dict['handler']
    enter_condition = condition_dict['enter']
    outputs_and_conditions = condition_dict['output']

    def handler():
        return [
            {
                "type": "event_handler",
                "output": {},
                "parent": "slot_handler_parent_" + reference,
                "event_name": "focus",
                "dialog_node": "handler_focus_" + reference,
                "previous_sibling": "handler_" + reference
            },
            {
                "type": "event_handler",
                "output": {},
                "parent": "slot_handler_parent_" + reference,
                "context": {
                    "location": handler_condition
                },
                "conditions": handler_condition,
                "event_name": "input",
                "dialog_node": "handler_" + reference
            }
        ]

    def slot():
        return {
                "type": "slot",
                "parent": reference,
                "variable": slot_var,
                "dialog_node": "slot_handler_parent_" + reference,
                "previous_sibling": "response_" + reference + "0"
            }

    def frame():
        return {
                   "type": "frame",
                   "title": reference,
                   "metadata": {
                       "_customization": {
                           "mcr": True
                       }
                   },
                   "conditions": enter_condition,
                   "dialog_node": reference,
                   "previous_sibling": previous_sibling
               }

    def responses():
        responses_list = []
        node_idx = 0
        for condition, output in outputs_and_conditions:
            responses_list.append({
                "type": "response_condition",
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
                "parent": reference,
                "conditions": condition,
                "dialog_node": "response_" + reference + str(node_idx)
            })
            if node_idx < len(outputs_and_conditions) - 1:
                responses_list[node_idx]["previous_sibling"] = "response_" + reference + str(node_idx + 1)
            node_idx += 1
        return responses_list

    result_raw = [handler(), slot(), frame(), responses()]
    result = []
    for r in result_raw:
        if isinstance(r, list):
            result.extend(r)
        else:
            result.append(r)
    return result


def dialog_node_standard(reference, output, condition, previous_sibling):
    return {
        "type": 'standard',
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
