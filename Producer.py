from kafka import KafkaProducer
from time import sleep
from json import dumps
import pandas as pd


try:
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                             value_serializer=lambda x: dumps(x).encode('utf-8'))
    df  = pd.read_csv('C:/Users/User/Desktop/VSCpython/kafka/load_archive.csv')
except Exception as e:
    print("An error occurred while initializing the producer", e)
    producer = None
    

if producer is not None:
    for i in range(df.shape[0]):
        
        try:
            
            total_load_data = df[['datetime','Ptot(kW)']].iloc[i].to_dict()
            producer.send('Ptot', value=total_load_data)
            phaseA_load_data = df[['datetime','Pa(kW)']].iloc[i].to_dict()
            producer.send('Pa', value=phaseA_load_data)
            print(total_load_data)
            sleep(10)
        except Exception as e:
            print("An error occurred while sending data to Kafka:", e)

if producer:
    try:
        producer.flush()
    except Exception as e:
        print("An error occurred while flushing the producer:", e)
producer.close()