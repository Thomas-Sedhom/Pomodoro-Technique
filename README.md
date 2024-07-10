# Pomodoro Technique 

 This project implements a web application based on the Pomodoro Technique. Users can create tasks, initiate a timer, and upon completion, the task is marked as finished. The application also provides functionalities for stopping and resetting the timer.
 ###

# Getting started
 ## - Setup flask framework

  ### Step 1: Install Virtual Environment
  Use apt to install virtualenv on Debian, Ubuntu and other related distributions

  ```bash
   sudo apt install python-virtualenv
  ```

  ### Step 2: Create an Environment
  Make a separate directory for your project:
  ```bash
   mkdir <project name>
  ```
  Move into the directory:
  ```bash
   cd <project name>
  ```
  To create a virtual environment for Python 3, use the venv module and give it a name:
  ```bash
   python3 -m venv <name of environment>
  ```
  ### Step 3: Activate the Environment
  ```bash
   . <name of environment>/bin/activate
  ```
  ###

 ## Running the application
  ```
   python main.py
  ```
   ###
# Tests
 this project using [Unittest](https://docs.python.org/3/library/unittest.html) framework to testing endpoints
 ### Running tests
  ```
   python -m unittest main.py
  ```
# Virtualize application with docker
## First install Docker in your local machine 
### Uninstall all conflicting packages
```
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done
```
### Setup Docker's apt repository
```
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```
### Install the Docker packages
```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
### Verify the Docker Engine installation is successful by running "hello-world" image
```
sudo docker run heelo world
```
###
# Create Docker File
```
# Use a minimal Python image as you can for efficiency
FROM python:alpine

# Set the working directory within the container
WORKDIR /app

# Install project dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy your project code
COPY . .

# Expose the port your application listens on
EXPOSE 5000

# Command to run your application
CMD ["python", "main.py"]
```
# create group and user to access to build and run Docker file
```
# create "docker" group
sudo groupadd docker
# adds your current user to the newly created #"docker" group
sudo usermod -aG docker $USER
```
###
# Build docker file
### "create an image from Docker file"
```
docker build --tag "image-name"
```
# run docker file
```
# the docker run command is what actually #brings that image to life. It takes the image #and starts a container instance based on its #instructions. This allows you to run the #application defined in the image.

docker run "image-name"
```
# create .dockerignore file 
```
touch .dockerignore file
```

# Share the application
```
# get docker image id 
docker images

#crate a tag name as same as dockerHubUserName/repoName
docker login -u userName
docker tag imgID docker/getting-started
docker push docker/getting-started
```