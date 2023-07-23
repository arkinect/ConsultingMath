# ConsultingMath
A friend asked for a free alternative to online math sites used to practice math for mangement consulting interviews.
_this was at one point named cloneConsultingMath because I somehow screwed up committing to github from VS Code

## Use (?)

## Developer Log

### Version 1:
_This version was never posted to github but relevan files can be found in the directory consultingMath Distrobution_

This version focussed on me being able to think about how to generate relevan consulting math questions which all had integer solutions, and implementing question asking and answering just as text in a command line.
I then used auto-py-to-exe to convert this simple version into an executable which could be shared. Unfortunately my friend has a mac and this executable didn't work on the mac so for my final product I'll hav to find a way of doing it that works on mac.

All told, this took maybe 2 evenings.

### Version 2:
_At time of writting this is sort of a pre-release to a friend?_

Friend complained that the text only version was kinda ugly and that I should try and make it "Windowed" so now I get to explore GUIs.
Last time I did this I used pysimpleGUI but that was back in grade 10, and I figured I'd take this as an opportunity to try something new and a little more sophistocated. 
My friend does a lot o UI design and so plotted out some designs for me to follow in Figma, In trying to find a good library to make GUIs with, I found a page talking about a tkinter command to convert Figma designs into python code and figured I'd give that a shot. 

TLDR, the command didn't work very well, but I was able to use some of what was produced a base for then writting the pages myself.

At time of writting I have now completed the home page, a page asking how many of the selected question one would like to answer (so you can line up a series of questions to practice with) and a page to display the question / take the user aswer / give feedback to the user.

In all cases, this is what my friend asked for and so I'll probably switch over to try and find a way to package this up so it runs on mac. However there are some features I still want to add because I think users would find them useful.

1. __An explanation of why their answer is wrong, and the correct solution:__ Right now the answer page just says whether or not you were correct, and what the correct answer is, not how to get that correct answer. If this is to be used as a learning tool, I probably want that in here.

2. __Tracking of scores over time:__ As part of the _Version 1_ I had a text output of their scores, but havn't implemented that yet. I would also like the score to be written to a text file so if asked I can display their progress over time in terms of number of questions answered, and % correct

3. __Timeed questions:__ For a lot of people practicing for these intervews, speed is a siginificant factor, so along with # answered, and % correct, I'd like to be able to offer stats on how long was spent on a question on average, ideally also with progress tracking over time (Think aimlabs)

### Version 3:
_Still to come, ideally with the features mentioned above and more_
