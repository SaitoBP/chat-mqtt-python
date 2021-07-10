# MQTT Chat with Python

This is a simple chat-like application using a mosquitto broker to exchange messages between clients. The clients are python programs that read and write messages to the broker.

## Requirements

- Python 3.9
- Docker

## How to run the program

1 - After cloning the repository you can simply run

```shell
docker-compose up
```

This will initiate our mosquitto broker

2 - Open the terminal and install the dependencies

```python
pip install paho-mqtt
```

3 - Execute the main file

```python
main.py
```

You can open as many clients as you want! Now just start chatting
