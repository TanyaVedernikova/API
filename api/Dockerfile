FROM python:3.7
WORKDIR /api
ADD main.py /api/
COPY . /api
RUN pip install -r requirements.txt --no-cache-dir
ENTRYPOINT [ "python", "main.py" ]

