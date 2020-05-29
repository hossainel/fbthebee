
#url = "https://www.facebook.com/profile.php?id=100007222056089"

try:    
    with open("uid.txt", 'r') as fob:
        uids = fob.readlines()
        uids = [int(i) for i in uids]
        fob.close()
except:
    uids = []
    with open("uid.txt", 'w') as fob:
        fob.close()
    
T=True
while T:
    tx = input("Enter UID (or q to quit): ")
    if tx=='Q' or tx=='q':
        T = False
        break
    if len(tx)==15:
##        url = "https://www.fb.com/%s"%tx
##        print(url)
##        page = requests.get(url)
##        name = page.content.split(b'<title id="pageTitle">')[1].split(b'</title>')[0]
##        with open('a.txt', 'wb') as foc:
##            foc.write(name)
##            foc.close()
        print('ID Accepted.')
        uids.append(int(tx))
        uids = set(uids)
        uids = sorted(uids)
        uids = list(uids)
        fob = open('uid.txt', 'w')
        for i in uids: fob.write(str(i)+"\n")
        fob.close()
    else:
        print("Invalid UID.")
