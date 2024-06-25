def clear_screen():
    print("\n" * 100)

# https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Guess%20The%20Number
LOGO = """
___________________________________
    _____                      __  
    /    )                   /    )
---/----/----__-------------/----/-
  /    /   /   ) /   /     /    /  
_/____/___(___(_(___/_____(____/___
                   /               
               (_ /                
"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

