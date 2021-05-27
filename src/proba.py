import Global_Par as Gp
import random
def ratio(dis):
   if dis <= Gp.com_dis/4:
       return 1
   else:
       y = -20/((3/4)*Gp.com_dis)*dis + 80 + (20*4)/3
       a = random.uniform(1,100)
       if a <= y:
           return 1
       else:
           return 0

