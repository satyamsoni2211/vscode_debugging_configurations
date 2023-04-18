FROM python:3.11

WORKDIR /app

COPY requirements.txt ./

RUN useradd -m -d /home/python_user python_user

USER python_user

RUN pip install -U --no-cache-dir -r requirements.txt

COPY demo.py .

CMD [ "python", "./fastapi_demo.py" ]