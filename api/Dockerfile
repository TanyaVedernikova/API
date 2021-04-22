FROM python:3.7-alpine
WORKDIR /api
COPY requirements.txt /api
RUN pip install -r requirements.txt --no-cache-dir
ADD main.py /api
ENTRYPOINT [ "python" ]
CMD ["main.py"]