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
The reward given to each particle is negative of it's potential energy after each time step or we can say the penalty given to each particle is it's potential energy. The potential energy function U(r) is given as <br>
![image](https://user-images.githubusercontent.com/82452505/181905920-1e6a84ab-c8f7-4aaa-9ad0-f04de8f3b1ed.png)
<br>
In this way the Q-learning algorithm maximizes reward and hance minimizes potential energy of the system in the steady state.

