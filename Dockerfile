FROM quantopian/zipline:trading_evolved

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt