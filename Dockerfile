FROM python:3.12.0
ADD requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]