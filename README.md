# Automated tests for Digital Opening Form (LYNX)

This repository contains automated tests for Digital Opening Form (LYNX) using Python, Selenium and Pytest. The test can run on Windows and Linux environments. It's using a data driven model where tests run for a different set of test data given in .csv file

## Test Description

This automated test performs the following steps:

1. **Open url for DOF**
   - Launches the DOF

2. **Fill out the form till it opens the 'trade' form**
   - Enters different kind of data from .csv file to execute multiple test scenarios

3. **Verify Results**
   - Checks if validations are working as expected and user is able to navigate correctly as expected
   - Test will fail if any of the assertions returns False

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Running Tests](#running-tests)



## Getting Started

To get started with this project, follow the instructions below

### Prerequisites

Before you begin, make sure you have the following installed:

- Python 3.8.0 or higher
- Chrome browser
- Git

### Installation
- Download and install the latest version of [Chrome Browser](https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwjug5KTpNeBAxUUp9UKHVE8BnQYABAAGgJ3cw&ase=2&gclid=Cj0KCQjw1OmoBhDXARIsAAAYGSHujsSoTwk0H1G7RgC-1Pt3qm6gKJ5Kq07F8MZ9crllSjTjT6n--GMaAiCoEALw_wcB&ei=e6waZYeqK46Fxc8P6JCxmAE&ohost=www.google.com&cid=CAESV-D2_-jWE4O2wHQzNOFVTiBHSdK3zxPb9VpJaB9TTTT0T-UU1wLVcYhH7kAx_vYPoWrWIsXMohwDB20guWl4a2rdIllyOs6d_u2VxSxRDhyggFpbHO02ww&sig=AOD64_3zvyT3UcU2AemBlSRNSMyyog_BNQ&q&sqi=2&nis=4&adurl&ved=2ahUKEwjH04qTpNeBAxWOQvEDHWhIDBMQ0Qx6BAgNEAE)
- Download and install the latest version of [Git](https://git-scm.com/downloads) available and make sure the system environmental variable points to it

## Usage

**Clone the Repository** 
   ```
    git clone https://github.com/PythonNovice5/lynx_tests_assignment.git
    cd lynx_tests_assignment
   ```
**Set up Virtual env and install the dependencies [Windows]** 
   ```
    python -m venv venv 
    venv\Scripts\activate.bat
    python -m pip install -r requirements.txt   
  ```
**Set up Virtual env and install the dependencies [Linux]** 
   ```
    python3 -m venv venv 
    source venv/bin/activate
    python -m pip install -r requirements.txt
   ```

## Running Tests
   **1. Running all tests via pytest command on Windows/Linux** 
  
  ```
  Go to project directory lynx_tests_assignment (cd lynx_tests_assignment)
  python -m pytest -v -s --html=report.html tests/test_registration.py
  ```
   **2. Running critical tests via pytest command on Windows/Linux** 
  
  ```
  Go to project directory lynx_tests_assignment (cd lynx_tests_assignment)
  python -m pytest -v -s --html=report.html -m critical
  ```

  **3. Running  all tests via pytest command on Windows/Linux as HeadLess browser**
  
  ```
  Go to project directory lynx_tests_assignment (cd lynx_tests_assignment)
  pytest -v -s --headless --html=report.html tests/test_registration.py
  ``` 
  **4. Running  critical tests via pytest command on Windows/Linux as HeadLess browser**
  
  ```
  Go to project directory lynx_tests_assignment (cd lynx_tests_assignment)
  pytest -v -s --headless --html=report.html -m critical
  ``` 

