'''
A cinema has n rows of seats, numbered from 1 to n and there are ten seats in each row, labelled from 1 to 10 
as shown in the figure above.

Given the array reservedSeats containing the numbers of seats already 
reserved, for example, reservedSeats[i] = [3,8] means the seat located in row 3 and labelled with 8 is already reserved.

Return the maximum number of four-person groups you can assign on the cinema seats. A four-person group 
occupies four adjacent seats in one single row. Seats across an aisle (such as [3,3] and [3,4]) are not 
considered to be adjacent, but there is an exceptional case on which an aisle split a four-person group, in
that case, the aisle split a four-person group in the middle, which means to have two people on each side.
'''

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        s = {}
        for x in reservedSeats:
            if x[0] not in s.keys(): 
                 s[x[0]] = [0,0,0]
            if x[1] in [2,3,4,5]:
                s[x[0]][0] = 1
            if x[1] in [6,7,8,9]:
                s[x[0]][2] = 1
            if x[1] in [4,5,6,7]:
                s[x[0]][1] = 1
        
        ans = 0
        for k in s.keys():
            ans += 2 if s[k][0] == 0 and s[k][2] == 0 else 1 if s[k].count(0) > 0 else 0
        return ans + (n - len(s.keys())) * 2
      
---------------------------------------------------------

class Solution(object):
	def maxNumberOfFamilies(self, n, reservedSeats):
		"""
		:type n: int
		:type reservedSeats: List[List[int]]
		:rtype: int
		"""
		d = collections.defaultdict(list)

		# possible seats for family
		f1 = [2,3,4,5]
		f2 = [4,5,6,7]
		f3 = [6,7,8,9]
		res = 0

		# fill the dictionary, row as a key and reserved seats as a list
		for i in range(len(reservedSeats)):
			d[reservedSeats[i][0]].append(reservedSeats[i][1])

		# f as a flag to check how many families in a row
		for v in d.values():
			f = [1,1,1]
			for seat in v:
				# if reserved seat related to f1 or f2 or f3, set flag 0
				if seat in f1:
					f[0] = 0
				if seat in f2:
					f[1] = 0
				if seat in f3:
					f[2] = 0

			# it is not possible 2 more families in a row
			if f[0] == 1 or f[2] == 1:
				f[1] = 0            

			# cumulate the number of families in the current row
			res += sum(f)

		# calculate the number of row that not including reserved seats
		# we can skip these rows and just calculate numbers
		remain = (n - len(d)) * 2

		return res + remain
