FROM python:3.7

WORKDIR /app

COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5755

ENTRYPOINT ["python"]
CMD ["1.py"]
