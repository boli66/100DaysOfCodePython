from libraries.FileIO import hson

flavours ={
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "price": 1.50
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150,
        },
        "price": 2.50
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
        },
        "price": 3.0
    }
}
resources = hson.hson("data.txt",{}).get()
coins = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickel": 0.05,
    "penny":0.01,



}