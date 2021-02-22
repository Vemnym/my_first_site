FROM python:3.9

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

#RUN python manage.py makemigrations
#RUN python manage.py migrate

RUN pip install gunicorn
RUN python manage.py collectstatic --noinput

EXPOSE 8001
# ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["gunicorn", "--bind", "0.0.0.0:8001", "mysite.wsgi", "--workers 4"]
