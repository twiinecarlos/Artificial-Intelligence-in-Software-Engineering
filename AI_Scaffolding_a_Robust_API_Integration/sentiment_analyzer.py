#!/usr/bin/python3
"""
Sentiment Analysis Tool
Analyzes the sentiment of a given sentence using a public API.
"""

import os
import sys

import requests


def analyze_sentiment(text):
    """Analyze the sentiment of the given text."""
    url = "https://api.text-processing.com/api/sentiment/"
    api_key = os.environ.get("TEXT_PROCESSING_API_KEY")

    if not api_key:
        print(
            "Missing TEXT_PROCESSING_API_KEY environment variable.",
            file=sys.stderr
        )
        return None

    headers = {
        "Authorization": "Bearer {}".format(api_key)
    }
    payload = {"text": text}

    try:
        response = requests.post(
            url,
            data=payload,
            headers=headers,
            timeout=10
        )
        response.raise_for_status()

        data = response.json()
        label = data.get("label", "neutral")

        if label == "pos":
            return "positive"

        if label == "neg":
            return "negative"

        return "neutral"

    except requests.exceptions.Timeout as error:
        print(
            "Request timed out: {}".format(error),
            file=sys.stderr
        )
        return None

    except requests.exceptions.ConnectionError as error:
        print(
            "Connection error: {}".format(error),
            file=sys.stderr
        )
        return None

    except requests.exceptions.HTTPError as error:
        print(
            "HTTP error: {}".format(error),
            file=sys.stderr
        )
        return None

    except requests.exceptions.RequestException as error:
        print(
            "Request failed: {}".format(error),
            file=sys.stderr
        )
        return None

    except (KeyError, ValueError) as error:
        print(
            "Invalid response format: {}".format(error),
            file=sys.stderr
        )
        return None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./sentiment_analyzer.py <sentence>")
        sys.exit(1)

    sentence = " ".join(sys.argv[1:])
    result = analyze_sentiment(sentence)

    if result:
        print(result)
    else:
        sys.exit(1)
