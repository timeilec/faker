# Report for Assignment 1

## Project chosen

Name: Faker
URL: https://github.com/timeilec/faker

Number of lines of code: 308.5 KLOC
The tool used to count the lines of code: lizard

Programming language: Python

## Coverage measurement

### Existing tool
    
The existing tool we used to measure the coverage was Coverage.py. We used GitHub Search filters to find repositories that matched the language we wanted to use and had enough contributors. We then forked them and ran tests such as counting lines and calculating coverage.

![overall-coverage-initial](https://hackmd.io/_uploads/SkwDvNdIA.png)

### Your own coverage tool

#### Group member: Kacper

Function 1: loading.py get_path()

https://github.com/joke2k/faker/commit/609bf2315cd3f10ed7576d771d1c2be4d97e4dd1

Function 2: loading.py list_module()

https://github.com/joke2k/faker/commit/609bf2315cd3f10ed7576d771d1c2be4d97e4dd1

![Screenshot 2024-06-20 at 14.44.30](https://hackmd.io/_uploads/HJVdS-9UA.png)

    
#### Group member: Maja

Function 1: generator.py add_provider()
    
Commit showing the added test case:

https://github.com/timeilec/faker/commit/568657fad6c2e1e6492fde9b8eb398566c60593c

Commit showing changes to generator.py file:

https://github.com/timeilec/faker/commit/6b7cc2f37881d8d4e12dac20e6622f95933c5c0b

![Screenshot 2024-06-24 at 16.02.29](https://hackmd.io/_uploads/Bkmut4O80.png)



Function 2: generator.py provider()

https://github.com/timeilec/faker/commit/568657fad6c2e1e6492fde9b8eb398566c60593c

![Screenshot 2024-06-20 at 14.42.05](https://hackmd.io/_uploads/BkO9KE_80.png)

    
#### Group member: Tim
    
Function 1: distribution.py choices_distribution()
    
https://github.com/timeilec/faker/commit/4ff8fa50c001ffe20b2c13496eb40568d93199f4
    
![Screenshot 2024-06-25 at 14.15.52](https://hackmd.io/_uploads/S18ZSE_IR.png)
    
Function 2: distribution.py random_sample()
    
https://github.com/timeilec/faker/commit/4ff8fa50c001ffe20b2c13496eb40568d93199f4

    
![Screenshot 2024-06-25 at 14.14.18](https://hackmd.io/_uploads/BJ66E4OL0.png)

    
#### Group member: Presyian

Function 1: cli.py print_doc()
    ![Screenshot 2024-06-25 at 14.11.15](https://hackmd.io/_uploads/S1lxNEdIC.png)

Function 2: cli.py execute_from_command_line()

![Screenshot 2024-06-25 at 14.12.39](https://hackmd.io/_uploads/HJVH4VdLR.png)

https://github.com/timeilec/faker/commit/8fd865a3fd22af352aa0b45bf00abcb3bacd0f45
    
https://github.com/timeilec/faker/commit/faddb51536709d8541f9adc9d5022d8c811301c3

## Coverage improvement

### Individual tests
    
#### Group member: Kacper

Function 1: loading.py get_path()
Function 2: loading.py list_module()
    
(both tests are included in the same commit)
    
https://github.com/joke2k/faker/commit/609bf2315cd3f10ed7576d771d1c2be4d97e4dd1
    

Old coverage:

![Screenshot 2024-06-20 at 14.44.30](https://hackmd.io/_uploads/r1ugKjbIA.png)

New coverage:
    
![Screenshot 2024-06-20 at 14.39.46](https://hackmd.io/_uploads/H1dWti-8A.png)

Improvement get_path(): 57% (4/7) to 85% (6/7)

The coverage was improved becuase branches that were previously not accessed are now being tested by the new tests (get_path_frozen). The tests accesses the new branches by simulating a condition that was previously not tested.
    
Improvement list_module(): 50% (1/2) to 100% (2/2)
    
The function list_module previously had no tests and to improve it's coverage a test for the function was added that activated True condition.

    
#### Group member: Maja

Commit showing the added test case:

https://github.com/timeilec/faker/commit/568657fad6c2e1e6492fde9b8eb398566c60593c

Commit showing changes to generato.py file:

https://github.com/timeilec/faker/commit/6b7cc2f37881d8d4e12dac20e6622f95933c5c0b
    
Old Coverage:

![old](https://hackmd.io/_uploads/SkwahgvIA.png)

    
New Coverage:

![new](https://hackmd.io/_uploads/By3eTlvUC.png)
  
Improvement: 5/6 (83.(3)%) to 6/6 (100%)

Justification for improvement: Having 6 branches where 5 were already hit, the improvement could only be possible if the first if statement in the function was executed. It was possible by creating a new use case to test this specific branch, "add_provider_1".
    
Function 2: generator.py provider()
    
https://github.com/timeilec/faker/commit/568657fad6c2e1e6492fde9b8eb398566c60593c

Old Coverage:
    
![old](https://hackmd.io/_uploads/H1n0wjb8R.png)

New Coverage:
    
![new](https://hackmd.io/_uploads/S1Tc_oZIA.png)

Improvement: 0/2 (0%) to 2/2 (100%)
    
Justification for improvement: Having none of the branches hit of the exception, the improvement of 80% was possible when two branches were hit. It was possible by creating a new use case to test these branches, "provider_1", "provider_2".

#### Group member: Tim
    
Function 1: distribution.py choices_distribution()
    
https://github.com/timeilec/faker/commit/4ff8fa50c001ffe20b2c13496eb40568d93199f4

Old coverage:
    
![1](https://hackmd.io/_uploads/rJwgHjbLR.png)
    
New coverage:
    
![2](https://hackmd.io/_uploads/rkWVSsbIR.png)

Improvement: 5/8 (62.5%) to 6/8 (75%)
    
The improvement is due to the fact that a new branch was hit "choices_distribution_4". This branch was a case where hasattr(random, "choices") was false and this case was not tested. To get around this, we passed in a testMode bool to force execution down the else branch and simulate this condition.

Function 2: distribution.py random_sample()
    
https://github.com/timeilec/faker/commit/4ff8fa50c001ffe20b2c13496eb40568d93199f4

Old coverage:
    
![2](https://hackmd.io/_uploads/SyW2Bj-LR.png)
    
New coverage:
    
![3](https://hackmd.io/_uploads/r1YhBjWIC.png)

Improvement: 6/8 (75%) to 7/8 (87.5%)
    
The improvement is due to the fact that a new branch was hit "random_sample_1" after adding the test case test_random_sample in test_utils.py. This function was not previously tested.
    
#### Group member: Presiyan

Function 1: cli.py print_doc()
    https://github.com/timeilec/faker/commit/8fd865a3fd22af352aa0b45bf00abcb3bacd0f45

Old Coverage:
![Screenshot 2024-06-20 at 16.02.54](https://hackmd.io/_uploads/HJ6qLnb8A.png)

New Coverage:
![Screenshot 2024-06-20 at 16.03.30](https://hackmd.io/_uploads/SyR2LhWIR.png)

Improvement: 8/11(72%) to 9/11(81%)
    
Justification for improvement:

There was a branch that hit only if the output was none, meaning an error somewhere along the way. I added a case where it forced the function to run with output parameter as None to check if the condition would execute properly (improved an existing test).
    

Function 2: cli.py execute_from_command_line()

https://github.com/timeilec/faker/commit/faddb51536709d8541f9adc9d5022d8c811301c3

Old Coverage:
![Screenshot 2024-06-20 at 16.03.56](https://hackmd.io/_uploads/S120L2-L0.png)

New Coverage:
    ![Screenshot 2024-06-20 at 16.04.23](https://hackmd.io/_uploads/rkzxD3-LR.png)

Improvement: 0/2(0%) to 2/2(100%)

Justification for improvement:
The function used for running commands from command line was not tested at all. I added 2 test cases, one testing with encoding as None, and one with forcing encoding to be UTF-8. Both branches are now properly tested and improved the coverage. 

### Overall

Old coverage results
    
![overall-coverage-initial](https://hackmd.io/_uploads/ByaPr4OUC.png)
    
New coverage results

![overall-coverage-final](https://hackmd.io/_uploads/H1WdB4dUA.png)
    
We can clearly see the increase in hits from 10202 to 10235 and decrease in misses from 449 to 416.


## Statement of individual contributions
    
### Kacper

Imrpoved branch coverage of the file loading.py from 85% to 95%. I did that by improving the coverage of two functions: get_path and list_module. By storing status of the covered branches in the dictionary I could make sure that over 80% of branches are hit in both functions (85% for get_path and 100% for list_module)
    
### Maja
    
Improved the overall branch coverage of the generator.py file from 80% to 96%. In this file I checked for branch hits and misses by adding marks to branches to evaluate which functions need improving. Test cases were added for add_provider() and provider() functions to imrpove their branch coverage. The formers imrpovement went from 83.(3)% to 100% and the former from 0% to 100%.

### Tim
    
Instrumented the distribution.py file to check branch coverage by storing status in a dictionary. Extended an existing test case test_choice_distribution() for choices_distribution() and added a new test case test_random_sample() to improve branch coverage of my chosen functions.
    
### Presiyan
Improved the coverage of print_doc() function in the cli.py file from 72% to 81%. Improved the coverage of execute_from_command_line function in the cli.py file from 0% to 100%. 