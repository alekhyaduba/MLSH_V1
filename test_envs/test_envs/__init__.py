import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='MovementBandits-v0',
    entry_point='test_envs.envs:MovementBandits',
    # timestep_limit=50,
)

register(
    id='KeyDoor-v0',
    entry_point='test_envs.envs:KeyDoor',
    # timestep_limit=100,
)

register(
    id='Allwalk-v0',
    entry_point='test_envs.envs:Allwalk',
    # timestep_limit=50,
)

register(
    id='Fourrooms-v0',
    entry_point='test_envs.envs:Fourrooms',
    # timestep_limit=100,
    # reward_threshold = 1,
)


register(
    id='HalfCheetahForwardBackward-v2',
    entry_point='test_envs.envs:HalfCheetahForwardBackwardEnv',
    max_episode_steps=100,
    # timestep_limit=1000,
)

register(
    id='Particles2D-v1',
    entry_point='test_envs.envs:Particles2DEnv',
    max_episode_steps=100
)

register(
    id='AntDirection-v1',
    entry_point='test_envs.envs:AntDirectionEnv',
    max_episode_steps=100
)