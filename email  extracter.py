import re
file = open("input.txt", "r")
text = file.read()
file.close()
pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
emails = re.findall(pattern, text)
unique_emails = list(set(emails))
output = open("emails_extracted.txt", "w")
for email in unique_emails:
    output.write(email + "\n")
output.close()
print(f"Extracted {len(unique_emails)} unique emails to 'emails_extracted.txt'.")
