#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This python CLI application was inspired by an article about how
remove images, containers and volumes. 
All in order to help clean up development environments,
after the great ease of creating docker environments.

The script performs a cleanup on the development machine.

Reference article: http://www.macoratti.net/19/02/dock_limp1.htm
"""
import os
import sys
import logging
import argparse


# Setting terminal colors and ascii art header
RED = "\033[31;1m"
GREEN = "\033[32;1m"
CIANO = "\033[36;1m"
BLUE = "\033[1;94m"
RESET = "\033[0;0m"
HEADER = f"""{BLUE}
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
	==============================
	{RESET}"""

# List of commands
INFO = "docker info"
CLEAR_IMAGES = "docker rmi $(docker images -q)"
CLEAR_CONTAINERS = "docker rm $(docker ps -a -q)"
CLEAR_VOLUMES = "docker volume rm $(docker volume ls -q)"
CLEAR_NETWORKS = "docker network rm $(docker network ls -q)"

# Setting the logging configurations
logging.basicConfig(format='%(message)s - docker-clean - %(asctime)s',
        level=logging.DEBUG)


def show_header():
	"""Show the script intro."""
	os.system("clear")
	print(HEADER)


def show_docker_infos():
	"""Show all info about docker"""
	logging.debug(f"📝 {BLUE}Show docker info{RESET}")
	os.system("docker info")


def clear_container():
	"""This function clear all containers"""
	# cleaning containers
	logging.debug(f"🗑 {BLUE}Cleaning containers{RESET}")
	os.system(CLEAR_CONTAINERS)
	#docker rm $(docker ps -a -q) -f(docker rm $(docker ps -a -q) -f)


def clear_images():
	"""This function clear all images"""
	logging.debug(f"🗑 {BLUE}Cleaning images{RESET}")
	os.system(CLEAR_IMAGES)
	#docker rmi $(docker images -q) -f(docker rmi $(docker images -q) -f)


def clear_volumes():
	"""This function clear all volumes"""
	# Cleaning volumes
	logging.debug(f"🗑 {BLUE}Cleaning volumes{RESET}")
	os.system(CLEAR_VOLUMES)


def clear_networks():
	"""This function clear all networks"""
	# Cleaning volumes
	logging.debug(f"🗑 {BLUE}Cleaning networks{RESET}")
	os.system(CLEAR_NETWORKS)


def clear_all():
	"""Clear all containers, volumes, images and networks"""
	logging.debug(f"🗑 {BLUE}Cleaning all{RESET}")
	clear_container()
	clear_images()
	clear_volumes()
	clear_networks()


def main():
	# Setting command line
	parser = argparse.ArgumentParser(
     prog='DOCKER-CLEAN',
     description= "Cleaning docker enviroment",
     epilog='''This cli app, help clean all images,
	 	containers, volumes and networks 
	 	in docker development environment.''')
	parser.add_argument('--info', help="Show dockers infos", action='store_true')
	parser.add_argument('--images', '-i', help="Cleaning all docker images",
	    action='store_true')
	parser.add_argument('--containers', '-c', help="Cleaning all docker containers",
	    action='store_true')
	parser.add_argument('--volumes', '-v', help="Cleaning all docker volumens",
	    action='store_true')
	parser.add_argument('--networks', '-n', help="Cleaning all networks",
	    action='store_true')
	parser.add_argument('--all', '-a', help="Cleaning all docker enviroment",
	    action='store_true')
	args = parser.parse_args()

	if args.info:
		show_docker_infos()
	elif args.images:
		clear_images()
	elif args.containers:
		clear_container()
	elif args.volumes:
		clear_volumes()
	elif args.networks:
		clear_networks()
	elif args.all:
		clear_all()


if __name__ == "__main__":
	# Call the header function
	show_header()
	sys.exit(main())
	
	
