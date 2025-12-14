https://docs.aws.amazon.com/lambda/latest/dg/python-logging.html#python-logging-advanced


I think just using stdout as part of ecs / kubernetes and sending that to cloudwatch is probably better than watchtower


When running Python applications on AWS Lambda or as containers on ECS/EKS, logs written to stdout or stderr are automatically captured and streamed to CloudWatch Logs by the respective AWS service. No additional configuration within the Python application is typically required beyond using standard print() statements or the Python logging module to output to console. 



https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-metrics.html


Using ECS with fargate hosting has the additional benefit of logging to cloudwatch


https://docs.aws.amazon.com//eks/latest/userguide/control-plane-logs.html


ECS is definitely closer than EC2 and running a docker container. I think we should switch to ECS as an intermediary.

EKS is definitely on the expensive end but ECS is about the same as EC2 + docker container.

