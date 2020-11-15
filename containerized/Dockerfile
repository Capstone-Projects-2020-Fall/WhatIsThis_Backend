FROM tensorflow/tensorflow:latest-py3
WORKDIR /server
COPY . /server
RUN apt-get update
RUN apt-get install 'ffmpeg'\
    'libsm6'\ 
    'libxext6'  -y
RUN pip install keras==2.2.5
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "./app.py"]