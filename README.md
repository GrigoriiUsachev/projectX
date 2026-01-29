# ProjectX — Automated API & UI Testing Framework

This project demonstrates how to build a **production-like automated testing framework**
for **API and UI testing** using **Python, Pytest, Playwright, and CI/CD (GitHub Actions)**.

The main focus areas are:
- clean and maintainable test architecture
- separation of API and UI layers
- reproducible test runs
- clear proof that tests are actually executed in CI

---

## ✅ CI Proof (click-to-see)

This repository is configured so that **tests are automatically executed on every push**.

### 🔹 How to verify that everything works
1. Click the CI badge below  
2. Open the latest **successful run**
3. Scroll down to **Artifacts** and download the HTML reports

👉 This is a real CI execution, not mocks or screenshots.

[![projectX CI](https://github.com/GrigoriiUsachev/projectX/actions/workflows/ci.yml/badge.svg)](https://github.com/GrigoriiUsachev/projectX/actions)

### 📊 Test Reports (Artifacts)
- `api-html-report` — API test execution report
- `ui-html-report` — UI test execution report (Playwright)

> HTML reports are generated automatically in GitHub Actions and attached to every workflow run.

---

## 🛠 Tech Stack

**Language & Frameworks**
- Python 3.11
- Pytest
- Playwright

**Testing**
- API testing
- UI testing
- pytest-html reports

**Infrastructure**
- GitHub Actions (CI)
- Virtual environments
- Cross-platform setup (Windows / macOS / Linux)

---

## 📁 Project Structure

projectX/
│
├── api_tests/ # API test cases
├── ui_tests/ # UI test cases (Playwright)
├── config/ # Configuration files
├── utils/ # Helpers and utilities
│
├── requirements.txt
├── pytest.ini
├── README.md
└── .github/workflows/ci.yml


## ▶️ Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/GrigoriiUsachev/projectX.git
cd projectX

Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

macOS / Linux
python3 -m venv .venv
source .venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt
playwright install

▶️ Run Tests
Run all tests
pytest

Run API tests only
pytest api_tests

Run UI tests only
pytest ui_tests

Generate an HTML report locally
pytest --html=report.html --self-contained-html

🎯 Project Purpose

This project is intended as a demonstration project to show:

how a real-world test automation framework can be structured

how CI pipelines are configured to run tests automatically

how test results are documented using HTML reports

how a test automation repository should look for code review and hiring processes

👤 Author

Grigorii Usachev
GitHub: https://github.com/GrigoriiUsachev
