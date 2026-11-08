import requests
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


def main():
    url = "https://192.168.1.2/answer/api/v1/user/login/email"
    res = requests.post(
        url,
        json={"e_mail": EMAIL, "pass": PASSWORD},
        verify="./certs/me.crt",
        timeout=10,
        headers={"Content-Type": "application/json", "accept": "application/json"},
    )
    print(res.status_code)
    print(res.json())


if __name__ == "__main__":
    main()
