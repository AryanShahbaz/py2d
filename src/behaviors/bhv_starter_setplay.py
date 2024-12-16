from typing import TYPE_CHECKING
from src.interfaces.IAgent import IAgent
from src.utils.convertor import Convertor
from pyrusgeom.geom_2d import *
from pyrusgeom.soccer_math import *
from service_pb2 import *
from src.interfaces.IBehavior import IBehavior

if TYPE_CHECKING:
    from src.sample_player_agent import SamplePlayerAgent

class BhvStarterSetPlay(IBehavior):
    def __init__(self):
        pass
    
    def execute(self, agent: "SamplePlayerAgent"):
        agent.logger.debug("BhvSetPlay.execute")
        raise NotImplementedError("BhvStarterSetPlay.execute not implemented")