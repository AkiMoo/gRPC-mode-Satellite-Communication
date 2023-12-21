from concurrent import futures
import os
import time
import logging
import threading
import queue
import json
import grpc
import comm_pb2_grpc as comm_pb2_grpc
import comm_pb2 as comm_pb2

def send_stream():
    with open('locationData.txt','rb') as f: # 需要传输的文件名字，必须要在当前文件夹路径
        size = os.path.getsize('locationData.txt')/1024 # 需要传输的文件名字
        n = 0
        while True:
            content = f.read(1024)
            if content:
                n = n+1
                print('Processing:{}%'.format(round(n/size*100,2)))
                yield comm_pb2.request(data = content)
            else:
                break

def run1():
    with grpc.insecure_channel('localhost:50001',options=[
        ('grpc.max_send_message_length',256*1024*1024),
        ('grpc.max_receive_message_length',256*1024*1024),
    ]) as channel:
        client = comm_pb2_grpc.StreamFileStub(channel)
        response = client.ClientStream(send_stream())
        print(response.message)

def run2():
    with grpc.insecure_channel('localhost:50002',options=[
        ('grpc.max_send_message_length',256*1024*1024),
        ('grpc.max_receive_message_length',256*1024*1024),
    ]) as channel:
        client = comm_pb2_grpc.StreamFileStub(channel)
        response = client.ClientStream(send_stream())
        print(response.message)

def run3():
    with grpc.insecure_channel('localhost:50003',options=[
        ('grpc.max_send_message_length',256*1024*1024),
        ('grpc.max_receive_message_length',256*1024*1024),
    ]) as channel:
        client = comm_pb2_grpc.StreamFileStub(channel)
        response = client.ClientStream(send_stream())
        print(response.message)

def run4():
    with grpc.insecure_channel('localhost:50004',options=[
        ('grpc.max_send_message_length',256*1024*1024),
        ('grpc.max_receive_message_length',256*1024*1024),
    ]) as channel:
        client = comm_pb2_grpc.StreamFileStub(channel)
        response = client.ClientStream(send_stream())
        print(response.message)

def run5():
    with grpc.insecure_channel('localhost:50005',options=[
        ('grpc.max_send_message_length',256*1024*1024),
        ('grpc.max_receive_message_length',256*1024*1024),
    ]) as channel:
        client = comm_pb2_grpc.StreamFileStub(channel)
        response = client.ClientStream(send_stream())
        print(response.message)


if __name__=='__main__':
    logging.basicConfig()
    run1()
    run2()
    run3()
    run4()
    run5()