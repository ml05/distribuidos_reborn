FROM python:3.8.10
COPY . /reader
WORKDIR /reader
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 install -U flask-cors
#RUN python3 -m grpc_tools.protoc -I protobuffs --python_out=. --grpc_python_out=. protobuffs/sales_records.proto
ENTRYPOINT ["python3"]
CMD ["-u","main.py"]