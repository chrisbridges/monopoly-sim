import unittest

from utils.create_board import create_complete_monopoly_board

from models.spaces import spaces, rent_values

class Test(unittest.TestCase):
  # create board
  def test_board_creation(self):
    board = create_complete_monopoly_board()
    # first board space is "Go"
    self.assertEqual(board.head.name, 'Go')

  # def test_property_names_and_rent_names_match(self):
  #   names_dont_match = False
  #   for property_name in rent_values.keys():
  #     if property_name in spaces:
  #       print(property_name)
  #       continue
  #     else:
  #       names_dont_match = True
  #       # print(property_name)

  #   self.assertEqual(names_dont_match, False)

  # check board position 10 is Jail
  def test_board_traversal(self):
    board = create_complete_monopoly_board()
    spaceFiveStepsFromGo = 'Reading Railroad'

    moveFiveStepsForward = board.traverse_board(5)

    self.assertEqual(moveFiveStepsForward, spaceFiveStepsFromGo)
  # check board position 15 is Pennsylvania Railroad

  # create players

  # confirm all players are on Go w/ $1500 and have valid tokens

  # confirm player 1 is able to move 5 steps and purchase Reading Railroad

  # confirm player 2 is able to roll doubles, purchase property, and roll again

  # confirm that when a player rolls doubles 3 times, they end up in jail

if __name__ == '__main__':
  unittest.main()