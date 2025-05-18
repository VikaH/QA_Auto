# QA Automation with Python

This project is a comprehensive collection of automated tests and supporting modules developed as part of the **QA Automation with Python** course provided by **Prometheus**.

## Major Technologies Used

- **Python**: Main programming language for test development.
- **Pytest**: Framework for writing and running unit and integration tests.
- **Selenium**: Used for browser automation and UI testing.
- **Requests**: For HTTP API testing.
- **SQLite3**: Lightweight database for backend testing and data storage.
- **webdriver-manager**: Simplifies management of browser drivers for Selenium.
- **VS Code**: IDE for development.

## Project Structure

- `modules/`  
  - `api/clients/`: API client classes (e.g., GitHub API).
  - `common/`: Shared modules (e.g., database access).
  - `ui/page_objects/`: Page Object Model classes for UI automation.
- `tests/`  
  - `api/`: API and HTTP tests.
  - `database/`: Database-related tests.
  - `ui/`: UI automation tests.
- `config/`: Configuration and utility functions.
- `conftest.py`: Pytest fixtures for test setup and teardown.

## Course

This repository was created as part of the **QA Automation with Python** course by [Prometheus](https://prometheus.org.ua/), covering:

- API testing
- UI automation
- Database testing
- Test organization and best practices

---

**Note:**  
To run the tests, install the required dependencies and use `pytest`. Make sure you have Chrome installed for UI tests and the database file (`become_qa_auto.db`) in the project root.
