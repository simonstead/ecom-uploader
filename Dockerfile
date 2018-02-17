FROM python
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_APP=app.py
ENV FLASK_DEBUG=1
CMD gunicorn -w 5 -b 0.0.0.0:8000 app:app
