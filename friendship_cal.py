alphabet='qwuioplkjhgfdsaznm'
score=0
name=input('Enter your first name ande give space than enter second name;')
for character in name:
    if character in 'aeiou':
      score+=5
    if character in 'friends':
      score+=10
    if character in 'alphabet':
       score+=alphabet.find(character)
    else:
       score+=0
if score>=100:
    print("your friendship score is:",score) 
    print("you are best friend")
else:
    print("your friendship score is:",score) 
        

