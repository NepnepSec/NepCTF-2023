FROM python:3.8

COPY ./files/* /app/
RUN mkdir -p /app/attachment/
WORKDIR /app/attachment/

CMD ["python", "/app/trs.py"]

# EXPOSE 8081
