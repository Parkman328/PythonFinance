FROM python:3
COPY . /
WORKDIR /app
RUN apt-get update
RUN pip install -r requirements.txt 
EXPOSE 5001 
ENTRYPOINT [ "python" ] 
CMD [ "app.py" ] 