# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 11:10:33 2023

@author: 20pw39
"""
def apply_action(ch, bank1, bank2):
    if (ch == 1):
        if ('MAN' in bank1):
            if ('TIGER' in bank1):
                bank1.remove('MAN')
                bank1.remove('TIGER')
                bank2.append('MAN')
                bank2.append('TIGER')
            else:
                print('ACTION Denied: TIGER is not at bank1')
        else:
            print('ACTION Denied: MAN is not at bank1')
        return bank1, bank2

    if (ch == 2):
        if ('MAN' in bank2):
            if ('TIGER' in bank2):
                bank2.remove('MAN')
                bank2.remove('TIGER')
                bank1.append('MAN')
                bank1.append('TIGER')
            else:
                print('ACTION Denied: TIGER is not at bank2')
        else:
            print('ACTION Denied: MAN is not at bank2')
        return bank1, bank2


    if (ch == 3):
        if ('MAN' in bank1):
            if ('COW' in bank1):
                bank1.remove('MAN')
                bank1.remove('COW')
                bank2.append('MAN')
                bank2.append('COW')
            else:
                print('ACTION Denied: COW is not at bank1')
        else:
            print('ACTION Denied: MAN is not at bank1')
        return bank1, bank2

    if (ch == 4):
        if ('MAN' in bank2):
            if ('COW' in bank2):
                bank2.remove('MAN')
                bank2.remove('COW')
                bank1.append('MAN')
                bank1.append('COW')
            else:
                print('ACTION Denied: COW is not at bank2')
        else:
            print('ACTION Denied: MAN is not at bank2')
        return bank1, bank2

    if (ch == 5):
        if ('MAN' in bank1):
            if ('GRASS' in bank1):
                bank1.remove('MAN')
                bank1.remove('GRASS')
                bank2.append('MAN')
                bank2.append('GRASS')
            else:
                print('ACTION Denied: GRASS is not at bank1')
        else:
            print('ACTION Denied: MAN is not at bank1')
        return bank1, bank2

    if (ch == 6):
        if ('MAN' in bank2):
            if ('GRASS' in bank2):
                bank2.remove('MAN')
                bank2.remove('GRASS')
                bank1.append('MAN')
                bank1.append('GRASS')
            else:
                print('ACTION Denied: GRASS is not at bank2')
        else:
            print('ACTION Denied: MAN is not at bank2')
        return bank1, bank2

    if (ch == 7):
        if ('MAN' in bank1):
            bank1.remove('MAN')
            bank2.append('MAN')
        else:
            print('ACTION Denied: MAN is not at bank1')
        return bank1, bank2


    if (ch == 8):
        if ('MAN' in bank2):
            bank2.remove('MAN')
            bank1.append('MAN')
        else:
            print('ACTION Denied: MAN is not at bank2')
        return bank1, bank2


def validate(bank1, bank2):
  if ('TIGER' in bank1 and 'COW' in bank1 and 'MAN' not in bank1):
    print("xxxxxxxxxxxxxxxxxxxxxxxxxx GAME OVER xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("Oh no!! TIGER eaten COW in absence of MAN on bank1; you lost the game")
    return False
  #for bank 2
  if ('TIGER' in bank2 and 'COW' in bank2 and 'MAN' not in bank2):
    print("xxxxxxxxxxxxxxxxxxxxxxxxxx GAME OVER xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("Oh no!! TIGER eaten COW in absence of MAN on bank2; you lost the game")
    return False

  # COW and GRASS should not be on same bank in absence of MAN
  #for bank 1
  if ('COW' in bank1 and 'GRASS' in bank1 and 'MAN' not in bank1):
    print("xxxxxxxxxxxxxxxxxxxxxxxxxx GAME OVER xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("Oh no!! COW eaten GRASS in absence of MAN on bank1; you lost the game")
    return False
  #for bank 2
  if ('COW' in bank2 and 'GRASS' in bank2 and 'MAN' not in bank2):
    print("xxxxxxxxxxxxxxxxxxxxxxxxxx GAME OVER xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("Oh no!! COW eaten GRASS in absence of MAN on bank2; you lost the game")
    return False

  return True


bank1 = ['MAN', 'TIGER', 'COW', 'GRASS']
bank2 = []
print(bank1,bank2)
while True:
  if (len(bank2)==4):
    print("GOAL ACHIEVED!")
    break
  else:
    print("\nACTION")
    print("ACTION 1: MAN takes TIGER from bank1 to bank2")
    print("ACTION 2: MAN takes TIGER from bank2 to bank1")
    print("ACTION 3: MAN takes COW from bank1 to bank2")
    print("ACTION 4: MAN takes COW from bank2 to bank1")
    print("ACTION 5: MAN takes GRASS from bank1 to bank2")
    print("ACTION 6: MAN takes GRASS from bank2 to bank1")
    print("ACTION 7: MAN go alone from bank1 to bank2")
    print("ACTION 8: MAN go alone from bank2 to bank1")
    ch = int(input("Enter action number to apply: "))
    bank1, bank2 = apply_action(ch, bank1, bank2)
    print("\nSTATUS")
    print("CURRENT STATE:")
    print("Bank 1:", bank1)
    print("Bank 2:", bank2)
    if (validate(bank1, bank2) == False):
      break

