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
### Algorithm
1. determine state s<sub>k</sub> of each particle. <br>
2. determine action a<sub>k</sub> to take according to epsilon-greedy rule: <br>
         random action ; with probability  (epsilon)<sup>n</sup> <br>  
         argmax<sub>a</sub> Q<sub>s<sub>k</sub>a<sub>k</sub></sub> ; with probability 1- (epsilon)<sup>n</sup> <br>
         where (epsilon)<sup>n</sup> = (0.995)<sup>n</sup> $ and n is the no. of episode. <br>
3. translate all particle positions according to action taken <br>
 ![image](https://user-images.githubusercontent.com/82452505/181906823-0c5ab433-d205-4e0f-b117-2799ffecf389.png) <br>
4.  Give reward R<sub>k</sub> to each particle.
5.  Update Q-matrix according to Bellman equation 
![image](https://user-images.githubusercontent.com/82452505/181906925-be89f7ed-b7a6-4ed6-a350-bb381a188a98.png)
6. Repeat until Q converges to optimal values  Q<sup>*</sup>  and agents starts acting according to optimal policy in the environment.
 
