*** Settings ***
Library    currency_converter.py    

*** Test Cases ***
Demo how to call python function
    ${thb} =     Convert Usd To    THB    20
    Log    ${thb}
