FROM python:3.9.0

WORKDIR /home/

RUN echo "testing"

RUN git clone https://github.com/ddubi6796/hjsm.git

WORKDIR /home/hjsm/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=hjsm.settings.deploy && python manage.py migrate --settings=hjsm.settings.deploy && gunicorn hjsm.wsgi --env DJANGO_SETTINGS_MODULE=hjsm.settings.deploy --bind 0.0.0.0:8000"]