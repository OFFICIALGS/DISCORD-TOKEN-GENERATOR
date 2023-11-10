import requests, colorama, tls_client, os, random, tasks
from tasks import *
from colorama import Fore
import threading
from threading import Lock
import json

good = Fore.LIGHTGREEN_EX+'[+]'+Fore.RESET
bad = Fore.LIGHTRED_EX+'[-]'+Fore.RESET
fpg = Fore.LIGHTBLUE_EX+'[~]'+Fore.RESET
solved = Fore.LIGHTCYAN_EX+'[*]'+Fore.RESET
config = json.load(open('config.json','r'))
proxy = config['proxy']
gened = 0
def generate_names():
    lt = 'x', 'X', 'y', 'Y', 'z', 'Z', 'M', 'm', 'cl'
    name = 'blackwool'
    return f"{name}{random.choice(lt)}{random.randint(00000, 99999999)}"
def generate_email():
    namees = generate_names()
    emaill = f"{namees}+bw@gmail.com"
def generate():
    session = tls_client.Session(

    client_identifier="chrome112",

    random_tls_extension_order=True

)
    cap_key = config['key']
    cap_service = config['service']
    names = generate_names()
    headers = {
            'Accept': '*/*',
            'Accept-Language': 'es-ES,es;q=0.9',
            'Connection': 'keep-alive',
            'Referer': 'https://discord.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-GPC': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'X-Track': 'eyJvcyI6IklPUyIsImJyb3dzZXIiOiJTYWZlIiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKElQaG9uZTsgQ1BVIEludGVybmFsIFByb2R1Y3RzIFN0b3JlLCBhcHBsaWNhdGlvbi8yMDUuMS4xNSAoS0hUTUwpIFZlcnNpb24vMTUuMCBNb2JpbGUvMTVFMjQ4IFNhZmFyaS82MDQuMSIsImJyb3dzZXJfdmVyc2lvbiI6IjE1LjAiLCJvc192IjoiIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfZG9tYWluX2Nvb2tpZSI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk5OTksImNsaWVudF9ldmVudF9zb3VyY2UiOiJzdGFibGUiLCJjbGllbnRfZXZlbnRfc291cmNlIjoic3RhYmxlIn0',
        }

    response = session.get('https://discord.com/api/v9/experiments', headers=headers, proxy=proxy)
    if response.status_code == 200:
            data = response.json()
            fingerprint = data["fingerprint"]
    else:
            print(f"{bad}Error Occured While Getting FingerPrint | {response.text}")
    invite_code = config['invite']
    captcha_code = 'P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hKdwYXNza2V5xQbV'
    cap = solve(cap_key,cap_service)
    print(f"{solved}Solved Captcha | {captcha_code}")
    gcap_respo = cap.get('gcap')

    headers = {
            'authority': 'discord.com',
            'accept': '*/*',
            'accept-language': 'es-ES,es;q=0.9',
            'referer': 'https://discord.com/',
            'origin': 'https://discord.com',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Brave";v="114"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'x-track': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImZyLUZSIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTE0LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk5OTksImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
            'x-fingerprint': fingerprint
        }
    payload = {
            'consent': True,
            'global_name': names,
            'unique_username_registration': True,
            'fingerprint': fingerprint,
            'captcha_key': gcap_respo,
            'invite': invite_code
        }
    response = session.post('https://discord.com/api/v9/auth/register', headers=headers, json=payload, proxy=proxy)
    if "token" not in response.text:
        print(f"{bad}Error On Getting Token | {response.text}")
    token = response.json().get('token')
    if token == None:
        print(f"{bad}Token Is Null | {response.text}")
    else:
        print(f"{good}Generated Token | {token} | Generated  Till Now!")
        with open('token.txt', 'a') as file:
            file.write(f"{token}\n")
def run():
    while True:
        generate()
with open("config.json") as f:
    data = json.load(f)
num_threads = data.get('threads', 100)
threads = []
for i in range(int(num_threads)):
    thread = threading.Thread(target=run, name=f"BOOSTER-{i+1}")
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()