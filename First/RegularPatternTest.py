import re

# testString = '55ddd d\n'
# patternstring = '(\d*)(d*)'

#Function1 : Match
# pattern = re.compile(patternstring)
# match = pattern.match(testString)
# for i in match.groups():
#     print i

#Function2: Search
# testString = 'd55dd555 d\n'
# patternstring = '\d+'
# pattern = re.compile(patternstring)
# res = pattern.search(testString)
# print res.group()

#Founction3:Findall
# testString = 'd55ddD555 d\n'
# patternstring = '\d+\D+'
#
# pattern = re.compile(patternstring,re.IGNORECASE)
# findstring = pattern.findall(testString)
# print findstring

#Function4: sub
testString = '55ddD555 d\n'
patternstring = '\s?[a-z]*[A-Z]*\s?'
pattern = re.compile(patternstring)
spl = pattern.split(testString)
sub = pattern.sub('r',testString)
print  pattern.pattern
