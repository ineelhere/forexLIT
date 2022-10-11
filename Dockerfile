FROM python:3.8.14
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8501
ENTRYPOINT ["streamlit", "run"]
CMD ["1_💰_ForexLIT.py"]