with open('./0.json', 'rb') as r:
    pic = r.read()

for n in range(0, 333):  # Note that the 1 can be changed to a 2 because pic1.png is alrady there
    with open(f'{n}.json', 'wb') as w:
        w.write(pic)
