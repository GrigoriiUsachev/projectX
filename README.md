[![projectX CI](https://github.com/GrigoriiUsachev/projectX/actions/workflows/ci.yml/badge.svg)](https://github.com/GrigoriiUsachev/projectX/actions)


ProjectX — Automated API & UI Testing Framework
This project demonstrates a production-like automated testing framework for API and UI testing using Python, Pytest, Playwright, and CI/CD with GitHub Actions.
CI Proof (Click-to-See)
All tests in this repository are executed automatically on every push via GitHub Actions.

How to verify:
1. Open the GitHub Actions page for this repository
2. Select the latest successful workflow run
3. Scroll down to Artifacts and download the HTML test reports

This provides real proof that tests are executed in CI.
Test Reports (Artifacts)
- api-html-report — API test execution report
- ui-html-report — UI test execution report (Playwright)
Tech Stack
Language & Frameworks:
- Python 3.11
- Pytest
- Playwright

Testing:
- API testing
- UI testing
- pytest-html reports

Infrastructure:
- GitHub Actions (CI)
- Virtual environments
- Cross-platform execution (Windows / macOS / Linux)
Project Structure
projectX/
 ├── api_tests/        API test cases
 ├── ui_tests/         UI test cases
 ├── config/           Configuration files
 ├── utils/            Helper utilities
 ├── requirements.txt
 ├── pytest.ini
 └── .github/workflows/ci.yml
Run Locally
1. Clone repository:
git clone https://github.com/GrigoriiUsachev/projectX.git
cd projectX

2. Create virtual environment:
Windows (PowerShell):
python -m venv .venv
.\.venv\Scripts\Activate.ps1

macOS / Linux:
python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies:
pip install -r requirements.txt
playwright install
Run Tests
Run all tests:
pytest

Run API tests only:
pytest api_tests

Run UI tests only:
pytest ui_tests

Generate HTML report locally:
pytest --html=report.html --self-contained-html
Project Purpose
This project exists as a demonstration of how a real-world test automation framework can be structured, executed in CI, and presented for code review and hiring processes.
Author
Grigorii Usachev
GitHub: https://github.com/GrigoriiUsachev
