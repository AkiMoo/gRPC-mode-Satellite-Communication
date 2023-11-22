from concurrent import futures
from PIL import Image
from torchvision import transforms
import os
import time
import logging
import threading
import queue
import json
import grpc
import torch
import torch.nn as nn
import comm_pb2_grpc
import comm_pb2


def send_info():
    message_list = ['9','10','11','12']
    for i in message_list:
        yield comm_pb2.Request(message=i)

def run():
    with grpc.insecure_channel('localhost:50003') as channel:
        client = comm_pb2_grpc.CommStub(channel)
        response = client.Transfer_Both(send_info())
        for i in response:
            print("Got message ", i.message)

if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    run()