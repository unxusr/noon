# Noon 
Automate E2E scenario on noon.com

### Description
Search for an item on noon.com , add it to the wish list and move it to the cart and build the address details 
### Note:
This project implemented and tested on the following specs

1. Ubuntu 20.4
2. python3 
3. behave framework
4. selenium webdriver
5. allure report
6. Chrome webdriver

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages in the requirements.txt.
```bash
pip3 install -r requirements.txt
```

### Usage
Clone the repo or download as zip

```shell
# CHANGE YOUR DIRECTORY TO REPOSITORY PARENT DIRECTORY
cd noon

# RUN WITH DEFAULT WEB BROWSER (Chrome)
behave

# USING DIFFERENT WEB BROWSER
behave -D BROWSER=firefox

# TO RUN ALL FEATURES USING ALLURE REPORTS
behave -f allure_behave.formatter:AllureFormatter -o 

# VIEW TEST REPORTS
allure serve reports/
```
### To be added later
1. Automate OTP verfication 
2. Make more complex End to End scenario
3. Add CI/CD with Jenkins or Travis

