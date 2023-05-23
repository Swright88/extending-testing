# Document Updater Test Plan.
## Objective

This test plan intends to outline the testing which will be performed to identify any potential bugs within the document_updater.py Python file.
This Python program has a section called originals in which it stores Targets (A name and an address) Then if the target is added to a droplist or allowlist it will follow the corresponding action and they may be updated. At the end any Targets left will be added to the finals section. 

* To be able to carry the tests out, Fake data will be created using Faker. This will allow us to generate a random name and address to go alongside it. 

## Scope of Testing
Tests for this program will be carried out using Python within VS Code. 
Test cases have been put together in Test_cases.md

## Test Envirnments
The following version of Python and environments are being used:
* Python 3.11.3
* Pipenv shell (environment)
* Faker (External Library)
* VS Code Version: 1.78.2 (Universal)

## To be tested
* Adding a new Target into Originals
* Adding Target to droplist
* Adding Target to allowlist
* Adding updated Target to Updates
* Checking Targets in Finals