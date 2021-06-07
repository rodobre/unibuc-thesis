import requests
import time

hostname = "http://localhost/api/store"
secret_key = "SECRET KEY"
secret_value = "SECRET VALUE"

if __name__ == '__main__':
	while True:
		r = requests.post(
			hostname,
			headers={"Content-Type": "text/plain", "key": secret_key},
			data=secret_value
		)
		time.sleep(0.1)
