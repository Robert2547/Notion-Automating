# Notion Auto

## Overview
Notion Auto is a program designed to automate the management of internship applications and job listings, integrating with Notion, Gmail, and Slack via Zapier.

## Features
- **Email Integration**: Automatically retrieves emails related to software internship applications using the Gmail API.
- **Content Analysis**: Employs GPT-3.5 for analyzing email content to distinguish between job listings and application updates.
- **Notion API Integration**: Updates a Notion database with job and application information.
- **GPT Fine-Tuning**: Enhances tool reliability and consistency.
- **Zapier Automation**:
    - **Notion to Slack**: Sends notifications to Slack using Zapier whenever a new database entry is added or updated in Notion, ensuring timely updates for the team.
    - **Gmail to Google Cloud**: Triggers Python code hosted on Google Cloud via Zapier when a new email arrives in the "Updates" section, automating the processing of email content.

## Technology Stack
- Python
- Gmail API
- GPT-3.5
- Google Cloud Auth
- Notion API
- Zapier Integration

## Project Status
In development since December 2023. Focused on streamlining the job application process for software internships.

## Contributions
Contributions are welcome. Please submit issues and pull requests on GitHub.

## Contact
For more information, contact [Joseph Benno](mailto:josephbenno2547@gmail.com).
