
# HealthData AI — Prompt Engineering Documentation

## 1. Project Goal

Build a healthcare data intelligence dashboard that uses AI-assisted development, interactive data analysis, and a locally running language model to summarize fictional healthcare provider records.

## 2. Prompt 1 — Application Design

**Prompt:**

Create a Python Streamlit healthcare data intelligence dashboard. Include provider search, specialty and city filters, summary metrics, charts, and CSV downloads. Use Pandas and Plotly. Keep the interface simple and explain how to run the application locally.

**Purpose:**

Define the application's functionality, framework, and initial structure.

**Expected outcome:**

A working dashboard that allows users to explore and filter provider records.

**Verification:**

Run the application and test the search, filters, chart, and CSV download.

## 3. Prompt 2 — Smart Data Insights

**Prompt:**

Add a Smart Data Insights section to my Streamlit application. Analyze the currently filtered provider records and display the most represented city, most represented specialty, and the number of providers, cities, and specialties. Handle empty filtered results safely.

**Purpose:**

Generate useful statistics from the selected dataset.

**Implementation:**

Use Pandas value counts, unique values, and the filtered DataFrame.

**Verification:**

Change the city and specialty filters and confirm that the insights update with the selected records.

**Important distinction:**

This section uses rule-based Python analytics. It is not a generative AI feature.

## 4. Prompt 3 — Local AI Summary

**Prompt:**

Connect my Streamlit dashboard to a local Ollama model. When the user clicks a button, send the currently filtered fictional provider records to the model and generate a concise report containing a summary, the most represented city, the most represented specialty, and one useful observation. Do not invent facts or provide medical advice.

**Purpose:**

Integrate a locally running language model without a paid external API.

**Implementation:**

Use the Requests library to call Ollama's local generation endpoint with the selected model.

**Verification:**

Click the AI summary button and check whether the model returns a report. Repeat with different filter selections.

## 5. Prompt 4 — Improve Accuracy

**Prompt:**

Improve the AI summary prompt by providing verified statistics calculated with Python. Include the total number of filtered records, number of cities, number of specialties, and provider counts by city and specialty. Tell the model to use only these statistics, preserve all counts, and mention ties when categories have equal counts.

**Purpose:**

Reduce inconsistent or invented counts in generated summaries.

**Implementation:**

Calculate the statistics in Python before constructing the prompt.

**Verification:**

Compare the AI-generated summary with the dashboard metrics and the underlying filtered records.

**Limitation:**

Prompt instructions alone cannot guarantee that a language model will always return accurate numbers.

## 6. Prompt 5 — Troubleshooting and Execution

**Prompt:**

Help troubleshoot a Windows Streamlit project using a Python virtual environment. Diagnose missing commands, confirm the correct environment, and provide commands to run the application without reinstalling working components unnecessarily.

**Purpose:**

Resolve environment and command-line issues during development.

**Verification:**

Confirm that the required packages are installed and that the Streamlit dashboard starts successfully.

## 7. Tools Used

- ChatGPT: assistance with code generation, debugging, and prompt refinement.
- Python: application logic and data analysis.
- Streamlit: web application interface.
- Pandas: filtering, counting, and data processing.
- Plotly: interactive visualization.
- Ollama with Llama 3.2 1B: local language-model inference.
- VS Code: development environment.

## 8. Challenges and Solutions

### Challenge 1: Running Streamlit

**Issue:** The terminal could not recognize the Streamlit command after switching terminals.

**Solution:** Activate the Python virtual environment and run the application using `python -m streamlit run app.py`.

### Challenge 2: Running Ollama

**Issue:** The Ollama command was initially unavailable in the terminal.

**Solution:** Complete the installation, reopen VS Code, and verify the installation using `ollama --version`.

### Challenge 3: Inconsistent AI-generated counts

**Issue:** The initial AI response included inconsistent counts.

**Solution:** Calculate verified counts using Pandas and include them explicitly in the model prompt.

## 9. Final Outcome

The application includes an interactive provider dashboard, filters, summary metrics, charts, CSV export, rule-based insights, and a local AI summary feature.

The application was tested locally using fictional sample data. The AI summary was observed to generate a response, but its factual accuracy must still be checked against the underlying data.

## 10. Future Improvements

- Use a verified public healthcare dataset.
- Add automated tests for filtering and data calculations.
- Validate AI-generated counts programmatically.
- Improve error handling and user feedback.
- Publish the source code and provide clear deployment instructions.

## 11. Responsible Use

The dataset contains fictional provider information. The application is intended for educational demonstration and must not be used to make clinical decisions.
