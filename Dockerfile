FROM python:3.7.16-slim 
RUN pip install flask
COPY Online/MainScores.py /app/
COPY Utils/Utils.py /app/Utils/
COPY Scores/ /app/Scores
WORKDIR /app/
EXPOSE 4000
CMD ["python3", "MainScores.py"]
