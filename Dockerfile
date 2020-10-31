FROM quantopian/zipline:latest

# Fix No module named 'numpy.testing.nosetester'
#  see https://bit.ly/2GdLzrc
RUN pip install -U scipy
RUN pip install pyfolio