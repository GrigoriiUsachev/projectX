[![projectX CI](https://github.com/GrigoriiUsachev/projectX/actions/workflows/ci.yml/badge.svg)](
https://github.com/GrigoriiUsachev/projectX/actions/workflows/ci.yml
)
# ProjectX — QA Automation Framework (UI + API)

ProjectX is a Python-based test automation framework that includes:
- UI automation (Selenium + Pytest, Page Object Model)
- API automation (Requests + Pytest, client-based design)
- GitHub Actions CI (API + UI in headless mode)
- HTML reports (pytest-html) and screenshots on UI failure

## Tech Stack
- Python 3.11
- Pytest
- Selenium WebDriver
- webdriver-manager
- Requests
- pytest-html
- GitHub Actions

## Project Structure
projectX/
api/
clients/
tests/
reports/
ui/
pages/
tests/
reports/
screenshots/
shared/
config/
utils/
.GitHub/workflows/
pytest.ini
requirements.txt

## Setup
Create and activate a virtual environment, then install dependencies:


python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

Run Tests
Run all tests
pytest -q

Run API tests only
pytest -m api -q --html=api/reports/api_report.html --self-contained-html

Run UI tests only
pytest -m ui -q --html=ui/reports/ui_report.html --self-contained-html

Reports

API HTML report: api/reports/api_report.html

UI HTML report: ui/reports/ui_report.html

UI screenshots on failure: ui/reports/screenshots/

In GitHub Actions, HTML reports and screenshots are published as workflow artifacts.

CI (GitHub Actions)

On every push / pull request:

API tests run first

UI tests run in headless mode

HTML reports are uploaded as artifacts

Screenshots are uploaded on UI failures