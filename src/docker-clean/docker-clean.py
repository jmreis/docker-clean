#!/usr/bin/env python
import os


print(
	"""\033[1;94m
	⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠛⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
	⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣀⣀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
	⣿⣿⣿⣿⣿⣿⣿⠀⠀⢸⡇⠀⠀⡇⠀⠀⢸⣿⣿⣿⣿⣿⡟⠻⣿⣿⣿⣿⣿⣿
	⣿⣿⣿⡿⠿⠿⣿⠶⠶⢾⡷⠶⠶⡷⠶⠶⢾⠿⠿⠿⣿⣿⠀⠀⠈⣿⣿⣿⣿⣿
	⣿⣿⣿⡇⠀⠀⣿⠀⠀⢸⡇⠀⠀⡇⠀⠀⢸⠀⠀⠀⣿⣿⡀⠀⠀⠀⠀⠀⢉⣿
	⣿⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⢀⣀⣠⣴⣿⣿
	⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿
	⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿
	⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿
	⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
	⣿⣿⣿⣿⣿⣷⣶⣦⣤⣤⣤⣤⣤⣤⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿

		DOCKER-CLEAN
		by Jair Reis

	\033[0;0m""")

# Listing containers
os.system("docker ps -a -q")
# cleaning containers
print("\033[1;94mCleaning containers....................................\033[0;0m")
os.system("docker rm $(docker ps -a -q)")
#docker rm $(docker ps -a -q) -f(docker rm $(docker ps -a -q) -f)

# Listing images
os.system("docker images -g")
# Cleaning images
print("\033[1;94mCleanint images........................................\033[0;0m")
os.system("docker rmi $(docker images -q)")
#docker rmi $(docker images -q) -f(docker rmi $(docker images -q) -f)

# Cleaning volumes
print("\033[1;94mCleaning volumes.......................................\033[0;0m")
os.system("docker volume rm $(docker volume ls -q)")


# List os images
print("\033[1;94mList of docker images..................................\033[0;0m")
os.system("docker images")
