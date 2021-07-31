from game.level import Level, Perimeter
from game.util import node_ordering, ROOM_CHAR, LEVEL1
from game.search import exhaustive_search, HallwayConstructionProblem, Node


def test_load_layout():
    level = Level()
    level._load_layout(LEVEL1)
    assert (level.layout[1][30] == 'C')


def test_load_layout_and_add_border():
    level = Level()
    level._load_layout(LEVEL1)
    level._add_border_to_layout()
    assert (level.layout[2][31] == 'C')


def test_location_ordering():
    level = Level()
    level._load_layout(LEVEL1)
    level._add_border_to_layout()
    start_loc = (13, 4)
    problem = HallwayConstructionProblem(level.layout, Node(start_loc), ROOM_CHAR)
    exhaustive_search(problem)
    assert ((12, 4) == min(problem.visited, key=node_ordering))
    assert ((14, 11) == max(problem.visited, key=node_ordering))


def test_find_room_name():
    level = Level()
    level._load_layout(LEVEL1)
    level._add_border_to_layout()
    p = Perimeter(Node([1, 17]), Node([3, 50]))
    assert p.find_room_name(level.layout) == 'CARGO'


def test_find_elevators():
    level = Level()
    level._load_layout(LEVEL1)
    level._add_border_to_layout()
    level._find_elevators()
    elevator1, elevator2 = level.elevators[0], level.elevators[1]
    assert (elevator1.name == 'ELEVATOR' and elevator1.perimeter.top_left == Node([1, 62]) and
            elevator1.perimeter.bottom_right == Node([3, 69]))
    assert (elevator2.name == 'ELEVATOR' and elevator2.perimeter.top_left == Node([12, 4]) and
            elevator2.perimeter.bottom_right == Node([14, 11]))


def test_initialize_level():
    level = Level(LEVEL1)
    assert len(level.rooms) == 3 and len(level.elevators) == 2


def test_hallways():
    level = Level(LEVEL1)
    assert len(level.hallways) == 17
    assert frozenset([(2, i) for i in range(51, 57)]) in level.hallways
    assert frozenset([(2, 57)]) in level.hallways
    assert frozenset([(2, i) for i in range(58, 62)])
    assert frozenset([(i, 57) for i in range(3, 10)]) in level.hallways
    assert frozenset([(10, 57)]) in level.hallways
    assert frozenset([(10, i) for i in range(52, 57)]) in level.hallways
    assert frozenset([(13, i) for i in range(12, 16)])
    assert frozenset([(13, 16)]) in level.hallways
    assert frozenset([(i, 16) for i in range(11, 13)]) in level.hallways
    assert frozenset([(10, 16)]) in level.hallways
    assert frozenset([(i, 16) for i in range(8, 10)]) in level.hallways
    assert frozenset([(10, i) for i in range(17, 24)]) in level.hallways
    assert frozenset([(10, i) for i in range(5, 16)]) in level.hallways
    assert frozenset([(10, 4)]) in level.hallways
    assert frozenset([(i, 4) for i in range(3, 10)]) in level.hallways
    assert frozenset([(2, 4)]) in level.hallways
    assert frozenset([(2, i) for i in range(5, 17)]) in level.hallways
