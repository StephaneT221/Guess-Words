bad_letters = []
good_letters = ['_', '_', '_', '_', '_']
word = "hello"

game_over = False
while game_over == False:
  if good_letters == ["h", "e", "l", "l", "o"]:
    print()
    print("You win!!")
    game_over = True
    break

  if len(bad_letters) < 6:
    print()
    print("----------------------")
    print("-Guess your letter:")
    letter = input()
  
    if letter in word == "hello":
      if letter == "h":
        good_letters[0] = letter
      if letter == "e":
        good_letters[1] = letter
      if letter == "l":
        good_letters[2] = letter
        good_letters[3] = letter
      if letter == "o":
        good_letters[4] = letter
    else:
      bad_letters.append(letter)

    print()
    print("-----------------------")
    print("Good Letter:")
    print(good_letters)
    print("Bad Letters:")
    print(bad_letters)
  
  else:
    game_over = True
    print()
    print("You lost!")
    break



  