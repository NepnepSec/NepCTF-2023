FROM python:3.8

RUN pip install numpy wave -i https://mirrors.ustc.edu.cn/pypi/web/simple
COPY ./files/* /app/
RUN mkdir -p /app/attachment/
WORKDIR /app/attachment/

CMD ["python", "/app/lic.py"]

# EXPOSE 8081
