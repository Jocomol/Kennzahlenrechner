#!/bin/bash
folder="/home/Jocomol/kennzahlen_files"
# Renew folder structure
rm -r $folder
mkdir $folder

#Make helpscripts executable
chmod +X ./*
cp * $folder

#copy the kennzahlenrechner
cd ..
cp bilanz.yml $folder
cp kennzahlenrechner.py $folder
cp std_kennzahlen.yml $folder
cp kennzahlenrechner_shell.py $folder/..

#dowload requirements
pip3 install -r requirements.txt

echo "the git folder can now be removed"
