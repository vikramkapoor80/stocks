FROM python:3.8.8-slim

# Copy source code to working directory
COPY . /app/

# Working Directory
WORKDIR /app

# Install packages from requirements.txt
RUN pip install --no-cache-dir --upgrade pip &&\
    pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python" ]

# CMD [ "app.py" ]
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]