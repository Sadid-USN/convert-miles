print("Enter a mile ")
mile1 = (int(input()))
kilometer1 = 1.609
length1 = mile1

def convert_mails(kilometr, length):
    count = kilometr*length
    if count >=1.6:
        return "  miles equal "  + str(count) + " kilometers "

mile = convert_mails(kilometer1,length1)
print(mile)
