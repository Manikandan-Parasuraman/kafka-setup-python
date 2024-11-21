from confluent_kafka import Producer
import json
import time
from datetime import datetime

def delivery_report(err, msg):
    """Callback function for message delivery reports"""
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} partition [{msg.partition()}] at offset {msg.offset()}')

# Create producer instance
producer_conf = {
    'bootstrap.servers': 'localhost:29092,localhost:29093,localhost:29094',
    'client.id': 'python-producer'
}

producer = Producer(producer_conf)

def send_message(topic_name, key, value):
    try:
        # Create message data
        data = {
            'key': key,
            'value': value,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # Convert data to JSON string
        message = json.dumps(data)
        
        # Send message
        producer.produce(
            topic=topic_name,
            key=str(key).encode('utf-8'),
            value=message.encode('utf-8'),
            callback=delivery_report
        )
        
        # Flush to ensure message is sent
        producer.flush()
        return True
    
    except Exception as e:
        print(f'Error sending message: {str(e)}')
        return False

def main():
    topic_name = 'test-topic'
    
    # Send some test messages
    for i in range(10):
        key = f'key_{i}'
        value = f'test message {i}'
        send_message(topic_name, key, value)
        time.sleep(1)  # Wait for 1 second between messages

if __name__ == '__main__':
    try:
        main()
    finally:
        # Close producer
        producer.flush()  # Ensure all messages are sent
        print('Producer closed successfully')
