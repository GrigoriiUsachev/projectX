[![projectX CI](https://github.com/GrigoriiUsachev/projectX/actions/workflows/ci.yml/badge.svg)](https://github.com/GrigoriiUsachev/projectX/actions)

## ProjectX — Automated API & UI Testing Framework

This repository demonstrates a **production-like automated testing framework** for **API and UI testing** using **Python, Pytest, Playwright, and CI/CD with GitHub Actions**.

The project is designed specifically as a **portfolio / hiring demonstration** to showcase test automation skills, CI integration, and proper repository structure.

## CI Status

Continuous Integration is configured using **GitHub Actions** and runs **automatically on every push**.

## How to Verify CI Is Working

1. Click the **CI badge** at the top of the README
2. Open the latest **successful workflow run**
3. Scroll down to the **Artifacts** section
4. Download and open the HTML test reports

This provides **real proof** that tests are executed in CI.

## Test Reports (Artifacts)

- **api-html-report** — API test execution report
- **ui-html-report** — UI test execution report (UI tests)

## Tech Stack

### Language & Frameworks
- Python 3.11
- Pytest
- Playwright

### Testing
- API testing
- UI testing
- pytest-html reports

### Infrastructure
- GitHub Actions (CI)
- Virtual environments
- Cross-platform execution (Windows / macOS / Linux)

## Project Structure

```text
projectX/
├── api_tests          # API test cases
├── ui_tests           # UI test cases
├── config             # Configuration files
├── utils              # Helper utilities
├── requirements.txt
├── pytest.ini
└── .github/workflows/ci.yml
```

## Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/GrigoriiUsachev/projectX.git
cd projectX
```

### 2. Create a virtual environment

#### Windows (PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

#### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
playwright install
```

## Run Tests

```bash
pytest
```

```bash
pytest api_tests
```

```bash
pytest ui_tests
```

```bash
pytest --html=report.html --self-contained-html
```

## Project Purpose

- practical skills in test automation
- separation of API and UI testing layers
- CI integration with real test execution
- proper repository presentation for technical review and hiring processes

## Author

**Grigorii Usachev**
GitHub: https://github.com/GrigoriiUsachev


