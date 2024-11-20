import hashlib
import csv

DATA_FILE = "dummy.csv"

search_string = input("Please enter an email address or password: ")
is_email = False

if "@" in search_string:
    is_email = True
with open(DATA_FILE, "r", newline='') as dummy_data_file:
    reader = csv.reader(dummy_data_file)
    for row in reader:
        if is_email:
            if row[0] == search_string: # this check
                print("Your email has been compromised")
                exit()
        else:
            if row[1] == hashlib.sha1(search_string.encode('utf-8')).hexdigest():
                print("Your password has been compromised")
                print("The email associated with this password is: " + row[0])
                exit()

print("Your information has not been compromised!")