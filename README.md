# MQTT (Message Queuing Telemetry Transport) on Esp32
### Made in Micropython

<div align="center">     
    ![Coding.](https://media.giphy.com/media/pALw8LdftuqAw/giphy.gif "MQTT gif")  
</div>

![Coding.](https://media.giphy.com/media/pALw8LdftuqAw/giphy.gif "MQTT gif") 


### In this repo you will a Python Code that connects the Esp32 to [Hive MQ broker](https://www.hivemq.com/demos/websocket-client) to use MQTT:

MQTT is a __lightweight and efficient messaging protocol designed for low-bandwidth, high-latency, or unreliable networks__. It was originally developed by IBM in the late 1990s and has since become an open standard widely used in the Internet of Things (IoT), home automation, and other scenarios where devices or applications need to communicate and exchange information 💁.

### __Her features are:__

* __Publish/Subscribe model:__ MQTT follows a publish/subscribe messaging pattern where devices (or clients) can publish messages to specific topics, and other devices can subscribe to those topics to receive the messages. This decoupled communication model is highly scalable and flexible 📢.

* __Quality of Service (QoS) levels:__ MQTT supports different QoS levels to ensure message delivery reliability. There are three QoS levels:
1. __QoS 0:__ At most once delivery (fire and forget).
2. __QoS 1:__ At least once delivery (guaranteed delivery but may result in duplicates).
3. __QoS 2:__ Exactly once delivery (highest guarantee but requires more overhead).

* __Last Will and Testament (LWT):__ MQTT allows clients to specify a "last will" message to be sent by the broker to a specified topic in case the client unexpectedly disconnects. This is useful for detecting when a device goes offline 📴.

* __Retained messages:__ MQTT brokers can retain the last message published on a specific topic. When a new client subscribes to that topic, it immediately receives the most recent message 🔗.
