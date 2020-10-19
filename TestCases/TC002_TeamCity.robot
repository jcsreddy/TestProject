*** Settings ***
Library  SeleniumLibrary
Library  Webdriver
Library     SeleniumLibrary
*** Variables ***

*** Test Cases ***
LoginTest

    open browser    https://salesforce.com      chrome
    close browser

*** Keywords ***
