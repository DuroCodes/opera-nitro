import requests
import threading
import time
import os
import uuid


os.system('cls' if os.name == 'nt' else 'clear')

red = '\x1b[31m(-)\x1b[0m'
blue = '\x1b[34m(+)\x1b[0m'
green = '\x1b[32m(+)\x1b[0m'
yellow = '\x1b[33m(!)\x1b[0m'


def get_timestamp():
    time_idk = time.strftime('%H:%M:%S')
    timestamp = f'[\x1b[90m{time_idk}\x1b[0m]'
    return timestamp


def gen():
    while True:
        url = "https://api.discord.gx.games/v1/direct-fulfillment"
        headers = {
            "Content-Type": "application/json",
            "Sec-Ch-Ua": '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0",
        }

        data = {
            "partnerUserId": str(uuid.uuid4())
        }

        try:
            response = requests.post(
                url, json=data, headers=headers, timeout=5)

            if response.status_code == 200:
                token = response.json().get('token')
                if token:
                    link = f"https://discord.com/billing/partner-promotions/1180231712274387115/{token}"

                    with open("links.txt", "a") as f:
                        f.write(f"{link}\n")
                    print(f"{get_timestamp()} {green} Generated Promo Link : {link}")
            elif response.status_code == 429:
                print(f"{get_timestamp()} {yellow} Rate Limited")
            else:
                print(f"{get_timestamp()} {red} Error : {response.status_code}")
        except Exception as e:
            print(f"{get_timestamp()} {red} Error : {e}")


def main():
    threads = int(input(f"{get_timestamp()} {blue} Threads : "))
    for i in range(threads):
        threading.Thread(target=gen).start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        os._exit(0)


if __name__ == "__main__":
    main()
