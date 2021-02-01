
s = 'Now is the time for all good men to come to the aid of their country!'

w = str.split(s, ' ')
print(w[5] + " " + w[6] + " " + w[-1].strip('!') +  w[7])

s = w[5] + " " + w[6] + " " + w[-1].strip('!') +  w[7]
print(s)