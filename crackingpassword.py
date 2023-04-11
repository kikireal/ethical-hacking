# Import Required Module
import pikepdf
from tqdm import tqdm
  
# Empty password list
passwords = []
  
# Contain passwords in text file
password_text_file = "words.txt"
  
# Iterate through each line
# and store in passwords list
for line in open(password_text_file):
    passwords.append(line.strip())
# iterate over passwords
for password in tqdm(passwords, "Noob_player.pdf"):
    try:
        
        # open PDF file and check each password
        with pikepdf.open("Noob_player.pdf",
                          password = password) as p:
            
            # If password is correct, break the loop
            print("[+] Password found:", password)
            break
              
    # If password will not match, it will raise PasswordError
    except pikepdf.PasswordError as e:
        
        # if password is wrong, continue the loop
       continue