# write your code here
# read data from console

# output the answer to the console according to the requirements of the question
'''

Find the sum of the main
diagonal elements of a n*nn∗n integer matrix nums. Please use the print 
statement to output the sum of the main diagonal elements of the matrix nums.
'''

n = int(input())

nums = []
if n == 1:
  print(int(input()))
else:
  for i in range(n):
    nums_inline = input()
    nums_inline = nums_inline.split(" ")
    nums.append(nums_inline)

  res = 0
  for i in range(len(nums)):
	  res += int(nums[i][i])
  print(res)
