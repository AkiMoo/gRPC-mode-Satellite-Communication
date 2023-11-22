from concurrent import futures
import logging
import grpc
import comm_pb2
import comm_pb2_grpc
import time
import pandas
from threading import Thread
import numpy as np

def deliver(message):
    for i in message:
        yield comm_pb2.reply(message=i)

class Communicate(comm_pb2_grpc.CommServicer):
    def Transfer_CtoS(self, request_iterator, context):
        for i in request_iterator:
            print(i.message)
        return comm_pb2.Reply(message='ok')
    
    def Transfer_StoC(self, request, context):
        print(request)
        #message_list = ['100', '101', '102', '103']
        message_list = dataAttain()
        print(message_list)
        for row in message_list:
            for element in row:
                print("Transfer data ",element)
                yield comm_pb2.Reply(message = element) #yield返回的是迭代器

#        print(message_list)
#        for i in message_list:
#            print("Transfer data ",i)
#            yield comm_pb2.Reply(message = i) #yield返回的是迭代器

    def Transfer_Both(self, request_iterator, context):
        for i in request_iterator:
            print('Server got ',i.message)
        for j in ['a','b','c','d']:
            time.sleep(1)
            yield comm_pb2.Reply(message = j) #yield返回的是迭代器

def serve():
    server = grpc.server(futures.ThreadPoolExecutor())
    comm_pb2_grpc.add_CommServicer_to_server(Communicate(), server)
    server.add_insecure_port('[::]:50001')
    server.add_insecure_port('[::]:50002')
    server.add_insecure_port('[::]:50003')
    server.add_insecure_port('[::]:50004')
    server.add_insecure_port('[::]:50005')
    server.start()
    server.wait_for_termination() #阻塞直至终止

def dataAttain():#用一个函数来读表
    tabledata = pandas.read_csv('satellite.csv')
    return tabledata

if __name__ == '__main__':
    logging.basicConfig()
    ## 尝试读入
    # tabledata = pandas.read_csv('satellite.csv')
    # print(tabledata.head())
    serve()