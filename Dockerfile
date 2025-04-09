FROM python:3.11
ENV PYTHONUNBUFFERED=1
WORKDIR /app
RUN apt-get update && apt-get install -y sqlite3 libsqlite3-dev
RUN pip install django
RUN pip install requests
RUN touch /app/src/db.sqlite3
COPY . /app/
EXPOSE 8000
CMD [ "script.bash" ]