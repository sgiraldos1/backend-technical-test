

    FROM python:3.9-slim
    
 
    WORKDIR /app
    

    COPY requirements.txt .
    
   
    RUN pip install --no-cache-dir -r requirements.txt
    
 
    COPY . .
    

    ENV APP_CONFIG_FILE=/app/app/config.py
    

    EXPOSE 8000
    

    CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app.app:app"]