# **Queue-based Microservice 

This will simulate inventory verification requests from incoming orders in an e-commerce application as part of an order processing workflow. Step Functions will send inventory verification requests to a queue on SQS. An AWS Lambda function will act as your inventory microservice that uses a queue to buffer requests. When it retrieves a request, it will check inventory and then return the result to Step Functions



>## Reference Architecture 

![image](https://user-images.githubusercontent.com/50748311/134581851-4e0d5b5a-920d-46a7-add1-a2413e9ea29a.png)


![image](https://user-images.githubusercontent.com/50748311/134581981-de82d6db-1ac5-4691-acda-7f3ddbd3f3dc.png)
