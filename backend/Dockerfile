FROM python:3

WORKDIR /backend

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD [ "python", "app.py" ]