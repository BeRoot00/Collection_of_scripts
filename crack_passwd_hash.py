import crypt

def CrackPass(cryptPass):
    salt = cryptPass[0:2]
    wordList = open("wordlist.txt", 'r')
    for word in wordList:
        word = word.strip('\n')  # Remove trailing newline character
        cryptWord = crypt.crypt(word, salt)
        if cryptWord == cryptPass:
            print("Password Found:", word)
            wordList.close()  # Close the file after finding the password
            return 0
    wordList.close()  # Close the file if password not found
    print("Sorry, password not found")
    return 0

def main():
    with open('passwd.txt', 'r') as pwdFile:  # Use 'with' to automatically close the file
        for line in pwdFile.readlines():
            if ":" in line:
                user = line.split(':')[0]
                cryptPass = line.split(':')[1].strip()
                print("Trying to crack password for", user)
                CrackPass(cryptPass)

if __name__ == "__main__":
    main()
