# Script Basic for personal secure locker
#defining the Interpreter
#!/bin/bash

username=""
companyname=""
pin=""
#Defining the Loop
for i in {1..3}; do
	if [ "$i" -eq 1 ]; then
		echo "Enter your Username:"
		read username
	elif [ "$i" -eq 2 ] ; then
		echo "Enter your company name:"
		read companyname

	else 
		echo "Enter your PIN:"
		read pin
	fi
done
#checking if the user entered the correct details: 
if [ "$username" = "John" ] && [ "$companyname" = "Tryhackme" ] && [ "$pin" = "7385" ]; then 
	echo "Authentication Successful. Welcome to your locker, John."
else
	echo "Authentication Denied!!"
fi
