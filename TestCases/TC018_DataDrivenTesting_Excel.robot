*** Settings ***
Library     SeleniumLibrary
Library     DataDriver  ../TestData/LoginData.xlsx  sheet_name  =   Sheet1
Resource    ../Resources/login_resources.robot

Suite Setup     Open My Browser
Suite Teardown  Close Browsers
Test Template   InvalidLogin

*** Test Cases ***
LoginTestWithExcel  ${username} and ${password}            #supports robotframework-datadriver 0.3.1

*** Keywords ***
InvalidLogin
    [Arguments]     ${username}    ${password}          #These attributes should match with excel header names
    Enter UserName  ${username}
    ENTER PASSWORD  ${password}
    Click Login Button
    Error message for invalid login