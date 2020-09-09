*** Settings ***
Library     SeleniumLibrary
Resource    ../Resources/login_resources.robot
Library     DataDriver  ../TestData/LoginData.xlsx  sheet_name  =   Sheet1

Suite Setup     Open My Browser
Suite Teardown  Close Browsers
Test Template   InvalidLogin

#*** variables ***
#${username}=null
#${password}=null

*** Test Cases ***
LoginTestWithExcel  ${username}  ${password}            #supports robotframework-datadriver 0.3.1

*** Keywords ***
InvalidLogin
    [Arguments]     ${username}    ${password}          #These attributes should match with excel header names
    Enter UserName  ${username}
    ENTER PASSWORD  ${password}
    Click Login Button
    Error message for invalid login