# How to create a string out of a list of char

The best method is;

```python
char_list = ['h', 'e', 'l', 'l', 'o']
word = ''.join(char_list)
print(word)
```

But if you need to do it while looping of the list of chars you have two possibiities:

```python
char_list = ['h', 'e', 'l', 'l', 'o']
word = ''

for char in char_list:
    word = ''.join([word, char])

print(word)

```

```python
char_list = ['h', 'e', 'l', 'l', 'o']
word = ''

for char in char_list:
    print("Processing character:", char)

    word += char

print(word)
```
