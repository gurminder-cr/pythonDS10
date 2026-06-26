# Regular expression - 
# Any 10 digits - \d{10}
import re 
exp="[6-9]{1}\d{9}"

str1= "hello 1 2 3 4 and my mobile number is 8264123555 and other number is 8264535123 and 723842 and 82987 and 1234568920 and mail id gurminder@coderroots.com and other is coderroots001@gmail.com and gurgmail.com and Ert12.hi@knm.tech "

print(re.findall(exp,str1))  # pattern ,string

print(re.sub(exp,repl='_', string=str1))


email_exp="[a-zA-Z0-9._]+@[a-zA-Z0-9]+.[a-zA-Z]{2,6}"

print(re.findall(email_exp,str1))

# user_input= input("Enter your email ")
# print(re.match(email_exp,user_input))