import re

# Function to clean the LinkedIn profile links using regex
def clean_link(link):
    match = re.match(r'(https://www\.linkedin\.com/in/[a-zA-Z0-9-]+)', link)
    return match.group(0) if match else link

link= clean_link('https://www.linkedin.com/in/nakul-36gupta?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAAC8lwkkB829JLZVENRa5UupdkYeipqoDxsY')

print(link)