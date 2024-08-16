#!/usr/bin/env bash
#this file is for task 3.Let me in, this file will show you all the steps to add an SSH pub key to your server.

#first connect your server by using this command line:
ssh ubuntu@100.26.213.98
#replace 100.26.213.98 by your IP

#then avigate to the .ssh directory:
cd ~/.ssh
#if this dir dosn't exist add those 2 comand:
#---> mkdir -p ~/.ssh
#---> chmod 700 ~/.ssh

#then add the ssh key 
echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNdtrNGtTXe5Tp1EJQop8mOSAuRGLjJ6DW4PqX4wId/Kawz35ESampIqHSOTJmbQ8UlxdJuk0gAXKk3Ncle4safGYqM/VeDK3LN5iAJxf4kcaxNtS3eVxWBE5iF3FbIjOqwxw5Lf5sRa5yXxA8HfWidhbIG5TqKL922hPgsCGABIrXRlfZYeC0FEuPWdr6smOElSVvIXthRWp9cr685KdCI+COxlj1RdVsvIo+zunmLACF9PYdjB2s96Fn0ocD3c5SGLvDOFCyvDojSAOyE70ebIElnskKsDTGwfT4P6jh9OBzTyQEIS2jOaE5RQq4IB4DsMhvbjDSQrP0MdCLgwkN" >> ~/.ssh/authorized_keys

#at the end do this:
chmod 600 ~/.ssh/authorized_keys
#and make sure it works by:
cat ~/.ssh/authorized_keys
