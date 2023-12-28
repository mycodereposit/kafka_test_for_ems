# dependencies  
1. apache-kafka_2.12-3.6.1 Windows version with setup as shown in https://fnote.medium.com/setting-up-apache-kafka-in-windows-1835141c3a32
2. python-kafka using pip install kafka-python
3. eclipse ide with gradle extension (for java-kafka) setup as https://www.conduktor.io/kafka/creating-a-kafka-java-project-using-gradle-build-gradle/
# running procedure 
1. start zookeeper using command `zookeeper-server-start.bat C:\kafka\config\zookeeper.properties` in windows cmd. Noted that argument must be the fullpath to zookeeper.properties file
![image](https://github.com/mycodereposit/kafka_test_for_ems/assets/126697725/476248c4-0fce-426d-8210-9d8866489254)
2. start kafka using command `kafka-server-start.bat C:\kafka\config\server.properties` in another windows cmd. Noted that argument must be the fullpath to server.properties file
![image](https://github.com/mycodereposit/kafka_test_for_ems/assets/126697725/71bff0c5-2f71-4184-ad14-0cb10bbb772a)
3. run Producer.py and Consumer.py respectively
# common error
## kafka zookeeper and server
1. NodeExists
  - go to data/zookeeper and data/kafka then empties both folders and start running again.
## python kafka
1. NoBrokersAvailable
  - start zookeeper and kafka server before running python kafka
## java kafka
1. org.slf4j can not be resolved
  - go to build.gradle right click -> gradle -> refresh gradle project and rerun build.gradle
![image](https://github.com/mycodereposit/kafka_test_for_ems/assets/126697725/bbc34c93-7675-4303-b253-b031509af04e)

# note
python source codes are modified from https://github.com/kishlayjeet/Stock-Market-Real-Time-Data-Pipeline-with-Apache-Kafka-and-Cassandra
