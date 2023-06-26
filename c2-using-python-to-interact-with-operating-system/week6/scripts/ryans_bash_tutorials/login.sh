#!/bin/bash

read -p 'Username: ' uservar
read -sp 'Password: ' passvar

echo
echo Thank you $uservar we now have your creds
echo Given command line argument: $1
echo Current path: $PWD
