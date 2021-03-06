#!/usr/bin/env python
# coding=utf8

from mq_http_aliyun_sdk.mq_exception import MQExceptionBase
from mq_http_aliyun_sdk.mq_producer import *
from mq_http_aliyun_sdk.mq_client import *

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

#长轮询表示如果topic没有消息则请求会在服务端挂住3s，3s内如果有消息可以消费则立即返回
#长轮询时间3秒（最多可设置为30秒）
wait_seconds = 3
#一次最多消费3条(最多可设置为16条)
batch = 3
print("%sConsume And Ak Message From Topic%s\nTopicName:%s\nMQConsumer:%s\nWaitSeconds:%s\n" % (10 * "=", 10 * "=", topic_name, group_id, wait_seconds))
while True:
    try:
        #长轮询消费消息
        recv_msgs = consumer.consume_message(batch, wait_seconds)
        for msg in recv_msgs:
            a = msg.message_body
            print('\n11======', a)
            time.sleep(400)
            print('jieshu')
            # print ("Receive, MessageId: %s\nMessageBodyMD5: %s \
            #                   \nMessageTag: %s\nConsumedTimes: %s \
            #                   \nPublishTime: %s\nBody: \
            #                   \nNextConsumeTime: %s \
            #                   \nReceiptHandle: %s" % \
            #                  (msg.message_id, msg.message_body_md5,
            #                   msg.message_tag, msg.consumed_times,
            #                   msg.publish_time,
            #                   msg.next_consume_time, msg.receipt_handle))

    except MQExceptionBase as e:
        if e.type == "MessageNotExist":
            print ("No new message! RequestId: %s" % e.req_id)
            continue

        print("Consume Message Fail! Exception:%s\n" % e)
        time.sleep(2)
        continue
    #
    # #5分钟之内若不确认消息消费成功，则消息会重复消费
    # try:
    #     receipt_handle_list = [msg.receipt_handle for msg in recv_msgs]
    #     consumer.ack_message(receipt_handle_list)
    #     print("Ak %s Message Succeed.\n\n" % len(receipt_handle_list))
    # except MQExceptionBase as e:
    #     print ("\nAk Message Fail! Exception:%s" % e)
    #     #某些消息的句柄可能超时了会导致确认不成功
    #     if e.sub_errors:
    #       for sub_error in e.sub_errors:
    #         print ("\tErrorHandle:%s,ErrorCode:%s,ErrorMsg:%s" % (sub_error["ReceiptHandle"], sub_error["ErrorCode"], sub_error["ErrorMessage"]))