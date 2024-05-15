"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""
# Daniel Mann
#Heartbeat exercise range finder
age = input("what is your age?")
numAge = int(age)
maxBeat = (220-numAge)
maxRange = int(maxBeat*.85)
minRange =int(maxBeat*.65)
print(f"When you exercise to strengthen your heart, you should keep your heart rate between {minRange} and {maxRange} beats per minute.")