# get user email address
email = input("what is ur email address?: ").strip()


# slice out user name

user = email[:email.index("@")]

# slice domain name
domain = email[email.index("@")+1:]

# format message

output = "ur username is  {} , ur domain name is {}".format(user,domain)
# display output message
print(output)
