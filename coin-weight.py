
import random

class Coin:
  def __init__(self, pound):
    self.pound = pound


class Scale:
  def __init__(self):
    self.use = 0


  def getHeavierCoins(self, arrA, arrB):
    '''DO NOT EDIT THIS FUNCTION'''
    if(self.use == 3): 
      raise Exception("You can only use the weight coin function 3 times")
    else:
      self.use += 1

      
    weightA = sum([coin.pound for coin in arrA])    
    weightB = sum([coin.pound for coin in arrB])    
    if weightA > weightB:
      return arrA

    if weightA < weightB:
      return arrB

    if weightA == weightB:
      return None



def createRandomCoinArray():
    '''DO NOT EDIT THIS FUNCTION
    Return an array of 12 coin but one of the coin is weighted differently.'''
    coinList = []
    for x in range(0, 11):
      coinList.append(Coin(2))

    if random.randint(0,1) == 0:
      coinList.append(Coin(1))
    else:
      coinList.append(Coin(3))

    random.shuffle(coinList)

    return coinList

    



def findUniqueCoin():
    '''TODO: Return Index of the Unique Coin.'''
    coinList = createRandomCoinArray()
    scale = Scale()

    response1 = scale.getHeavierCoins(coinList, coinList)
    response2 = scale.getHeavierCoins(coinList, coinList)
    response3 = scale.getHeavierCoins(coinList, coinList)

    return coinList[0] #EDIT TO RETURN ACTUAL COIN


uniqueCoin = findUniqueCoin()
print(uniqueCoin.pound)