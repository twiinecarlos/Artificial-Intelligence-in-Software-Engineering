# AI: Scaffolding a Robust API Integration

This task demonstrates how I used contextual prompting with ChatGPT to improve
a Python sentiment analysis API integration.

## Objective

The goal was to improve the original program by adding secure API key handling
and more specific network error handling.

## Files

### sentiment_analyzer_initial.py

Contains the original sentiment analyzer before AI-assisted refactoring.

### sentiment_analyzer.py

Contains the improved version generated and reviewed during this task.

The refactored version:

- Reads the API key from `TEXT_PROCESSING_API_KEY`
- Does not hard-code the API key
- Uses an `Authorization: Bearer <key>` header
- Adds a timeout to the HTTP request
- Handles `requests.exceptions.Timeout`
- Handles `requests.exceptions.ConnectionError`
- Handles `requests.exceptions.HTTPError`
- Handles `requests.exceptions.RequestException`
- Handles invalid response data

## AI Tool Used

I used ChatGPT and provided the complete original code together with specific
security and error-handling requirements.

Using contextual prompting helped the AI preserve the original behavior while
adding the required authentication and robustness improvements.

## Testing

I tested the missing API key case with:

    unset TEXT_PROCESSING_API_KEY
    python3 sentiment_analyzer.py "I love programming"

The program returned:

    Missing TEXT_PROCESSING_API_KEY environment variable.

I then set a dummy API key with:

    export TEXT_PROCESSING_API_KEY="DUMMY_KEY"

I ran:

    python3 sentiment_analyzer.py "I really enjoyed this project"

The external API returned an SSL connection error, and the program correctly
handled it using its ConnectionError exception handling.
