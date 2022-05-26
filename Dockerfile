FROM ros:galactic

# # install ros package
RUN sed -i 's#http://archive.ubuntu.com/#http://mirrors.tuna.tsinghua.edu.cn/#' /etc/apt/sources.list
RUN apt-get update && apt-get install -y libgl1-mesa-glx
RUN apt-get -y install pip

# Any working directory can be chosen as per choice like '/' or '/home' etc
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

#to COPY the remote file at working directory in container
COPY . .
# Now the structure looks like this '/usr/app/src/test.py'
#CMD instruction should be used to run the software
#contained by your image, along with any arguments.
CMD [ "python3", "./app/talker.py"]
