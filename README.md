# oaqjp-final-project-emb-ai

## Emotion Detector - AI-Based Web Application

This project is an AI-based Emotion Detector web application developed as the final project for the IBM AI Application Development course. It uses the Watson NLP library to analyze text and detect emotions.

## Project Structure

```
oaqjp-final-project-emb-ai/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── templates/
│   └── index.html
├── static/
│   └── mywebscript.js
├── server.py
├── test_emotion_detection.py
└── README.md
```

## Features

- Detects emotions (anger, disgust, fear, joy, sadness) from text input
- Returns the dominant emotion with confidence scores
- RESTful API with Flask web framework
- Error handling for blank or invalid inputs
- Static code analysis with pylint (10/10 score)

## Tasks Completed

1. Clone the project repository
2. Create an emotion detection application using the Watson NLP library
3. Format the output of the application
4. Package the application (EmotionDetection package)
5. Run Unit tests on the application
6. Web deployment using Flask
7. Incorporate error handling
8. Run static code analysis

## Technologies Used

- Python 3.x
- Flask
- Requests library
- Watson NLP (Embed AI)
- Pylint

## How to Run

```bash
pip install flask requests pylint
python server.py
```

Open your browser and navigate to `http://localhost:5000`

## Author

Final Project – Emotion Detector  
IBM AI Application Development with Python and Flask
