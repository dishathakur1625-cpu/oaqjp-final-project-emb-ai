"""
Unit tests for the emotion_detector function.
Uses unittest.mock to simulate Watson NLP API responses
so tests pass without requiring network access to the IBM Skills Network.
"""

import unittest
from unittest.mock import patch, MagicMock
from EmotionDetection.emotion_detection import emotion_detector


def make_mock_response(emotion_scores, status_code=200):
    """Helper to create a mock requests.Response object."""
    mock_resp = MagicMock()
    mock_resp.status_code = status_code
    mock_resp.json.return_value = {
        "emotionPredictions": [
            {
                "emotion": emotion_scores
            }
        ]
    }
    return mock_resp


class TestEmotionDetector(unittest.TestCase):
    """Test cases for the emotion_detector function."""

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_joy_for_joyful_statement(self, mock_post):
        """Test that joy is the dominant emotion for a joyful statement."""
        mock_post.return_value = make_mock_response({
            'anger': 0.006274985, 'disgust': 0.0026897677,
            'fear': 0.009251126, 'joy': 0.9680386, 'sadness': 0.04672442
        })
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_anger_for_angry_statement(self, mock_post):
        """Test that anger is the dominant emotion for an angry statement."""
        mock_post.return_value = make_mock_response({
            'anger': 0.8073156, 'disgust': 0.024299098,
            'fear': 0.0076722, 'joy': 0.0043957, 'sadness': 0.028516777
        })
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_disgust_for_disgusting_statement(self, mock_post):
        """Test that disgust is the dominant emotion for a disgusting statement."""
        mock_post.return_value = make_mock_response({
            'anger': 0.07378601, 'disgust': 0.8786643,
            'fear': 0.018506264, 'joy': 0.007545637, 'sadness': 0.03682629
        })
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_sadness_for_sad_statement(self, mock_post):
        """Test that sadness is the dominant emotion for a sad statement."""
        mock_post.return_value = make_mock_response({
            'anger': 0.040723733, 'disgust': 0.030722141,
            'fear': 0.13491854, 'joy': 0.018329207, 'sadness': 0.79130608
        })
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_fear_for_fearful_statement(self, mock_post):
        """Test that fear is the dominant emotion for a fearful statement."""
        mock_post.return_value = make_mock_response({
            'anger': 0.047889516, 'disgust': 0.019494437,
            'fear': 0.7681317, 'joy': 0.013942124, 'sadness': 0.14654484
        })
        result = emotion_detector("I am really scared about this")
        self.assertEqual(result['dominant_emotion'], 'fear')


if __name__ == '__main__':
    unittest.main()
