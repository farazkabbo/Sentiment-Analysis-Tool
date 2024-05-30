import unittest
from src.preprocess_data import preprocess_text
from src.analyza_data import analyze_sentiment
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

class TestSentimentAnalysis(unittest.TestCase):
    
    def setUp(self):
        # Setup that runs before each test method
        self.sample_data = ["Happy with the excellent customer service!", "Terrible experience, very disappointed."]
        self.vectorizer = CountVectorizer()
        self.model = MultinomialNB()

    def test_preprocess_text(self):
        # Test the preprocessing output
        results = [preprocess_text(text) for text in self.sample_data]
        expected = [['happy', 'excellent', 'customer', 'service'], ['terrible', 'experience', 'disappointed']]
        self.assertEqual(results, expected)

    def test_sentiment_analysis(self):
        # Test sentiment analysis functionality
        data = self.vectorizer.fit_transform(self.sample_data)
        self.model.fit(data, [1, 0])  # Assuming 1 is positive, 0 is negative
        predictions = self.model.predict(data)
        expected = [1, 0]  # Expected sentiments
        self.assertEqual(list(predictions), expected)

if __name__ == '__main__':
    unittest.main()
