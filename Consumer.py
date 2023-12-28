
from kafka import KafkaConsumer
from json import loads, dumps
import pandas as pd

try:
    consumer = KafkaConsumer(bootstrap_servers=['localhost:9092'],
                             value_deserializer=lambda x: loads(x.decode('utf-8')),
                             request_timeout_ms = 10000)
    consumer.subscribe(['Ptot','Pa'])
except Exception as e:
    print("An error occurred while initializing the Kafka consumer:", e)
    consumer = None


if consumer is not None:
    
    for message in consumer:
        # data =  pd.DataFrame.from_dict(message.value,orient='index').T
        print('topic:',message.topic,'value:', message.value)
        print(type(message))
    #         try:
    #             massage_id += 1
    #             new_data = {'Id': massage_id}
    #             new_data.update(message.value)
    #             final_data = dumps(new_data)
    #             print(new_data)
    #         except Exception as e:
    #             print("exception:", e)