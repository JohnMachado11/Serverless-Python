FROM python:3.9-slim

ENV APP_HOME /app  
WORKDIR $APP_HOME
COPY . ./

RUN pip install pip pipenv fastapi uvicorn requests --upgrade
RUN pipenv install --skip-lock --system --dev

CMD exec uvicorn main:app --host 0.0.0.0 --port $PORT