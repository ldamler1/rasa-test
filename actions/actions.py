# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

#todo custom utter action to retrieve response from gateway?
#todo custom action for static intent/response fulfillment
# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionTransactionSearch(Action):

    def name(self) -> Text:
        return "action_transaction_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        transaction_amount = tracker.get_slot("transaction_amount")
        transaction_date = tracker.get_slot("transaction_date")

        dispatcher.utter_message(text="Is this the transaction you're looking to dispute? {}, {}".format(transaction_amount, transaction_date))

        return [SlotSet("transaction_amount", transaction_amount), SlotSet("transaction_date", transaction_date)]
