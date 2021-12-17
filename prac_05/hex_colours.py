"""
CP1404/CP5632 Practical - Suggested Solution
Hexadecimal colour lookup
"""

COLOUR_CODES = {"Black": "#000000", "Bitter Lemon": "#cae00d",
                "Bright Green": "#66ff00", "Cardinal": "#c41e3a",
                "Cerulean Blue": "#2a52be", "Coffee": "#6f4e37",
                "Dark Brown": "#654321", "Dark Sky Blue": "#8cbed6",
                "Golden Yellow": "#ffdf00", "Gray": "#bebebe",}

print(COLOUR_CODES)
colour_name = input("Enter a colour name: ")
while colour_name != "":
    # Note: using the get dictionary method
    # means you will get None if the key is not found
    print("The code for \"{}\" is {}".format(colour_name,
                                             COLOUR_CODES.get(colour_name)))
    colour_name = input("Enter a colour name: ")
    
