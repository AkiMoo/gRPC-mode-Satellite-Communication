from concurrent import futures
from PIL import Image
import os
import time
import logging
import threading
import queue
import json
import grpc
import comm_pb2_grpc as comm_pb2_grpc
import comm_pb2 as comm_pb2

class StreamTest(comm_pb2_grpc.StreamFileServicer):
    def ClientStream(self, request_iterator, context):
        with open("outpu5.txt",'wb') as f: # 写入接收的数据
            for i in request_iterator:
                f.write(i.data)
        print("Finish!")
        file = open('outpu5.txt',"r") # print测试
        content = file.read()
        print(content)
        file.close
        return comm_pb2.response(message = 'ok')
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10),options=[
        ('grpc.max_send_message_length',256*1024*1024),
        ('grpc.max_receive_message_length',256*1024*1024),])
    comm_pb2_grpc.add_StreamFileServicer_to_server(StreamTest(),server)
    server.add_insecure_port('[::]:50005')
    server.start()
    server.wait_for_termination()

if __name__=='__main__':
    logging.basicConfig()
    serve()
    file = open('outpu5.txt',"r")
    content = file.read()
    print(content)
    file.close