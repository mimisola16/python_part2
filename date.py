import datetime

# today = datetime.datetime.now()
# print(today.date())
# tdelta = datetime.timedelta(7)
# print(today + tdelta)

# strftime
# today = datetime.datetime(2024,2,14)
# print(today)

# this will bring out the year in full (2024)
# today = datetime.datetime.now()
# print(today.strftime("%Y"))

'''
#(Y, M, D, H, m, S, ms)
# %y, %m, %a, %H (24hrs)
# %Y, %M, %A,  %I (12hrs)
'''

# this will bring out the year in (24)
today = datetime.datetime.now()
# print(today.strftime("%y"))

# this will bring out the monthin (24)
today = datetime.datetime.now()
# print(today.strftime("%y"))

#  %I for 24hrs
today = datetime.datetime.now("%I")
print(today)