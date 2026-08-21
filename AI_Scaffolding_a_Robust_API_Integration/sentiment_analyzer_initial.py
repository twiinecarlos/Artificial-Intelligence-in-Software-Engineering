#!/usr/bin/python3
"""
Sentiment Analysis Tool
Analyzes the sentiment of a given sentence using a public API.
"""

import sys

import requests


def analyze_sentiment(text):
    """Analyze the sentiment of the given text."""
    url = "https://api.text-processing.com/api/sentiment/"
    payload = {"text": text}

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
        data = response.json()
        label = data.get("label", "neutral")

        if label == "pos":
            return "positive"
        elif label == "neg":
            return "negative"
        else:
            return "neutral"

    except requests.exceptions.HTTPError as error:
        print("HTTP Error: {}".format(error), file=sys.stderr)
        return None
    except requests.exceptions.RequestException as error:
        print("Request failed: {}".format(error), file=sys.stderr)
        return None
    except (KeyError, ValueError) as error:
        print("Invalid response format: {}".format(error), file=sys.stderr)
        return None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./sentiment_analyzer_initial.py <sentence>")
        sys.exit(1)

    sentence = " ".join(sys.argv[1:])
    result = analyze_sentiment(sentence)

    if result:
        print(result)
    else:
        sys.exit(1)
