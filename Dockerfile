FROM python:3
EXPOSE 5000

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP greeter.py

CMD [ "flask", "run", "--host", "0.0.0.0" ]
