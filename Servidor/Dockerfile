FROM ubuntu:20.04
MAINTAINER LRHH
RUN apt-get update
RUN apt -y install default-jdk
RUN apt-get -y install ant
RUN apt-get -y install automake bison flex g++ git libboost-all-dev libevent-dev libssl-dev libtool make pkg-config
RUN apt-get -y install thrift-compiler
RUN apt -y install git
RUN cd /home/
RUN git clone https://github.com/LuisR7210/CalculadoraThrift
RUN cd CalculadoraThrift/Servidor/
RUN ant compile


EXPOSE 