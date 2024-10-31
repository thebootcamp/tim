from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class ActionSubmitReport(Action):
    def name(self):
        return "action_submit_report"

    def run(self, dispatcher, tracker, domain):
        incident_type = tracker.get_slot('incident_type')
        device = tracker.get_slot('device')
        # Process the incident report...
        dispatcher.utter_message(text="Your report has been submitted. Our team will contact you shortly.")
        return []

class ActionAnalyzeSentiment(Action):

    def name(self) -> Text:
        return "action_analyze_sentiment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        analyzer = SentimentIntensityAnalyzer()
        user_message = tracker.latest_message.get('text')
        sentiment = analyzer.polarity_scores(user_message)

        if sentiment['compound'] >= 0.05:
            sentiment_label = "positive"
        elif sentiment['compound'] <= -0.05:
            sentiment_label = "negative"
        else:
            sentiment_label = "neutral"

        # Store sentiment in a slot
        return [SlotSet("sentiment", sentiment_label)]
