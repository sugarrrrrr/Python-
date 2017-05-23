import random

#じゃんけん関数
def janken(n):
  global result
  result=[]
  i=1
  
  while i<=n: #n回だけじゃんけんを繰り返す
    
    # 自分の手を決める関数
    def my():
      my_hand =input('じゃんけん...：') #自分の手の入力
      
      # g.c.pが入力されているか判定
      while True:
        if my_hand=='g' or my_hand=='c' or my_hand=='p':
          break
        else:
          print('g(グー)かc(チョキ)かp(パー)を入力してください')
          my_hand=input('最初はグー、じゃんけん...：')
          continue
          
      # 自分の手の数値化
      if my_hand=='g':
        return 0
      elif my_hand=='c':
        return 1
      elif my_hand=='p':
        return 2
      
    # コンピューターの手を決める関数
    def cp():
      hand=['g','c','p']
      cp_hand = random.randint(0,2)
      print('コンピューター：',hand[cp_hand])
      return cp_hand


    # 勝負の判定
    def judge():
      while True: # あいこなら続ける
        x=(my()-cp()+3)%3
        if x==0:
          print('あいこです')
          continue
        elif x==1:
          print('あなたの負けです')
          result.append(0)
          break
        elif x==2:
          print('あなたの勝ちです')
          result.append(1)
          break
    
    judge()


    print('')    
    i+=1


# 勝率を求める関数
def win_rate():
  new_result=sum(result)
  rate = new_result/5*100
  print('じゃんけんの勝率は',rate,'％です')



janken(5)
win_rate()




