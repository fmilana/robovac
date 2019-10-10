from rasa_sdk import Action
from rasa_sdk.events import SlotSet


class ResetSlots(Action):
    def name(self):
        return "action_reset_slots"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("location", None), SlotSet("time", None)]


# sets slots based on user message entities
class CheckEntities(Action):
    def name(self):
        return "action_check_entities"

    def run(self, dispatcher, tracker, domain):
        for e in tracker.latest_message['entities']:
            # might need to differentiate between location/angle, time/interval
            if e['entity'] == 'location':
                location = e['value']
            elif e['entity'] == 'angle':
                location = e['value']
            elif e['entity'] == 'time':
                time = e['value']
            elif e['entity'] == 'interval':
                time = e['value']

        return [SlotSet("location", location), SlotSet("time", time)]


class GoBackToBase(Action):
    def name(self):
        return "action_go_back_to_base"

    def run(self, dispatcher, tracker, domain):
        for e in tracker.latest_message['entities']:
            if e['entity'] == 'time':
                time = e['value']
            elif e['entity'] == 'interval':
                time = e['value']

        # API call here

        if time is not None:
            message = "Ok, I will return to my base " + str(time) + "."
        else:
            message = "Ok, I will return to my base."

        dispatcher.utter_message(message)
        return []


class ActionClean(Action):
    def name(self):
        return "action_clean"

    def run(self, dispatcher, tracker, domain):
        location = tracker.get_slot('location')
        time = tracker.get_slot('time')

        # API call here

        if time is not None:
            message = "Ok, I will clean " + str(location) + " " + str(time) + "."
        else:
            message = "Ok, I will clean " + str(location) + " now."

        dispatcher.utter_message(message)
        return []


class HowLongLeft(Action):
    def name(self):
        return "action_how_long_left"

    def run(self, dispatcher, tracker, domain):

        # API call here

        message = "I will take less than 1 minute."
        dispatcher.utter_message(message)
        return []


class WhatAmIDoing(Action):
    def name(self):
        return "action_what_am_i_doing"

    def run(self, dispatcher, tracker, domain):

        # API call here

        message = "I am currently cleaning."
        dispatcher.utter_message(message)
        return []


class Bin(Action):
    def name(self):
        return "action_bin"

    def run(self, dispatcher, tracker, domain):

        # API call here

        message = "My bin is 20% full."
        dispatcher.utter_message(message)
        return []


class Battery(Action):
    def name(self):
        return "action_battery"

    def run(self, dispatcher, tracker, domain):

        # API call here

        message = "My battery is 80% full."
        dispatcher.utter_message(message)
        return []


class Stop(Action):
    def name(self):
        return "action_stop"

    def run(self, dispatcher, tracker, domain):

        # API call here

        message = "Ok, I will stop cleaning now."
        dispatcher.utter_message(message)
        return[]


class AmIAtBase(Action):
    def name(self):
        return "action_am_i_at_base"

    def run(self, dispatcher, tracker, domain):

        # API call here

        message = "Yes. I am currently at my base."
        dispatcher.utter_message(message)
        return []


class Fallback(Action):
    def name(self):
        return "action_fallback"

    def run(self, dispatcher, tracker, domain):
        message = "Sorry, I don't understand."
        dispatcher.utter_message(message)
        return []
