import requests,re,csv

#insert a website that you want to scrape emails from, here is an example:
#f = requests.get("https://pastebin.com/wFcDSDns")

f = requests.get("http://")
s = f.text

#Using regular expressions to identify all the email formats in the page 
eemail = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",s)

for em in eemail:
    print(em)

#You know, to separate stuff...
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Done!")
ans = input("Press any key to export to a CSV file.")

#Specify where do you want to export CSV
filen = "C:\\Users\\User\\Desktop\\emails.csv"
f = open(filen,"a")
head = "E-mails\n"
f.write(head)

for emls in eemail:
    f.write(emls+"\n")

print("Exported to : "+filen)