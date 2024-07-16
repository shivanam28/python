from string import Template
name = input("Enter details to be fill in letter template:\nName: ")
date = input("Date: ")

letter = Template("Dear $name, \nYou are selected! \n $date")
print(letter.safe_substitute(name = name , date = date))