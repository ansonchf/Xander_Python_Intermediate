import re

def match(pattern,text):
    match = re.search(pattern,text)
    if match:
        print("Match found!", match.group())
    else:
        print("Match not found.")
    
# 1. MMDDYYYY
pattern = r"\d{2}/\d{2}/\d{4}"
text = "The date is 04/05/2020"

match(pattern,text)

# 2. username@domain.com
pattern = r"[\w\.-]+@[\w\.]+.[\w]"
text = "username@domain.com"

match(pattern,text)

# 3. http(s)www.domain.compathtopage.html
pattern = r"https?://(w{3}\.)?\S+\.com/\S+\.(html|php|ahp)"
text = "https://domain.com/path/to/page.html"

match(pattern,text)

# ​4. (XXX) XXX-XXXX
pattern = r"\(\d{3}\) \d{3}-\d{4}"
text = "(123) 324-1525"

match(pattern,text)

# 5. A string that contains at least one uppercase letter, one lowercase letter, and one digit, and is between 8 and 20 characters long
pattern = r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,20}"
text = "a12dawdAdawGV"

match(pattern,text)

# 6. A string that contains only letters, numbers, and spaces, and is between 5 and 50 characters long.
pattern = r"[A-Za-z0-9 ]{5,50}"
text = "11--231kj-325"

match(pattern,text)

# 7. A string that contains at least one uppercase letter, one lowercase letter, one digit, and one special character, and is between 8 and 20 characters long.
pattern = r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\ws]).{8,20}"
text = "a12daw21----dAdawGV"

match(pattern,text)

# 8. XXXX-XXXX-XXXX-XXXX
pattern = r"\d{4}-\d{4}-\d{4}-\d{4}"
text = "8521-4563-9512-7532"

match(pattern,text)
