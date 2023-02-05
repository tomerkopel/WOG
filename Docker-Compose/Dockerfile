FROM python:3.7.16-slim 
RUN pip install flask
COPY MainScores.py /app/
COPY Utils.py /app/Utils/
COPY Scores.txt /app/Scores/
WORKDIR /app/
EXPOSE 4000
CMD ["python3", "MainScores.py"]
