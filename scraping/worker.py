import json
from message_broker.broker import MessageBroker
from scraping.scraping_details import run_scrape_details_and_save_to_db
from scraping.scraping_links import run_scrape_links


class WorkerBroker(MessageBroker):

    def callback(self, channel, method, properties, body):
        print(" [x] Received %r" % body.decode())
        task = json.loads(body.decode())
        links = run_scrape_links("https://factorioprints.com/top")
        for link in links[0:2]:
            run_scrape_details_and_save_to_db(link)
        channel.basic_ack(delivery_tag=method.delivery_tag)
        exit(0)


def run_worker():
    wb = WorkerBroker('worker-queue')
    wb.consume_messages()


if __name__ == '__main__':
    run_worker()
