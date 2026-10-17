"""
p15
The following problem is from Chapter 6. Try it again, this time using a dictionary whose
keys are the names of the time zones and whose values are offsets from the Eastern time
zone.
Write a program that converts a time from one time zone to another. The user enters the time
in the usual American way, such as 3:48pm or 11:26am . The first time zone the user enters
is that of the original time and the second is the desired time zone. The possible time zones
are Eastern , Central , Mountain , or Pacific .
Time: 11:48pm
Starting zone: Pacific
Ending zone: Eastern
2:48am
"""
# if the current time not central convert it .
# create a dict which its keys is times zone and values are float numbers.
#d[zone that user want] + current time.
time, zone = input("Time: ").split()
curr_zone = input("Starting zone: ")
end_zone = input("Ending zone: ")
standard = 0

d = {'Eastern': -1, 'Central': 0, 'Mountain': 1, 'Pacific': 2}
if curr_zone != 'Central':
    standard = d[curr_zone] + int(time[:2])
new_time = standard - d[end_zone]
if new_time > 12 :
    new_time -= 12
    if zone == 'pm':
        zone = 'am'
    else:
        zone = 'pm'
print(new_time, time[2:], zone, sep='')



##########################################