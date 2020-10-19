*** Settings ***
Library  SeleniumLibrary
Library  Webdriver

*** Variables ***

*** Test Cases ***
LoginTest
    #Create Webdriver    chrome    executable_path=C:\Users\CHANDRASEKHARJANGA\PycharmProjects\TestProject\Drivers\chromedriver.exe
    open browser    https://salesforce.com      chrome
    wait until element contains  salesforce
    close browser

*** Keywords ***
