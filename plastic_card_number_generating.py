"""
Project name : Generate plastic card number
Author : Khusanboy Sobirjonov
Create date : 1/09/2023 09:07 PM
Telegram : @uzbek_coder_2022
"""
import random  
import datetime 
import secrets 

def PlasticCard():
    """
    Use it.
    """
        
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    
    today = datetime.datetime.now()
    day = today.month
    year = today.year
    
    plastic_card_number = str(year) + '-' + '-'.join([''.join((secrets.choice(digits)) for i in range(4)) for j in range(3)])
    
    validity_period = f"{str(day).zfill(2)}/{year%100 + 5}"
    
    print(f"Plastic card number : {plastic_card_number}"
          f"\nValidity period : {validity_period}")

print(PlasticCard())


    
    
    
    
    
    
    
    
    
    