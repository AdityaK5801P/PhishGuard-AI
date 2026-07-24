Project Name: PhishGuard AI

Version: 1.0

Type: AI-Powered Cybersecurity Web Application

Goal:
Detect phishing websites by analyzing URLs, using machine learning to classify them, and explaining the reasons behind the prediction so users can make informed decisions.

Functional Requirements

The system shall:

Analyze a submitted URL.
Extract security-related URL features.
Predict whether the URL is Safe, Suspicious, or Phishing.
Generate a confidence score.
Explain the factors that influenced the prediction.
Save scan history.
Display previous scans on a dashboard.
Generate downloadable PDF reports.
Non-Functional Requirements

Our application should also meet quality goals.

Requirement	Goal
Performance	Analysis should complete within a few seconds for a URL-only scan.
Security	Validate all input, protect against common web attacks, and avoid exposing sensitive configuration.
Maintainability	Use a modular project structure with clear separation of responsibilities.
Scalability	Design components so external services (WHOIS, VirusTotal, etc.) can be added later.
Usability	Provide a clean, beginner-friendly interface with clear explanations.
Technology Stack
Frontend
React
Vite
Tailwind CSS
Axios
React Router
Backend
FastAPI
Uvicorn
Pydantic
SQLAlchemy
SQLite (Version 1.0)
Machine Learning
Python
Scikit-learn
Pandas
NumPy
Joblib
Development Tools
VS Code
Git
GitHub
Postman (API testing)
Swagger UI (FastAPI)
Project Scope
Included in Version 1.0
URL analysis
Feature extraction
Explainable AI
ML prediction
Dashboard
History
PDF report generation
Deferred to Later Versions
Browser extension
Email phishing analysis
QR code analysis
User accounts
Real-time monitoring
Mobile application
Success Criteria

A release of PhishGuard AI v1.0 is considered successful if:

A user can submit a URL.
The application returns a classification (Safe / Suspicious / Phishing).
The application provides a confidence score.
The application explains the reasoning behind the result.
The scan is saved to history.
The user can generate a PDF report.