# Use the official Ubuntu 22.04 image as base
FROM ubuntu:22.04

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script and CSV files into the container
COPY challenge.py .
COPY media_source.csv .
COPY mmp.csv .

# Install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Install pandas
RUN pip3 install pandas

# Run the Python script when the container launches
CMD ["python3", "challenge.py"]