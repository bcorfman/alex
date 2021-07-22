from game.level import Level
from game.search import complete_search, BlueprintSearchProblem
from game.util import ROOM_CHAR, LEVEL1, Stack


def test_expand_on_elevator():
    level = Level()
    level._load_layout(LEVEL1)
    level._add_border_to_layout()
    start_node = (12, 4)  # row, col
    problem = BlueprintSearchProblem(level.layout, start_node, ROOM_CHAR)
    expanded_nodes = problem.getSuccessors(start_node)
    assert len(expanded_nodes) == 2 and (13, 4) in expanded_nodes and (12, 5) in expanded_nodes


def test_depth_first_search_on_elevator():
    level = Level()
    level._load_layout(LEVEL1)
    level._add_border_to_layout()
    start_node = (13, 4)
    problem = BlueprintSearchProblem(level.layout, start_node, ROOM_CHAR)
    complete_search(problem, Stack())
    assert (12, 6) in problem.visited and (14, 11) in problem.visited
