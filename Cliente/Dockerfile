FROM ubuntu:20.04
MAINTAINER LRHH

RUN apt-get update
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata
RUN apt-get -y install automake bison flex g++ git libboost-all-dev libevent-dev libssl-dev libtool make pkg-config
RUN apt-get -y install thrift-compiler
RUN apt -y install python3-pip
RUN pip3 install thrift
RUN apt -y install git
WORKDIR /home/
RUN git clone https://github.com/LuisR7210/CalculadoraThrift
WORKDIR CalculadoraThrift/Cliente/
RUN thrift -r --gen py ThriftCalculadora.thrift

EXPOSE 8080
WORKDIR /home/CalculadoraThrift/Cliente/
CMD python3 ClienteCalculadora.py