FROM python:3.7-stretch

RUN pip install ws4py
RUN pip install flask
RUN git clone https://github.com/NATIX-io/iofog-python-sdk.git /src/iofog-python-sdk
WORKDIR /src/iofog-python-sdk
RUN python setup.py install
RUN pip install numpy
RUN pip install -U flask-cors
COPY . /src
WORKDIR /src
EXPOSE 5000

CMD ["python", "/src/index.py"]
