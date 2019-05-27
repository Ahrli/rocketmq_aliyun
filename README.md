# MQ Python HTTP SDK  
Alyun MQ Documents: http://www.aliyun.com/product/ons

source https://github.com/aliyunmq/mq-http-python-sdk

Aliyun MQ Console: https://ons.console.aliyun.com

Documentation https://libraries.io/pypi/mq-http-sdk

## Requires

Python version: [3.0,3.7]

## Install sdk by pip

1. install pip, see [document](https://pip.pypa.io/en/stable/installing/)
2. install sdk by pip

```bash
pip install mq_http_aliyun_sdk
```
# 示例
## consumer
#初始化 client
mq_client = MQClient(
    #设置HTTP接入域名（此处以公共云生产环境为例）
    "xxxxxx",
    #AccessKey 阿里云身份验证，在阿里云服务器管理控制台创建
    "xxxxxx",
    #SecretKey 阿里云身份验证，在阿里云服务器管理控制台创建
    "xxxxxx"
    )
#所属的 Topic
topic_name = "xxxxxxx"
#Topic所属实例ID，默认实例为空None
instance_id = "xxxxxx"
group_id = 'xxxxxxxx'
consumer = mq_client.get_consumer(instance_id, topic_name, group_id)

## Notice

MQClient, Producer, Consumer are not thread safe, please use multi instance in mutli thread.

## Samples

[Publish Message](https://github.com/aliyunmq/mq-http-samples/blob/master/python/producer.py)

[Consume Message](https://github.com/aliyunmq/mq-http-samples/blob/master/python/consumer.py)
