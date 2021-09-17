#!/usr/bin/env python
import sys


# Listing containers
os.system("docker ps -a -q")
# cleaning containers
print("Cleaning containers....................................")
os.system("docker rm $(docker ps -a -q)")
#docker rm $(docker ps -a -q) -f(docker rm $(docker ps -a -q) -f)

# Listing images
os.system("docker images -g")
# Cleaning images
print("Cleanint images........................................")
os.system("docker rmi $(docker images -q)")
#docker rmi $(docker images -q) -f(docker rmi $(docker images -q) -f)

# List os images
print("List of docker images..................................")
os.system("docker images")
