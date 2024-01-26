import cgi

def save_subscription(email):
    with open('subscribers.txt', 'a') as file:
        file.write(email + '\n')

def main():
    print("Content-type: text/html\n")  
    form = cgi.FieldStorage()
    
    if "email" in form:
        email = form["email"].value
        
        
        if '@' in email:
            save_subscription(email)
            print("<p>Subscription successful!</p>")
        else:
            print("<p>Invalid email address!</p>")
    else:
        print("<p>Error: Email not provided!</p>")

if __name__ == "__main__":
    main()
