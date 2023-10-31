#!python3
"""
Create a function that converts the price of Bitcoin into Canadian Dollars .
The function will require 2 input parameters:
float: amount of currency being converted

return: float value in Canadian Dollars
You will make use of a local variable called "currBTC"
currBTC shows that the conversion is 1 btc = 45000 cad

Sample assertions:

assert btcTocad(1) == 45000
(2 points) 
"""

def btcTocad(a):
    if type(a) is str:
        return 'error'

    return a * 45000

"""
This checks to see if you are running the program as the main script or
if it is imported by another program.
If this py file is imported by another program, then the commands below
are not executed.
"""
if __name__ == "__main__":
    assert btcTocad(1) == 45000
    assert btcTocad(2.5) == 112500
    assert btcTocad('one') == 'error'