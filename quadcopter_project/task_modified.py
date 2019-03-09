import numpy as np
from physics_sim import PhysicsSim

class TaskModified():
    """Task (environment) that defines the goal and provides feedback to the agent."""
    """O novo objetivo é aterrissar o quadricóptero. Foi substituído a variável de posição
        de objetivo de 'target_pos' para target_pos_x_y' com apenas as posições de 'x' e 'y', sendo que a posição 'z' será sempre zero,
        representando a altura no ponto de pouso."""
    def __init__(self, init_pose=None, init_velocities=None, 
        init_angle_velocities=None, runtime=5., target_pos_x_y=None): # target_pos=None
        """Initialize a Task object.
        Params
        ======
            init_pose: initial position of the quadcopter in (x,y,z) dimensions and the Euler angles
            init_velocities: initial velocity of the quadcopter in (x,y,z) dimensions
            init_angle_velocities: initial radians/second for each of the three Euler angles
            runtime: time limit for each episode
            target_pos: target/goal (x,y,z) position for the agent
        """
        # Simulation
        self.sim = PhysicsSim(init_pose, init_velocities, init_angle_velocities, runtime) 
        self.action_repeat = 3

        self.state_size = self.action_repeat * 6
        self.action_low = 0
        self.action_high = 900
        self.action_size = 4

        # Goal
        # self.target_pos = target_pos if target_pos is not None else np.array([0., 0., 10.])
        """A altitude 'z' e os ângulos de Euler sempre serão 0. para o objetivo de aterrissagem, sendo necessário
            passar apenas os valores das coordenadas 'x' e 'y'."""
        self.target_pos = np.append(target_pos_x_y, 0.) if target_pos_x_y is not None else np.array([0., 0., 0.])

    def get_reward(self):
        """Uses current pose of sim to return reward."""
        """É importante pontuar a recompensa não só pela posição alvo, mas também pela estabilidade na aterrissagem.
            Por isso, os ângulos de Euler também entraram no cálculo dessa pontuação, sendo dividido por igual o peso
            da pontuação que era de 0.3"""
        # reward = 1.-.3*(abs(self.sim.pose[:3] - self.target_pos)).sum()
        reward = 1.-.3*(abs(self.sim.pose[:3] - self.target_pos)).sum()-.2*(abs(self.sim.pose[3:] - [0., 0., 0.])).sum()
        return reward

    def step(self, rotor_speeds):
        """Uses action to obtain next state, reward, done."""
        reward = 0
        pose_all = []
        # rotor_speeds_suavised = []
        for _ in range(self.action_repeat):
            done = self.sim.next_timestep(rotor_speeds) # update the sim pose and velocities
            """Repassa as velocidades de forma suavisada ao aproximar do alvo.
            for speed in rotor_speeds:
                rotor_speeds_suavised.append((speed/(self.init_height*1.25))+.2)
            done = self.sim.next_timestep(np.concatenate(rotor_speeds_suavised))"""
            reward += self.get_reward() 
            pose_all.append(self.sim.pose)
        next_state = np.concatenate(pose_all)
        return next_state, reward, done

    def reset(self):
        """Reset the sim to start a new episode."""
        self.sim.reset()
        state = np.concatenate([self.sim.pose] * self.action_repeat) 
        return state