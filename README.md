# RL-MIPS
### States
state = {rattler, non-rattler} = {0,1} <br>
Let the no. of other particles a prticle is in contact with be c.
#### i) Rattler 
c < 3
state = 0
#### ii) Non-rattler
c >= 3
state = 1

### Actions
action = {tumble,run} = {0,1} <br>
![image](https://user-images.githubusercontent.com/82452505/181905502-1b13ffd3-dffb-49f5-a341-12574c8d2d45.png)

### Reward
The reward given to each particle is negative of it's potential energy after each time step or we can say the penalty given to each particle is it's potential energy. The potential energy function used in the problem is given as <br>
$ U(r) = k*(r - 2*a)^2 ; r<=2a 
U(r) = 0 ; r>2a $
