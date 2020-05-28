FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /pandapower_simulation_api
WORKDIR /pandapower_simulation_api
COPY requirements.txt /pandapower_simulation_api/
RUN pip install -r requirements.txt
COPY . /pandapower_simulation_api/
