FROM python:3.9-slim-buster
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app
# EXPOSE 5001
ENV FLASK_APP=app.py
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
# CMD ["flask", "run", "--host", "0.0.0.0"]