
# HealthData AI — Healthcare Data Intelligence Dashboard

## Overview

HealthData AI is a Python-based web application that helps users explore and analyze healthcare provider information. It combines interactive data visualization, filtering, CSV export, and locally generated AI summaries.

This project was developed as a practical demonstration of AI-assisted development, prompt engineering, data analysis, and automation.

## Features

- Search healthcare provider records by name.
- Filter records by specialty and city.
- Display summary metrics for the filtered dataset.
- Visualize provider distribution using interactive charts.
- Download filtered records as a CSV file.
- Generate natural-language summaries using a locally running Ollama model.
- Display rule-based insights calculated with Pandas.

## Technology Stack

- Python 3.13.7
- Streamlit
- Pandas
- Plotly
- Requests
- Ollama
- Llama 3.2 1B local language model

## Dataset

The application currently uses a small, fictional dataset for demonstration and testing. The provider names do not represent verified real healthcare facilities.

No patient records or personal medical information are used.

## Prerequisites

- Python installed on your computer
- Ollama installed and running
- The `llama3.2:1b` model downloaded through Ollama

## Installation and Setup

1. Clone or download this project.
2. Open a terminal in the project directory.
3. Create a virtual environment:

   ```powershell
   python -m venv venv
   ```

4. Activate it on Windows:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

5. Install the required packages:

   ```powershell
   python -m pip install streamlit pandas plotly requests
   ```

6. Download the local AI model if it is not already installed:

   ```powershell
   ollama pull llama3.2:1b
   ```

7. Start the application:

   ```powershell
   python -m streamlit run app.py
   ```

8. Open the local URL displayed in the terminal, usually `http://localhost:8501`.

Ensure Ollama is running locally when using the AI summary feature.

## How to Use

1. Open the dashboard.
2. Search for a provider or select a city and specialty.
3. Review the updated metrics, provider table, and chart.
4. Download the filtered records using the CSV export button.
5. Select **Generate AI Summary** to request a summary of the filtered records.
6. Review the generated response and compare it with the displayed data.

## Project Structure

```text
HealthDataAI/
├── app.py
├── README.md
├── prompts.md
└── venv/
```

The virtual environment folder is local to your machine and should not be uploaded to GitHub.

## Limitations

- The current dataset contains fictional sample records.
- AI-generated summaries may contain inaccuracies and should be checked against the underlying data.
- The AI model runs locally through Ollama.
- A publicly hosted dashboard cannot automatically access Ollama running on a reviewer's computer. A separate deployment architecture is required for remote AI inference.

## Future Improvements

- Integrate a verified public healthcare provider dataset.
- Add automated data validation and more test cases.
- Improve AI output validation and error handling.
- Deploy the application with an appropriate hosted inference solution.
- Add downloadable analytical reports.

## Disclaimer

This application is an educational data-analysis demonstration. It is not a medical decision-support system and does not provide medical advice.
