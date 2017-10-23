from random import randint
from random import seed

def roll_dice():
    """ roll_dice
Generate random string from '一' to '六'
    Arguements: None
    Returns: a string
    """
    chinese_dice_book = {
1:'\
               \n\
               \n\
               \n\
一一一一一一一一\n\
               \n\
               \n',
2:'\
               \n\
  二二二二二二  \n\
               \n\
               \n\
二二二二二二二二\n\
               \n',
3:'\
               \n\
  三三三三三三  \n\
               \n\
    三三三三    \n\
               \n\
三三三三三三三三\n',
4:'\
四四四四四四四四\n\
四   四  四   四\n\
四  四   四   四\n\
四四        四四\n\
四            四\n\
四四四四四四四四\n',
5:'\
  五五五五五五五\n\
       五      \n\
  五五五五五五  \n\
     五    五  \n\
    五   五    \n\
五五五五五五五五\n',
6:'\
     六        \n\
       六      \n\
六六六六六六六六\n\
    六    六   \n\
  六       六  \n\
六          六 \n',
}
    roll = chinese_dice_book[randint(1, 6)]
    return roll


if __name__ == "__main__":
    seed()
    print(roll_dice())