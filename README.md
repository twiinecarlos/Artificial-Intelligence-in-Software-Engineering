# Artificial Intelligence in Software Engineering

## Overview
This repository contains tasks demonstrating the use of Artificial Intelligence (AI) tools (such as ChatGPT) in software engineering workflows.

The goal is to use AI not just for generating code, but as:
- A conceptual tutor
- A debugging assistant
- A security auditor
- A code generation co-pilot

Each task focuses on a specific concept and shows how AI can improve understanding, safety, and development efficiency.

---

## Repository Structure

---

## Tasks Included

### 1. AI C Preprocessor Co-Pilot
- Demonstrates macro safety inspection using AI
- Identifies common macro bugs (operator precedence)
- Uses AI to generate safe conditional compilation scaffolding

---

## Tools Used
- ChatGPT (AI analysis and code generation)
- C Programming Language

---

## Key Learning Outcomes
- Understanding C preprocessor risks
- Writing safer macros
- Using AI for debugging before compilation
- Applying conditional compilation professionally

---
# AI: Integrating Robust Error Handling in OOP

## AI Tool Used
Gemini Code Assist (VS Code sidebar)

## Files
- `initial_code.py` — original Product/InventoryManager classes, no validation
- `refactored_code.py` — final code with @property validation and InvalidProductDataError

## Summary
Used Gemini Code Assist to add @property-based validation for `price` and `quantity`
on the Product class, raising a custom InvalidProductDataError on invalid (negative)
values instead of allowing the app to crash or silently store bad data. Verified with
a test case assigning a negative quantity, which correctly raised and caught the
custom exception.

## Author
Twiine Mugisha Carlos
