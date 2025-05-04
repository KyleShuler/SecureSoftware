# SecureSoftware
This is a secure weather forecast application that allows you to retrieve a 3-day weather forecasts by entering a ZIP code.
The application has been made following secure software development principles, including input validation, error handling, encryption of secrets, logging, unit testing, and static code analysis.

Features
Retrieve and display 3-day weather forecasts

Save a history of weather requests

Input validation and sanitization

Secure handling of API secrets

Detailed logging with secure file permissions

Error handling with user-friendly error messages

Unit tests and static analysis

Dependencies

Library	Version

requests	^2.31.0
python-dotenv	^1.0.1


External APIs Used
OpenWeatherMap API

API Docs: https://openweathermap.org/api

Threat Mitigation
API key exposure: API key stored securely in .env, not hardcoded in codebase. .gitignore prevents .env from being uploaded.

Input validation: bypass User input is validated to ensure only 5-digit ZIP codes are accepted.

Sensitive data leakage through errors: Error messages are user-friendly and do not expose internal system details. Technical errors are logged.

SQL/Injection attacks:	Any potential database use would employ prepared statements


Threat not yet handled: there is no rate limiting to prevent API abuse 


