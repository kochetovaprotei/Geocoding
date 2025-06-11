# Geocoding Project

This repository provides automated testing for geocoding functionality using the Nominatim API. The project is written in Python and leverages popular testing and reporting frameworks such as pytest and Allure.

## Features

- **Direct Geocoding Tests**: Verifies that given an address (from a JSON test data file), the system correctly returns the expected latitude and longitude.
- **Reverse Geocoding Tests**: Checks that given coordinates (latitude and longitude from another JSON file), the system can accurately return the corresponding address.
- **Parameterized Testing**: Uses pytest’s parameterization to run multiple test cases from external JSON files, ensuring broad coverage of possible geocoding scenarios.
- **Allure Integration**: Includes step-by-step Allure reporting, attaching test data and detailed logs for easy debugging and result analysis.
- **Logging**: Utilizes a custom logging utility to log key assertions and outcomes during test execution.

## Structure

- `utils/`: Contains utility modules for data loading, API communication, and logging.
- `tests/`: Contains pytest test classes for both direct and reverse geocoding.
- `data_for_searching_by_name.json` and `data_for_searching_by_coordinates.json`: Store sample input and expected output data for parameterized tests.

## Typical Use Case

This project is ideal for teams developing, verifying, or integrating geocoding services, ensuring that API responses match expected results for both address-to-coordinates and coordinates-to-address lookups.

## Technologies

- Python
- pytest
- Allure
- Nominatim API

---

**Summary:**  
The repository is a robust, test-driven suite for validating geocoding (address ↔ coordinates) accuracy using the Nominatim API, with advanced reporting and logging for transparent quality assurance.
