"""replace all special symbol with # in the following string
str1='/*jon is @developer & musician!!' """

str1='/*jon is @developer & musician!!'
print("original string:",str1)
# str1=str1.replace('/','#').replace('*',"#").replace('@',"#").replace('&,"#').replace('!','#')
# print("new string:",str1)
str2=str1.replace("/","#").replace("*","#").replace("@","#").replace("&","#").replace("!","#")
print(str2)
