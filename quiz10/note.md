# Solving quiz 10 by pen and paper
## List
[None, 65, 53, 62, 33, 49, 5, 51]\
## Tree:
```
            65
        53      62
      33  49  5   51
```
## Examin whether 65 can be inserted as the last number
### Sort the list:
[65, 62, 53, 51, 49, 33, 5]
- 51 is greater than 5
- 62 is greater than 53\
### Therefore:
- prepend 65 to preferred_sequence = [65]
- delete 65
### New tree:
```
            62
        53      51
      33  49  5
```
## Examin whether 62 can be inserted as the last number
### Sort the list:
[62, 53, 51, 49, 33, 5]
- 5 is the only child
- 51 is NOT greater than 53
### Therefore, try 53:





###
```
            65
        53      62
      33  49  5   51
```
delete 53
```
            65
         49     62
      33      5    51
```
65 49 62 33 5 51
```
            65
         51     62
      33   49  5
```

```
            62
        53      51
      33  49  5
```