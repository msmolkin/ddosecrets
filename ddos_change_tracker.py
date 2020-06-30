import requests
r = requests.get('https://data.ddosecrets.com/file/')
with open('old.html', 'r') as old_file:
    old = old_file.readlines()
    for i in range(len(old)):
      old[i] = old[i].rstrip()

new = r.text.split('\r\n')

with open('old.html', 'w') as old_file:
  old_file.write(r.text)
  #print(r.text)

diff = [x for x in new if x not in old]
with open('changes.txt', 'a') as changes:
  changes.writelines(diff)
