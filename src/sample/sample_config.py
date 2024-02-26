import os
from dataclasses import dataclass

@dataclass
class TrainConfig:
    epoch : int = 10
    lr : float = 1e-3
    exp_num : int = 5

def train(config:TrainConfig) -> None:
    epoch = TrainConfig.epoch
    lr = TrainConfig.lr
    warm_up = TrainConfig.warm_up
    exp_dir = os.path.join("./", config.exp_num)