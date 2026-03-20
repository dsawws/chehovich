text="елка , ваывфвыа , ывафыафв, ееее"
a='е'
b=0
text_a=text.split()

for text in text_a:
    if text.startswith(a):
        b+=1
 
print (b)