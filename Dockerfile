FROM python:alpine


# Set the working directory in the container
WORKDIR /app

# Copy only the necessary files into the container
COPY paragraphs.txt /app
COPY code.py /app

# Install any dependencies
RUN pip install nltk
RUN python -m nltk.downloader stopwords
RUN python -m nltk.downloader punkt

# Run the Python script
CMD ["python", "code.py"]

