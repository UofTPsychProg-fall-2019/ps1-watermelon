#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem Set 1
@author: katherineduncan
"""

#%% Part 1: pass the error forward ____________________________________________
# this should be completed one at a time to get practice using GitHub


# there's an error in the definition of x below
# first group member (coder 1), your job is to first correct it 
# and make a new variable with an error for the next group member to fix
# after competign both steps, commit and push your changes to GitHub
evi = 'hello world! python line’ + ‘ 1’ 
print(evi)

# second group member's error to fix
yachen = ‘hello world!' * int(2.5)
print(yachen)

# now the second group member should define a variable with an error
# and then commit and push changes to GitHub
jason = 'a' + 'b' + 'c'
print(jason)

# Rachel fixing Jason's error
rachel = ["j", "a", "s", "o", "n"]
print(rachel)

# Joe fixing Rachel's error 
Joe = ['psychology', 1, 4]
print(Joe)

#%%  Part 2  find and remove the invalid response______________________________

# imagine these are a list of reaction times that you recorded 
rt = [400, 450, 500, 440, -1, 410, 570]

# the -1 indicates missing data. Your job is to remove it
# use the index method to find the missing value 
missing_rt = rt[-3]

# and then use missing_rt to remove the trial from rt
clean_rt = rt.remove(missing_rt)


# now you have data with more than one missing value
rt_trouble = [400, 450, 500, 440, -1, 410, 570, -1, 400]

# try the same procedure. Does it work? 
missing_rt = rt_trouble[4:8:3]
clean_rt = rt_trouble.remove(missing_rt)
print(clean_rt)

# use a comment to explain why or why not below in comments
# it doesn't work, because missing_rt now forms a list [-1,-1], which is not an item in rt_trouble. 
## if you use the first method ->
### clean_rt = rt_trouble.remove[missing_rt] it only removes the first missing item, not all of the missing items. 
#### Python sees it as only removing one value at a time


# now write an if statement that you can use to remove the frist missing value 
# only when there is a missing value (-1) in a list 
# this statement should always generate a clean_rt list; if there's no missing
# data clean_rt is set to the original rt list.  
	
if -1 in rt_trouble:
	clean_rt_trouble = rt_trouble.remove(-1)
	print(rt_trouble)
else:
    print(rt_trouble)

# for the last section, you will work with a list of lists:
# this master list combines information about each trial in an experiment,
# where index 0 in each sublist refers to data from the first trial, etc.
# using the same appraoches as above, find the trial with missing rt data
# and remove it from all sublists in data 
# be sure to only work with the master data list, to practice indexing 
# lists of lists
rt_new = [400, 450, 500, 440, -1, 410, 570]
trial_num = [1,2,3,4,5,6,7]
accuracy = [0, 1, 0, 0, 1, 0]
data = [rt_new, trial_num, accuracy]

missing = data[0].index(-1)
del(data[0][missing])
del(data[1][missing])
print(data)  

# Other methods:
data = [rt_new.remove(-1),trial_num.remove(5)]
data = [rt_new, trial_num, accuracy]
print(data)

missing = data[0].index(-1)
for x in data:
    if x != data[-1]:
        del(x[missing])
print(data)

remove = data[0].index(-1)
for i in [0,1]:
    del(data[i][remove])
print(data)

