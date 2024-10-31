from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionSubmitReport(Action):
    def name(self):
        return "action_submit_report"

    def run(self, dispatcher, tracker, domain):
        incident_type = tracker.get_slot('incident_type')
        device = tracker.get_slot('device')
        # Process the incident report...
        dispatcher.utter_message(text="Your report has been submitted. Our team will contact you shortly.")
        return []
