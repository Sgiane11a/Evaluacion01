FROM python:3.11
ENV PYTHONUNBUFFERED=1
WORKDIR /app
RUN 
RUN pip install django
RUN pip install requests
COPY . /app/
EXPOSE 8000
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]