#== 'a'  "e"  "i" or "o" or "u" or "A" or "E" or "I" or "O" or "U" :
def vowels_check(word,count,vowels):
  for i in range(len(word)):
    if word[i] in vowels:
      count+=1
  return count

word=input("enter the name")
count=0
vowels=['a'  ,"e"  ,"i" , "o" , "u" , "A" , "E" , "I" , "O" , "U" ]
print(vowels_check(word,count,vowels))