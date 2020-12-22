#!/usr/bin/env python
# coding: utf-8

# In[67]:


print ('First Assignment of Elif Ozmutlu')
# Manually choosen values from different types

a= 8.19
b= 133
c= "q"
d,e= True, False
f= "724"

# With "f-string" usage

print (f'\nValue of a: {a}')
print (f'Value of b: {b}')
print (f'Value of c: {c}')
print (f'Value of d and e: {d,e}')
print (f'Value of f: {f}')

# In one line

print (f'\nValue of a, b, c, d, e and f: {a, b, c, d, e, f}')


print (f'\nType of a: {type(a)}')
print (f'Type of b: {type(b)}')
print (f'Type of c: {type(c)}')
print (f'Type of d and e: {type(d)}')
print (f'Type of f: {type(f)}')

# With "format" usage

print ("\nValue of a is {}".format(a))
print ("Value of b is {}".format(b))
print ("Value of c is {}".format(c))
print ("Value of d and e is {}".format(d)+" and " +format(e))
print ("Value of f is {}".format(f))

# In one line
print ("\nValue of a, b, c, d, e and f is {}".format(a)+", "+format(b)+", "+format(c)+", "+format(d)+", "+format(e)+" and "+format(f))

print("\nType of a is {}".format(type(a)))
print("Type of b is {}".format(type(b)))
print("Type of c is {}".format(type(c)))
print("Type of d and e is {}".format(type(d)))
print("Type of f is {}".format(type(f)))


# In[ ]:




