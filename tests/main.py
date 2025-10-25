import logging
from datetime import datetime
from typing import List, Dict, Any
from multiprocessing import Process, Queue
from queue import Empty
import json
import requests

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_data(data: Dict[str, Any]) -> Dict[str, Any]:
    if 'timestamp' in data:
        data['timestamp'] = datetime.fromisoformat(data['timestamp'])
    return data

def worker(queue: Queue) -> None:
    while True:
        try:
            item = queue.get(timeout=10)
            processed_data = process_data(item)
            logging.info(f"Processed data: {processed_data}")
        except Empty:
            logging.warning("Queue is empty, stopping worker.")
            break
        except Exception as e:
            logging.error(f"Error processing data: {e}")

def fetch_data(url: str) -> List[Dict[str, Any]]:
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Failed to fetch data: {e}")
        return []

def main() -> None:
    data_url = "https://api.example.com/data"
    data = fetch_data(data_url)
    
    queue = Queue()
    for item in data:
        queue.put(item)
    
    processes = [Process(target=worker, args=(queue,)) for _ in range(4)]
    for p in processes:
        p.start()
    
    for p in processes:
        p.join()

if __name__ == "__main__":
    main()