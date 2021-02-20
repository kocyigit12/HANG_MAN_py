

import random
import hangman_words as word_list
import hangman_art as art


random_word =random.choice(word_list.word_list)
blank =[]
chosen_list =[]
for i in range(0 ,len(random_word ) ):
    chosen_list.extend(random_word[i])

for i in range(0 ,len(random_word)):
    blank.append("_")
print(art.logo)
print("HANG MAN GAME !!\n")
print(blank)
# print(random_word)
# print(chosen_list)

health =len(random_word)
print(f"your health : {health}")



while health>0 :
  guess=input("Guess a letter\n")
  for  i in range (0,len(random_word)):

      if guess == chosen_list[i]:
          blank[i] = guess
          print(blank)

          continue
      elif not chosen_list.__contains__(guess) :
          health-=1
          try:
              print(art.stages[health])
          except IndexError:
               print("OUT OF RANGE")

          print(f"You have lost 1 health, Remain : {health}")
          break
  if not blank.__contains__("_"):
      print("You have win")

      exit(0)














