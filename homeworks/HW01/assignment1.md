# Homework #1

- (a) Define the dynamic system model, including the state $x_k$, control input $u_k$, and the state equation. Also, define a cost function to solve the problem. (Disregard the reward returned by the Maze environment, and compute the cost function you defined instead.)
    
  Let's define the state at time $k$ as the 2D coordinate of the robot $x_k = (x_{1_k}, x_{2_k})$, with $x_{1_k}, x_{2_k} \in \{0, 1, \dots, 9\}$. As the robot can only go up, down, right, or left, we can define the control input as an integer $u_k \in \{0, 1, 2, 3\}$. The state equation can be defined as:
  $$
  \begin{aligned}
    x_{k+1} &= f(k, x_k, u_k) \\
    &= x_k + c(u_k), \quad x_0 = (0, 0) \\
    c(u_k) &= 
    \begin{cases} 
    (0, 0)  & \quad \text{if blocked}\\
    (0, -1) & \quad \text{if } u_k = 0 \text{ and not blocked}\\
    (1, 0)  & \quad \text{if } u_k = 1 \text{ and not blocked}\\
    (0, 1)  & \quad \text{if } u_k = 2 \text{ and not blocked}\\
    (-1, 0) & \quad \text{if } u_k = 3 \text{ and not blocked},\\
  \end{cases}
  \end{aligned}
  $$
  where $c(u_k)$ is the coordinate mapping function.

  The cost function can be defined as:
  $$
  \begin{aligned}
    J(0, x_0, u) &= \mathbb{E} \left[\sum_{k=0}^{\infty} L(x_k, u_k) \mid x_0 \right] \\
    L(x_k, u_k) &= ||x_k - x_d||_2^2 = (x_{1_d} - x_{1_k})^2 + (x_{2_d} - x_{2_k})^2,
  \end{aligned}
  $$
  where $x_d = (9, 9)$ is the goal position.



- (b) Use value iteration to find a solution. Start with the initial value $V_0 = 0$. Plot the cost function at each step of the value iteration and discuss whether the value iteration converges.

- (c) Use policy iteration to find a solution. Begin with the initial policy $\pi_0 = 0$. Plot the cost function at each step of the policy iteration and discuss whether the policy iteration converges.

- (d) Now, repeat (b) and (c) with different initial values $V_0$ and $\pi_0$. Suppose we know the optimal path for the maze problem. Can you devise a way to embed this path into $V_0$ and $\pi_0$?