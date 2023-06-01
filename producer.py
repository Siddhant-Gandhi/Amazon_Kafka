from flask import Flask, request
from kafka import KafkaProducer, KafkaConsumer
from json import dumps
import os
app = Flask(__name__)

bootstrap_servers = os.environ['bootstrap_servers']  # Update with your bootstrap servers
topic_name = os.environ['topic_name']  # Update with your topic name

# Kafka producer setup
producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,

    api_version=(0, 10, 1)
)


@app.route('/send', methods=['POST'])
def send_message():
    message = request.get_json()['message']
    producer.send(topic_name, message.encode())
    return 'Message sent success'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
