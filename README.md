# Kafka High-Availability Cluster with Python Integration

A production-ready Kafka setup with high availability, multiple brokers, monitoring, and Python integration.

## Features

- **High Availability**
  - 3 Kafka brokers for fault tolerance
  - ZooKeeper for cluster coordination
  - Replication factor of 3 for data redundancy

- **Monitoring**
  - Kafka UI for real-time cluster monitoring
  - Topic management interface
  - Consumer group tracking
  - Message browser

- **Python Integration**
  - Producer with delivery guarantees
  - Consumer with proper error handling
  - Message serialization and deserialization
  - Consumer group support

## Prerequisites

- Docker and Docker Compose
- Python 3.7+
- pip (Python package manager)
- 4GB+ RAM available for the Kafka cluster

## Directory Structure

```
kafka-setup-python/
├── docker-compose.yml    # Kafka cluster configuration
├── producer.py          # Python producer example
├── consumer.py         # Python consumer example
├── requirements.txt    # Python dependencies
└── README.md          # Documentation
```

## Quick Start

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd kafka-setup-python
   ```

2. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the Kafka Cluster**
   ```bash
   docker-compose up -d
   ```

4. **Verify the Setup**
   - Open Kafka UI: http://localhost:8080
   - Check if all brokers are online
   - Verify the test-topic is created

5. **Run the Example Scripts**
   - In one terminal:
     ```bash
     python consumer.py
     ```
   - In another terminal:
     ```bash
     python producer.py
     ```

## Detailed Configuration

### Kafka Cluster

- **Brokers**
  - Broker 1: localhost:29092 (external), kafka1:9092 (internal)
  - Broker 2: localhost:29093 (external), kafka2:9093 (internal)
  - Broker 3: localhost:29094 (external), kafka3:9094 (internal)

- **ZooKeeper**
  - Port: 2181
  - Tick Time: 2000ms

- **Topic Configuration**
  - Name: test-topic
  - Partitions: 3
  - Replication Factor: 3
  - Auto-create enabled

### Python Components

#### Producer Features
- Message delivery confirmation
- Custom partitioning
- JSON serialization
- Error handling and retries
- Proper cleanup on exit

#### Consumer Features
- Consumer group support
- From-beginning consumption
- JSON deserialization
- Proper error handling
- Graceful shutdown

## Monitoring

### Kafka UI Features
- **URL**: http://localhost:8080
- **Capabilities**:
  - Topic management (create, delete, configure)
  - Consumer group monitoring
  - Message browsing and searching
  - Broker configuration viewing
  - Partition distribution visualization

## Common Operations

### Managing Topics

1. **Create a Topic**
   ```bash
   docker-compose exec kafka1 kafka-topics --create \
     --bootstrap-server kafka1:9092 \
     --topic new-topic \
     --partitions 3 \
     --replication-factor 3
   ```

2. **List Topics**
   ```bash
   docker-compose exec kafka1 kafka-topics --list \
     --bootstrap-server kafka1:9092
   ```

3. **Describe a Topic**
   ```bash
   docker-compose exec kafka1 kafka-topics --describe \
     --bootstrap-server kafka1:9092 \
     --topic test-topic
   ```

### Testing the Setup

1. **Console Producer**
   ```bash
   docker-compose exec kafka1 kafka-console-producer \
     --bootstrap-server kafka1:9092 \
     --topic test-topic
   ```

2. **Console Consumer**
   ```bash
   docker-compose exec kafka1 kafka-console-consumer \
     --bootstrap-server kafka1:9092 \
     --topic test-topic \
     --from-beginning
   ```

## Troubleshooting

1. **Broker Connection Issues**
   - Verify all containers are running:
     ```bash
     docker-compose ps
     ```
   - Check broker logs:
     ```bash
     docker-compose logs kafka1
     ```

2. **Python Script Issues**
   - Ensure all dependencies are installed
   - Check broker connectivity
   - Verify topic exists
   - Check consumer group ID

3. **Resource Issues**
   - Ensure enough memory is available
   - Monitor CPU usage
   - Check disk space

## Maintenance

1. **Scaling**
   - Add more brokers by updating docker-compose.yml
   - Increase partition count for topics
   - Adjust replication factor

2. **Cleanup**
   ```bash
   # Stop the cluster
   docker-compose down

   # Remove all data
   docker-compose down -v
   ```

## Security Considerations

Current setup is for development. For production:
1. Enable SSL/TLS encryption
2. Implement SASL authentication
3. Configure ACLs
4. Use secure passwords
5. Implement network isolation

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

### GNU GPL v3.0 Summary

Permissions:
- Commercial use
- Distribution
- Modification
- Patent use
- Private use

Conditions:
- Disclose source
- License and copyright notice
- Same license
- State changes

Limitations:
- Liability
- Warranty

For the full license text, visit: https://www.gnu.org/licenses/gpl-3.0.en.html
