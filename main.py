import random, sys, time
from getkey import getkey

#colours
reset = "\033[0m"
dim = "\033[2m"
underline = "\033[4m"
blue = "\033[1;34m"
red = "\033[1;91m"
green = "\033[1;32m"

#just all of the different passages
strings = [
  "Typing speed is measured by the number of words you can type correctly in a set amount of time. A word is equivalent to five keystrokes. During a test, both speed and accuracy are measured. You will receive a number that indicates your average words per minute (WPM) and a percentage that indicates your accuracy.",
  "Now we have devised robots that are much more complicated than any other machines we have ever had. They are complicated enough to do jobs that until now only human beings could do, but that are too simple for the marvellous brains we all have. The robots, even though they are smarter than other machines, are still only capable of very simple tasks - the kind of tasks human beings ought not to waste their time doing. In that case, why not let the robots do it? Why shouldn't human beings do other and better things? After all, whenever there is an important new invention, some jobs are lost. When the automobile came into use, there was a gradual, but steady, loss of jobs that involved horses. There were fewer stables, fewer manufacturers of buggies and wagons, fewer whips, and fewer spurs. On the other hand, think of the jobs the automobile created. Think of all the garages that came into being, all the auto mechanics needed, all the tyre manufacturing, highway building, oil well drilling. Automobiles created hundreds of times as many jobs as they destroyed. That's the way it will be with robots too. Lots of assembly-line jobs will vanish, but think of all the jobs needed to design robots, manufacture their parts, put them together, install them, and keep them in good repair, There will be many times as many jobs coming into being as are destroyed. The jobs that are destroyed will be very dull ones anyway, so dull that even a robot can do them. The jobs that will be created will be interesting ones that will stretch the mind. Of course, there is a catch. We can't just tell a person who has been working on an assembly line for twenty-five years to stop and take a job designing robots instead. It takes a special kind of education to be able to work with robots, and assembly-line worker won't have it. If we are going to have a large changeover in types of jobs, there will have to be a careful programme of retraining and re-education for people with old-style jobs. It will have to be done even if they take rather simple new-style ones. That Will be expensive and hard, but it will have to be done. There are also sure to be people who are too old, or too beaten down by the dull job they had to do all their lives, to be able to take advantage of retraining. Some sort of jobs will have to be found that they can do. Eventually, of course, things will be different. Children going to schools in the future will be educated in ways or using and understanding computers and robots. They will grow up and De able to take the new jobs, and no one will ever consider the old jobs or want them. Everyone will be glad to leave the dull jobs and the dangerous jobs too.",
  "In computing, a printer is a peripheral device which makes a persistent representation of graphics or text, usually on paper. While most output is human-readable, bar code printers are an example of an expanded use for printers.",
  "The first commercial printers generally used mechanisms from electric typewriters and Teletype machines. The demand for higher speed led to the development of new systems specifically for computer use.",
  "In a speed typing contest contestants compete to attain the highest accurate typing speeds. These contests have been common in North America since the 1930s and were used to test the relative efficiency of typing with the Dvorak and QWERTY keyboard layouts.",
  "A computer is a machine that can be instructed to carry out sequences of arithmetic or logical operations automatically via computer programming. Modern computers have the ability to follow generalized sets of operations, called programs.",
  "Since the first dinosaur fossils were recognized in the early 19th century, mounted fossil dinosaur skeletons have been major attractions at museums around the world, and dinosaurs have become an enduring part of world culture.",
  "A book is a medium for recording information in the form of writing or images, typically composed of many pages bound together and protected by a cover.",
  "A touch typist will know their location on the keyboard through muscle memory, the term is often used to refer to a specific form of touch typing that involves placing the eight fingers in a horizontal row along the middle of the keyboard and having them reach for specific other keys.",
]


def write(text):
  sys.stdout.write(text)


def clear():
  sys.stdout.write("\033[2J\033[H")


def countdown(num, text):
  for i in range(num, 0, -1):
    clear()
    print(reset + "String is: " + red + underline + text + reset)
    print(str(i))
    time.sleep(1)


ready = input(
  underline + green + "Welcome to Daivik's typing speed test!!\n\n" +
  reset +
  "You enter every letter individually, if you get a letter wrong, you must enter it until it is correct.\nIt will all become clear.\n\nAre you ready? (Press Enter)"
)

tries = 0
totalwpm = 0
bestWPM = 0

totalAccuracy = 0

play = "y"

while play == "y":
  #chooses the random passage
  string = random.choice(strings)

  countdown(3, string)

  complete = False
  currentLetter = 0
  wrong = 0
  time1 = time.time()
  while not complete:
    if currentLetter > 0:
      #if the letter isn't the first one in the string, then dim all the letters before the current one
      doneString = reset + dim + string[:currentLetter]
    #underline the current letter
    current = underline + blue + string[currentLetter]
    #reset the colour for all the ones after the current letter
    afterCurrent = reset + string[currentLetter + 1:]

    clear()
    if currentLetter == 0:
      print(current + afterCurrent)
    else:
      print(doneString + current + afterCurrent)

    #detects what key is pressed
    inputChar = getkey()
    while inputChar != string[currentLetter]:
      #if you put the wrong letter in
      wrong += 1
      #underlines the current letter, showing that you have got it wrong
      current = underline + red + string[currentLetter]
      clear()
      if currentLetter == 0:
        print(current + afterCurrent)
      else:
        print(doneString + current + afterCurrent)

      #input the letter again
      inputChar = getkey()

    #have they gone through the whole passage
    if currentLetter >= len(string) - 1:
      complete = True

    #increments the current letter variable
    currentLetter += 1

  # all the calculations
  tries += 1
  time2 = time.time()
  clear()
  timeTaken = (time2 - time1) / 60

  wpm = round((len(string) / 5) / timeTaken)
  totalwpm += wpm
  if wpm > bestWPM:
    bestWPM = wpm
  average = round(totalwpm / tries)
  accuracy = round(100 - ((wrong / (len(string) + wrong)) * 100))
  totalAccuracy += accuracy
  avrgAcc = round(totalAccuracy / tries)

  text = reset + "Well done!\n\nWPM: " + green + str(
    wpm) + reset + "\nAverage WPM: " + green + str(
      average) + reset + "\nYour Highest: " + green + str(
        bestWPM) + reset + "\n\nAccuracy: " + green + str(
          accuracy) + "%" + reset + "\nAverage Accuracy: " + green + str(
            avrgAcc) + "%\n"

  print(text)

  play = input("Play again or see leaderboard? (y/n)").lower()
  while play not in ["y",  "n"]:
    clear()
    print(text)
    play = input("Play again or see leaderboard? (y/l/n)").lower()
  if play == "y":

    clear()
    print(text)
    play = input("Play again? (y/n)").lower()
    while play not in ["y", "n"]:
      clear()
      print(text)
      play = input("Play again? (y/n)").lower()

clear()
print(green + "BYE!!!!" + reset +
      "\n\n\nComment your highscores!\n\nUpvote if you had fun\n\n:)")
