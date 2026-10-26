/**
 * mywebscript.js
 * Client-side JavaScript for the Emotion Detector web application.
 * Handles API calls to the Flask backend and renders results.
 */

function analyzeEmotion() {
    const textInput = document.getElementById('textInput').value.trim();
    const resultBox = document.getElementById('resultBox');
    const emotionBars = document.getElementById('emotionBars');
    const errorMsg = document.getElementById('errorMsg');

    // Clear previous state
    errorMsg.style.display = 'none';

    if (!textInput) {
        errorMsg.style.display = 'block';
        return;
    }

    resultBox.classList.remove('visible');
    emotionBars.classList.remove('visible');
    resultBox.innerHTML = '<span style="color:rgba(255,255,255,0.4)">⏳ Analysing emotions...</span>';
    resultBox.classList.add('visible');

    const encodedText = encodeURIComponent(textInput);

    fetch(`/emotionDetector?textToAnalyse=${encodedText}`)
        .then(response => response.text())
        .then(data => {
            resultBox.innerHTML = data;
            resultBox.classList.add('visible');

            // Parse scores from response for the bars
            const angerMatch = data.match(/'anger': ([\d.]+)/);
            const disgustMatch = data.match(/'disgust': ([\d.]+)/);
            const fearMatch = data.match(/'fear': ([\d.]+)/);
            const joyMatch = data.match(/'joy': ([\d.]+)/);
            const sadnessMatch = data.match(/'sadness': ([\d.]+)/);

            if (angerMatch) {
                updateBar('barAnger', 'valAnger', parseFloat(angerMatch[1]));
                updateBar('barDisgust', 'valDisgust', parseFloat(disgustMatch[1]));
                updateBar('barFear', 'valFear', parseFloat(fearMatch[1]));
                updateBar('barJoy', 'valJoy', parseFloat(joyMatch[1]));
                updateBar('barSadness', 'valSadness', parseFloat(sadnessMatch[1]));
                emotionBars.classList.add('visible');
            }
        })
        .catch(err => {
            resultBox.innerHTML = '❌ Error connecting to the server. Please try again.';
        });
}

function updateBar(barId, valId, score) {
    const pct = Math.round(score * 100);
    document.getElementById(barId).style.width = pct + '%';
    document.getElementById(valId).textContent = pct + '%';
}

// Allow Enter key (Ctrl+Enter) to trigger analysis
document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('textInput').addEventListener('keydown', function (e) {
        if (e.ctrlKey && e.key === 'Enter') {
            analyzeEmotion();
        }
    });
});
