from confluent_kafka import Consumer, KafkaError
import json
from datetime import datetime

def json_deserializer(data):
    return json.loads(data.decode('utf-8'))

def create_consumer(topic_name, group_id):
    # Consumer configuration
    conf = {
        'bootstrap.servers': 'localhost:29092,localhost:29093,localhost:29094',
        'group.id': group_id,
        'auto.offset.reset': 'earliest',
        'enable.auto.commit': True
    }

    # Create consumer instance
    consumer = Consumer(conf)
    
    # Subscribe to topic
    consumer.subscribe([topic_name])
    return consumer

def process_message(msg):
    """Process the consumed message"""
    try:
        # Extract message details
        key = msg.key().decode('utf-8') if msg.key() else None
        value = json.loads(msg.value().decode('utf-8'))
        partition = msg.partition()
        offset = msg.offset()
        timestamp = datetime.fromtimestamp(msg.timestamp()[1] / 1000.0)

        print(f'\nReceived message:')
        print(f'Key: {key}')
        print(f'Value: {value}')
        print(f'Partition: {partition}')
        print(f'Offset: {offset}')
        print(f'Timestamp: {timestamp}')
        
        return True
    except Exception as e:
        print(f'Error processing message: {str(e)}')
        return False

def main():
    topic_name = 'test-topic'
    group_id = 'test-consumer-group'
    
    try:
        # Create consumer
        consumer = create_consumer(topic_name, group_id)
        print(f'Starting consumer... listening to topic: {topic_name}')
        
        # Consume messages
        while True:
            msg = consumer.poll(1.0)  # timeout in seconds
            
            if msg is None:
                continue
            
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    print('Reached end of partition')
                else:
                    print(f'Error: {msg.error()}')
            else:
                process_message(msg)
            
    except KeyboardInterrupt:
        print('\nConsumer stopped by user')
    except Exception as e:
        print(f'Error in consumer: {str(e)}')
    finally:
        # Close consumer
        try:
            consumer.close()
            print('Consumer closed successfully')
        except Exception as e:
            print(f'Error closing consumer: {str(e)}')

if __name__ == '__main__':
    main()
