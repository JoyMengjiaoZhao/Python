import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
cat
mat
pat
bat
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov

'''
sentence='Start a sentence and then bring it to an end'

print('\tTab')
print(r'\tTab')  #raw string

#search things for '.',we need to use'\.'
#pattern=re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d') #dash or dot (only match one character)
#pattern=re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
#pattern=re.compile(r'[1-5]') #range
#pattern=re.compile(r'[^a-zA-Z]') # '^'carrot means except"a-zA-Z"
#pattern=re.compile(r'[^b]at')
#pattern=re.compile(r'\d{3}.\d{3}.\d{4}')
#pattern=re.compile(r'M(r|s|rs)\.?\s[A-Z]\w+') #'?' question mwans '1' or '0'
#pattern=re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)') #email address
pattern=re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
#"|" means groups 'or'
subbed_urls=pattern.sub(r'\2\3',text_to_search) #'\2and \3'number of group

print(subbed_urls)
matches=pattern.finditer(text_to_search)
#findall return the matches as a list of strings
#match/search/we can add flag
for match in matches:
    print(match.group(2)) #(0)entire url/()means group

#with open('data.txt','r') as f:
#    contents=f.read()
#    matches=pattern.finditer(contents)

#    for match in matches:
#        print(match)


