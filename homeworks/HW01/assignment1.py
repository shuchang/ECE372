import gym
import gym_maze


def policy_iteration():
    pass


def value_iteration():
    pass

def main():
    env = gym.make("maze-random-10x10-v0")
    obs = env.reset()
    act = env.action_space.sample()
    obs = env.step(act)
    env.render()


if __name__ == "__main__":
    main()