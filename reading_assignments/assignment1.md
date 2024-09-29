# Reaching the Limit in Autonomous Racing: Optimal Control versus Reinforcement Learning

<!-- 1. problem formulation
2. methods to solve the problem
3. why the proposed methods are optimal -->


---
## 1: Introduction
### 1.1 Optimal Control vs Reinforcement Learning

- model-based optimal control: relies on the explicit use of an accurate mathematical model within an optimization framework to find an optimal control law for a given dynamical system.
- model-free reinforcement learning: trains an agent to maximize a reward signal in an environment.

- Question: which is better (optimal)?

---

### 1.2 Autonomous Drone Racing
- Definition: fly a quadrotor through a sequence of gates in a given order in minimum time
- why this task?
  - For maximal performance, this task requires pushing the aircraft to its physical limits of speed and acceleration.
  - tolerance for error is low

---

### 1.3 Problem Formulation
- Autonomous Drone Racing is formulated as a constrained optimization problem:
$$
\min t_N
$$


---

## 2: Proposed Methods
### 2.1 Optimal Control Methods
- Planning + Control (MPC)

- Two planning methods:
  - Trajectory Tracking
  - Contouring Control

---

#### 2.1.1 Trajectory Tracking


---

#### 2.1.2 Contouring Control

---

#### 2.1.3 Model Predictive Control

---

### 2.2 Reinforcement Learning Method

---

#### 2.2.1 Gate Progress

---

#### 2.2.2 Policy Gradient

---

## 3: Experiments
Two experiment settings

---

### 3.1 Optimization Method Hypothesis


---

### 3.2 Optimization Objective Hypothesis


## 4. Results

---

### 4.1 Main Results

---

### 4.2 Optimization Method

---

### 4.3 Optimization Objective

---

### 4.4 Visualizing Value Functions

---

## 5. Conclusion
