FROM python:3.8-alpine

WORKDIR /code

ENV FLASK_APP=app.py

RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 3000

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0",  "--port=3000"]
