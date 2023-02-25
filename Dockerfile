FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/app
COPY app/requirements.txt /usr/app
RUN pip install -r requirements.txt
COPY . /usr/app
COPY boot.sh /scripts/boot.sh
RUN ["chmod", "+x", "/scripts/boot.sh"]
ENTRYPOINT ["/scripts/boot.sh"]
