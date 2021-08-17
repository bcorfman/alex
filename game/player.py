from dataclasses import dataclass, field
from concurrent.futures import ProcessPoolExecutor
from .chartypes import PLAYER_AVATAR
from .agent import Agent
from .util import Loc, Node, Queue
from .search import BlueprintSearchProblem, graph_search


@dataclass
class Player(Agent):
    actions: Queue = field(default_factory=Queue)
    avatar: str = PLAYER_AVATAR

    async def moveTo(self, pos: Loc):
        # noinspection PyUnresolvedReferences
        problem = BlueprintSearchProblem(self.parent.layout, Node(self.location), Node(pos))
        with ProcessPoolExecutor(max_workers=1) as executor:
            future = executor.submit(graph_search, problem, Queue())
        completed = future.result()
        self.actions = Queue(completed.actions) if completed else Queue()

    def update(self):
        self.numGameTicks += 1
        if self.numGameTicks > self.game_ticks_before_each_move:
            if not self.actions.isEmpty():
                self.priorLocation = self.location
                self.location = self.actions.pop()
            self.numGameTicks = 0
