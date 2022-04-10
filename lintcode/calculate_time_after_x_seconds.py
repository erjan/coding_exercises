#my annoying solution

'''

Your code needs to read the 
current time from the standard input stream (console). The input 
format is such as hh:mm:ss, which represents hour, minute, and second respectively, and 
then a positive integer x is given to find the elapsed time. The time after x seconds is 
expressed, and the result is calculated and printed to the standard output stream (console).

'''


s = input()
x = int(input())

s = s.strip('\r')
s = s.split(':')
s = list(map(int, s))


totalsec =   s[0]*60*60 + s[1] * 60 + s[2]

#print('before, just the original time in sec', totalsec)
totalsec +=x
#print('after , with x time', totalsec)
#back to h:m:s

h, rest = divmod(totalsec,3600)

if h > 23:
	h = h%24
#print(h,rest)
m, rest = divmod(rest, 60)
#print(m,rest)

sec = rest
# print('seconds')
# print(sec)

if len(str(h)) < 2:
	h = '0'+str(h)

if len(str(m)) <2:
	m = '0' + str(m)

if len(str(sec))<2:

	sec = '0' + str(sec)
res = str(h) + ':' + str(m)+':' + str(sec)
print(res)


-------------------------------------------------

time = input()
x = int(input())
h = int(time.split(":")[0])
m = int(time.split(":")[1])
s = int(time.split(":")[2])
ss = ((h*3600+m*60+s+x) % 3600) % 60                    # 秒，60进制。总秒数对小时取余剩分，再对分取余剩秒。因为取余了，所以秒位不会溢出
mm = int(((h*3600+m*60+s+x-ss) % 3600) / 60)            # 分，60进制。先去除秒位上的秒数，剩下的秒数对小时取余，剩下的都是分位上的整秒数，再除就是分。因为取余了，所以分位不会溢出
hh = int(((h*3600+m*60+s+x-ss-mm*60) / 3600) % 24)      # 时，24进制。先去除秒位和分位上的秒数，剩下的都是时位上的整秒数，再除就是时，用它的进制取余就是时。因为是第一个位数，所以会溢出，要取余

print("{:0>2d}:{:0>2d}:{:0>2d}".format(hh, mm, ss))
---------------------------------------


s = input().replace('\r', '').split(':')
x = int(input())
a = []
for i in s:
    a.append(int(i))
b = a[0]*60*60+a[1]*60+a[2]+x
e=b//3600
if e > 24:
    e = e%24
c = b%3600//60
d = b%3600%60

print("%02d:%02d:%02d"%(e,c,d))
