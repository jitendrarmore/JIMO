import re
import csv

with open('ip.csv') as csvfile:
  readCSV = csv.reader(csvfile, delimiter=',')
  iplist = []
  for row in readCSV:
    iplist.append(row[0])

print(iplist)
#

def get_valid_ip_list(address):
  list = []
  #score = float(raw_input())
  list.append(address)
  s = list
  ipv4_address = re.compile('^(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$')
  for i in list:
    print("IP is Valid" if ipv4_address.match(i) else "IP is not Valiad" )

for address in iplist:
  get_valid_ip_list(address)

if __name__ == '__main__':
  address = []
  for i in range(int(raw_input())):
    address.append(raw_input())
  for j in address:
    checkIP(j)
