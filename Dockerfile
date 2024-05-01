FROM python:3.11.9
ENV  PYTHONUNBUFFERED 1
WORKDIR /ObesityCheck_Streamlit
COPY requirements.txt /ObesityCheck_Streamlit
RUN pip install --no-cache-dir -r requirements.txt
COPY . /ObesityCheck_Streamlit
EXPOSE 8501