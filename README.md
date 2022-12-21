# Python-QA-Engineer-Module3
Course: Python QA Engineer - 2022 (OTUS).\
Homework 5: Writing simple autotests and the basics of Selenium.\
Homework 6: PageObject.\
Homework 7: Logging and reporting(Allure).\
Homework 8: Selenoid.\
Homework 12: Write a Dockerfile for your project.\
Project work: Test automation for Opencart web application.

Technologies used: python, pytest, pytest-xdist, selenoid, mimesis, selenium, docker, allure.\
Before starting you need:
- deploy opencart app
- install python 3.9+
- create a virtual environment (example for macOS): python -m venv venv; source venv/bin/activate;
- install dependencies: pip install -r requirements.txt

Run autotests command: pytest --param1 value1 --param2 value2 ... --paramN valueN

You can also run autotests in docker:
- install docker desktop
- build image: docker build -t <image_name> .
- start the container by passing parameters for pytest: docker run <image_name> --browser firefox

To generate a report, you need to run the command: allure generate allure-results.

Passed parameters:
- browser - possible values are "chrome"(default), "firefox", "opera"
- url - Opencart address, by default "http://192.168.0.105:8081"
- drivers - path to folder with Selenium drivers, for local launch, by default "~/selenium_drivers/"
- headless - headless mode enable flag, False by default
- executor - ip with deployed Selenoid, or "local" (in case of local launch), by default "192.168.0.105"
- browser_version - browser version in Selenoid, specified in conjunction with executor, default "108.0"
- you can also add the -n option to parallelize autotests.