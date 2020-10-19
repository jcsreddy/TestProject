*** Settings ***
Library     SeleniumLibrary
*** Variables ***

*** Test Cases ***
LoginTest

    open browser    https://salesforce.com      chrome
    wait until page contains  salesforce
    close browser

*** Keywords ***
