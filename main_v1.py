import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

N = 172
a = 0.1
L = 1.772
k = 75
v = 0.6
dt = 0.005
no_states = 2          # rattler(0) and non-rattler(1)
no_actions = 2         # run(1) and tumble(0)
Q = np.zeros((N,2,2))  # Q-matrix for each of the N particles

def state(X, Y, a):
    states = np.zeros(N)
    for i in range(N):
        cnt = 0        # Conatcts
        for j in range(N):
            if (j!=i):
                r = np.sqrt((X[i] - X[j])**2 + (Y[i] - Y[j])**2)
                if (r <= 2*a):
                    cnt = cnt + 1
                if(cnt == 3):
                    states[i] = 1   # Non-rattler
                    break
    states = states.astype(int)
    return states

def action(epsilon, n, states):
    p = (epsilon)**n
    actions = np.zeros(N)
    for i in range(N):
      act = random.choices(['random_action', 'optimal_action'], weights=(p, 1-p), k = 1)[0]  # epsilon-greedy
      if (act == 'random_action'):
        actions[i] = random.randint(0,1)
      if (act == 'optimal_action'):
        q = Q[i][states[i]]
        actions[i] = np.where(q == np.max(q))[0][0]
    actions = actions.astype(int)
    return actions

def motion(X, Y, Theta, v, dt, actions):
    # Run and tumble motion
    X = X + np.multiply(actions, v*np.cos(Theta)*dt)
    Y = Y + np.multiply(actions, v*np.sin(Theta)*dt)
    Theta = Theta + (1 - actions)*np.random.normal(0,np.pi/50)
    X = X%L
    Y = Y%L
    return X,Y

def reward(X, Y, a, t):
    rewards = np.zeros(N)
    for i in range(N):
        x_i = X[i]
        y_i = Y[i]
        for j in range(N):
            if (j!=i):
                x_j = X[j]
                y_j = Y[j]
                r = np.sqrt((x_i - x_j)**2 + (y_i - y_j)**2)
                if (r < 2*a):
                    rewards[i] += -k*(r -2*a)**2 - t    # Negative of potential energy
    return rewards

def Q_learn(episodes, gamma):
    epsilon = 0.1
    # episodes : No. of  episodes of learning
    # alpha = learning rate
    # gamma = discount factor
    for n in range(episodes):
        alpha = 0.1
        X = np.random.uniform(0, L, N)
        Y = np.random.uniform(0, L, N)
        Theta = np.random.uniform(0, 2*np.pi, N)
        for t in range(1001):
            states = state(X, Y, a)
            actions = action(epsilon, n, states)
            X,Y = motion(X,Y,Theta,v,dt,actions)
            rewards = reward(X,Y,a, t)
            for i in range(N):
                new_state = state(X,Y,a)
                Q[i][states[i]][actions[i]] = (1 - alpha)*Q[i][states[i]][actions[i]] + alpha*(rewards[i] + gamma*np.max(Q[i][new_state[i]]))
            print('t')
            if(t % 100 == 0):
                fig, ax = plt.subplots()
                circle = []
                for i in range(N):
                  circle.append(plt.Circle((X[i], Y[i]), a, facecolor='red', edgecolor='black'))
                for i in range(N):
                  ax.add_patch(circle[i])
                plt.xlim(0,L)
                plt.ylim(0,L)
                plt.savefig(f'p_{t}')
            if(t==1000):
              Q_t = Q.reshape((N, -1))  # temporary
              df = pd.DataFrame(Q_t)
              df.to_csv(f'Qval_{n}.csv')


        print(f'episode {n} completed')

if __name__ == '__main__':
    Q_learn(1, 0.99)

