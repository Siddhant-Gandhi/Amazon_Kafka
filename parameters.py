import os

# Set environment variables
os.environ['bootstrap_servers'] = 'b-2.sidcluster.gevwho.c21.kafka.us-east-1.amazonaws.com:9092,b-3.sidcluster.gevwho.c21.kafka.us-east-1.amazonaws.com:9092,b-1.sidcluster.gevwho.c21.kafka.us-east-1.amazonaws.com:9092'
os.environ['topic_name'] = 'MSKTutorialTopic1'
