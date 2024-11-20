import hashlib
import csv

password_file=open("honeynet.txt","r")
password_list=[]
for line in password_file:
    password_list.append(hashlib.sha1(line.strip().encode('utf-8')).hexdigest())

names_file=open("names.txt","r")
with open("dummy.csv" , "w", newline="") as file:
    writer = csv.writer(file)
    counter=0
    for line in names_file:
        email=line.strip() + "@gmail.com"
        writer.writerow([email, password_list[counter]])
        counter+=1
