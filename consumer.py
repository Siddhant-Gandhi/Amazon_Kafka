from flask import Flask
from kafka import KafkaConsumer
import os

app = Flask(__name__)

@app.route('/consume', methods=['GET'])
def consume_messages():
    topic_name = os.environ['topic_name']
    bootstrap_servers = os.environ['bootstrap_servers'] 
    consumer_timeout_ms = 1000

    consumer = KafkaConsumer(
        topic_name,
        auto_offset_reset='earliest',
        bootstrap_servers=bootstrap_servers,
        api_version=(0, 10, 1),
        consumer_timeout_ms=consumer_timeout_ms,
        value_deserializer=lambda x: x.decode('utf-8')  # Decode bytes to string
    )
    messages = []
    for msg in consumer:
        messages.append(msg.value)

    consumer.close()

    return {'messages': messages}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3012, debug=True)
