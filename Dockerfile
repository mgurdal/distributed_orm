FROM python:3
RUN pip3 install dispy
RUN pip3 install psutil
ADD distributer/dispynode.py /
CMD python dispynode.py
EXPOSE 51348
