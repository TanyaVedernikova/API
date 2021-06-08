FROM python:3.7-alpine
WORKDIR /test_suit_for_api/
EXPOSE 8080
COPY . /test_suit_for_api
RUN pip install -r requirements.txt --no-cache-dir
COPY . /test_suit_for_api/
ENV SERVICE_URL http://server:8000
ENTRYPOINT ["pytest", "test_for_api.py"]