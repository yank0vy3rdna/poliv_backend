FROM python:3.8
WORKDIR /app
ADD requirements.txt .
RUN python3 -m pip install -r requirements.txt
ADD app/ ./app
ADD static/ ./static
CMD ["uvicorn", "--host", "0.0.0.0", "app:app"]