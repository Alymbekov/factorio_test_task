import json
from scraping.worker import WorkerBroker

url = "https://factorioprints.com/top"
task = {'url': url}
task = json.dumps(task)
wb = WorkerBroker('worker-queue', 10)
message = json.dumps(task)
wb.produce_message(message=message, priority=1)
