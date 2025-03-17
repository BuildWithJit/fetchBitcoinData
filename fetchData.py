import logging
import os

import requests
from dotenv import load_dotenv

logging.basicConfig(filename="status.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def get_url(backend_url: str, endpoint: str):
    if backend_url.endswith("/"):
        print(f"{backend_url}{endpoint}")
        return f"{backend_url}{endpoint}"
    else:
        print(f"{backend_url}/{endpoint}")
        return f"{backend_url}/{endpoint}"


def get_token(url: str, username: str, password: str):

    response = requests.post(
        url, json={"username": username, "password": password}, headers={"Content-Type": "application/json"}
    )
    if response.status_code == 200:
        return response.json()["token"]
    else:
        raise Exception(f"Failed to get token: {response.status_code} {response.text}")


def get_data(url: str, token: str):
    response = requests.get(url, headers={"Authorization": f"Bearer {token}"})
    if response.status_code == 200:
        return logging.info("We have successfully fetch the data for bitcoin and stored in database")
    else:
        raise logging.error(f"We failed to fetch data and store in database")


if __name__ == "__main__":

    load_dotenv(".env.local")

    backend_url = os.getenv("backend_url")
    token_endpoint = os.getenv("token_endpoint")
    data_endpoint = os.getenv("data_endpoint")
    username = os.getenv("username")
    password = os.getenv("admin_password")

    token_url = get_url(backend_url, token_endpoint)
    token = get_token(token_url, username, password)
    data_url = get_url(backend_url, data_endpoint)
    data = get_data(data_url, token)
