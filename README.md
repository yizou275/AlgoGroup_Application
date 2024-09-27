# Algo Group UChicago Assessment (READ UNTIL END)
- In this assignment, we are looking for solutions that are efficient, demonstrate high quality code, and are production ready. 
- Answer **ONE** of the questions of your choice, include testing you ran on code, and _briefly_ explain the reasoning behind your solutions. 
- Any coding language is acceptable so long as we can easily verify that your solutions are correct (the example files are in C++/Python, but you need not use/follow them at all).
- We are NOT looking for elaborate write-ups or hundreds of lines of code, **nor do we want you to spend more than 1 hour on this**. We just want to get a feel for your technical abilities, thoroughness, and general approach to problem solving!

## Questions
We don't have a preference for which problem you solve, but our evaluation of tougher tasks will be more lenient. Simply follow the instructions for the question you choose.

### Option 1: FIND DUPLICATE
- Implement a function to identify a duplicate integer in an unsorted array. Ideally, you would write 2 different solutions with different time/space performance.
- Given an array of exactly $N+1$ numbers, where each of the numbers in range $[1,N]$ appears at least once, find the number that appears more than once.
- Write a sentence or two describing the performance of your solution(s).
- Write tests and attach their results in the repo to prove correctness.
- See [option1.cpp](./find-duplicate/option1.cpp) / [option1.py](./find-duplicate/option1.py) to get started (note that you may use any language, test frameworks, file structures, etc.) so long as your completion of the task is clear.

### Option 2: IMPLEMENT STACK (HARDER)
- Implement an integer stack WITHOUT containers (list, vector, array, etc.).
- It should have methods:
  - `push` adds an integer to the top and does not return anything
  - `pop`  returns and removes the integer at the top. If the stack is empty, an error is thrown
  - `peek` returns the integer at the top. If the stack is empty, an error is thrown
  - `size` returns an integer: the number of values on the stack
  - More info about stacks can be found here: https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
- [Optional] Write tests and attach their results in the repo to prove correctness.
- See [option2.cpp](./implement-stack/option2.cpp) to get started (note that you may use any language, test frameworks, file structures, etc.) so long as your completion of the task is clear.

### Option 3: GREEN SCREEN (HARDEST)
- See [option3.cpp](./green-screen/option3.cpp) for details.
- Write tests and attach their results in the repo to prove correctness.

## Steps to follow
1. Set up a GitHub repository and a local directory to work out of (see the **Set up submission on GitHub** section below).
2. In README.md, delete this content and clearly state which question you are answering at the top.
3. Add your reasoning/methodology for said question.
4. Delete all irrelevant files, and attach your solution along with any tests you may have written.
5. If you wrote tests, attach proof that the tests you ran are passing (proof of correctness) in the repo.
6. Make the repo public and attach a link in the application form for us!

## Set up for submission on GitHub
1. [Create a GitHub account here](https://github.com/signup).
2. Make sure Git is installed locally. The easiest way to check is by running `git --version`. If you need help installing Git, contact an Algo Group board member!
3. Create a new repository on the GitHub web UI—its name doesn't matter, but make sure it's public.
4. Create a local directory on your machine to work out of. Enter that directory.
```
mkdir algo-group-take-home
cd algo-group-take-home
```
5. Connect this local repository to both your new GitHub repository, and the upstream Algo Group repository.
```
git init
git remote add origin [Your GitHub repository HTTPS URL]
git remote add upstream https://github.com/Algo-Group-UChicago/takehome-assessment.git
git pull upstream main
git branch -M main
git push -u origin main
```
6. To push your local changes to your GitHub repository, enter your local directory and enter the following commands:
```
git add .
git commit -m "[COMMIT MESSAGE]"
git push
```

*If you run into major issues with Git/GitHub, feel free to simply upload your code files to Google Drive and include the shared link in your application.*

## Good luck!
We don't expect you to know everything coming into Algo Group, and this is just meant to emulate a light takehome that you might receive in the recruitment process. We don't expect you to spend more than 1 hour on this. Even if you can't implement a full solution in an hour, definitely submit what you have, as we value commitment and enthusiasm over everything.
