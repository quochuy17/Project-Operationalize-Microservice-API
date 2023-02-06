FROM python:3.7.3-stretch

## Initially , just make the working directory
WORKDIR /app

## Next, create some similar source code to the directory of work
COPY . app.py /app/

## Third, just install packages from the file "requirements.txt" with the hadolint "ignore=DL3013"
# hadolint ignore=DL3013
RUN pip install --upgrade pip && \
    pip install --trusted-host pypi.python.org -r requirements.txt

## Fourthly, just show the port 80
EXPOSE 80

## Fifthly, implement the file "app.py" at the launch of container
CMD ["python", "app.py"]
