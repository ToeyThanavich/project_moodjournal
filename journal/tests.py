from django.test import TestCase
from journal.utils import AIForthaiSentimentAnalyzer

class AIForthaiTestCase(TestCase):
    def test_sentiment_api(self):
        analyzer = AIForthaiSentimentAnalyzer()
        text = "วันนี้คุณรู้สึกดีไหม?"
        result = analyzer.analyze(text)
        print(result)
        self.assertIn(result['sentiment_label'], ['positive', 'neutral', 'negative'])
