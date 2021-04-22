FROM python:3.7-alpine
WORKDIR /test_suit_for_api
COPY requirements.txt /test_suit_for_api
RUN pip install -r requirements.txt --no-cache-dir
ADD test_for_api.py /test_suit_for_api
ENTRYPOINT [ "pytest" ]
CMD ["test_for_api.py"]