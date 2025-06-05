#### Blood groups

Humans have different blood groups: 1, 2, 3 and 4.  
Each person also has a Rhesus factor (Rh), which can be + (positive) or - (negative). 

A child's blood group is determined by the blood groups of their parents according to genetic inheritance rules: 

| Parent 1 | Parent 2 | Possible Child Blood Groups |
|:---------|:---------|:----------------------------|
| 1        | 1        | 1                           |
| 1        | 2        | 1, 2                        |
| 1        | 3        | 1, 3                        |
| 1        | 4        | 2, 3                        |
| 2        | 2        | 1, 2                        |
| 2        | 3        | 1, 2, 3, 4                  |
| 2        | 4        | 2, 3, 4                     |
| 3        | 3        | 1, 3                        |
| 3        | 4        | 2, 3, 4                     |
| 4        | 4        | 2, 3, 4                     |

For example if parents have blood groups 1 and 4, child blood group may be either 2 or 3, according the table. 

##### Task 1 - creating a new human

Create a class `Human`. Add attribute `blood_group`. 

Add possibility to create a new `Human` object using `+` sign (implement method `__add__`). 

New object should have a blood_group according table rules.

> Note: use `random` to select one of possible groups


##### Task 2 - multiple generations

Create a list of 64 humans. Assign random blood group to each.  

Now, create pairs and get a child form each pair. For all children, create pairs and get a child for each...  
Repeat this process multiple time until only 1 person remaining 


Print blood group of that remaining person 

