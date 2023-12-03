# range

`range` is a function.
It is used to generate a sequence of numbers `range(3)`. This will generate: 1, 2, 3. It produces a 'range object', if we want to put this number in a list we need something like `my_list = list(range(3)`. In a similar way we can assign after conversion the content of the range object a a tuple (`my_tuple = tuple(range(3))`), a set (`my_set = set(range(3))`)

- range can take 1, 2 or 3 arguments:
  - _single argument_: range(3) generates 1, 2, 3.
  - _two arguments_: range(5, 8) generate 5, 6, 7. The firs arguments is the start, the second is the stop, which is not included in the range.
  - _three arguments_ range(5, 8, 2) generate 5, 7. The third arguments is 'step' and define the unit of the increment.

In a 'for' loop the range take over the definition of the range on which we loop (the second condition of a while loop and define also the way we increment it)

```c
for(int i = 0; i < 0 i++)
	printf("%d\n", i);
```

```python
for i in range(1, 10)
	print(i)
```
