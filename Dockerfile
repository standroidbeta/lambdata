FROM debian

# Comments are like this
ENV PYTHONUNBUFFERED=1
# so logging works w/Docker

# You can RUN things, mostly to install dependencies
RUN apt-get update && apt-get upgrade -y && \
  apt-get install python3-pip python-pandas -y && \
  pip3 install -i https://test.pypi.org/simple/ lambdata-standroidbeta && \
  python3 -c "import lambdata_standroidbeta"
