#!/usr/bin/env python
# coding: utf-8

# In[4]:


x=1
print(x)
x_str=str(x)
print("my fav num is",x,".",x,"x=1")
print("mt fav num is", x_str, ".",x)


# In[5]:


text= input("type anything..")
print(5*text)
num=int(input("type anything.."))
print(5*num)


# In[6]:


text= input("type anything..")
print(5*text)
num=int(input("type anything.."))
print(5*num)


# In[7]:


abc<bca


# In[8]:


a<b


# In[9]:


"a"<"b"


# In[10]:


n=input("you are lost in forest\n*****************go left or right")
while n== "right" or n=="Right":
    n=input("you are lost in forest\n*****************go left or right")
    print( "\ngo out of the lost forest!\n \O/")


# In[12]:


n=input("you are lost in forest\n*************************\n")
while n== "right" or n=="Right":
    n=input("you are lost in forest\n**********************")
    n=input("are you mad change your plan |_|")
    print( "\n go out of the lost forest!\n \O/")


# In[25]:



x=input(" type value....")
while
x==1
print(x)


# In[34]:


x= int (input("x"))
y= int (input("y"))
print(x**y)
print (log (x))


# In[1]:


s="abc"
len(s)


# In[2]:


s[1:3]


# In[3]:


s="himani"
s[2:5]


# In[4]:


s[::]


# In[5]:


s[::-1]


# In[11]:


s="hello"
s='y'+ s[1:len(s)]
print(s)
#stringsareimmutable


# In[19]:


s = "himani"
 for index in range (len (s)):
 if s[index] == 'i' or s[index] == 'u':
print("There is an i or u")


# In[20]:


for char in s:
if char == 'i' or char == 'u':
print("There is an i or u")


# In[ ]:





# In[ ]:


an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))
i = 0
while i < len(word):
    char= word[i]
    if char in an_letters:
        print("Give me an " + char + "!" + char)
    else:
        print("Give me a " + char + "!" + char)
        print("What does that spell?")
    for i in range(times):
        print(word, "!!!")


# In[2]:


an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))
for char in word:
    if char in an_letters:
        print("Give me an " + char + "!" + char)
    else:
        print("Give me a " + char + "!" + char)
        print("What does that spell?")
    for i in range(times):
        print(word, "!!!")


# In[4]:


s1 = "mit u rock"
s2 = "i rule mit"
if len(s1) == len(s2):
    for char1 in s1:
        for char2 in s2:
            if char1 == char2:
                print("common letter")
                break


# In[5]:


cube = 8
for guess in range(cube+1):
    if guess**3 == cube:
        print("Cube root of", cube, "is", guess)


# In[13]:


cube = 8
for guess in range(abs(cube)+1):
    if guess**3 >= abs(cube):
        break
        if guess**3 != abs(cube):
            print(cube, 'is not a perfect cube')
        else:
                if cube < 0:
                    guess = -guess
                    print('Cube root of '+str(cube)+' is '+str(guess))


# In[ ]:


cube = 8
epsilon = 0.01
num_guesses = 0
low = 0
high = cube
guess = (high + low)/2.0
while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube :
        low = guess
    else:
            high = guess
            guess = (high + low)/2.0
            num_guesses += 1
            print ('num_guesses =', num_guesses)
            print (guess, 'is close to the cube root of', cube)


# In[ ]:


cube =27
epsilon = 0.01
num_guesses = 0
low = 0
high = cube
guess = (high + low)/2.0
while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube :
        low = guess
    else:
            high = guess
            guess = (high + low)/2.0
            num_guesses += 1
            print ('num_guesses =', num_guesses)
            print (guess, 'is close to the cube root of', cube)


# In[ ]:





# In[ ]:




