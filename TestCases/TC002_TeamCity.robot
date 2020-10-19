*** Settings ***
Library  SeleniumLibrary
Library  Webdriver
Library     SeleniumLibrary
*** Variables ***

*** Test Cases ***
LoginTest

    open browser    https://salesforce.com      chrome
    wait until element contains  salesforce
    close browser

*** Keywords ***
