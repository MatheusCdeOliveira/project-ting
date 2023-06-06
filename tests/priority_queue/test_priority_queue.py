from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    priority = PriorityQueue()

    mocks = [
              {"qtd_linhas": 1},
              {"qtd_linhas": 2},
              {"qtd_linhas": 6},
              {"qtd_linhas": 3}
            ]
    
    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority.search(100)

    priority.enqueue(mocks[0])
    priority.enqueue(mocks[1])
    priority.enqueue(mocks[2])
    priority.enqueue(mocks[3])

    assert len(priority) == 4
    assert priority.search(0) == mocks[0]
    assert priority.search(1) == mocks[1]
    assert priority.search(2) == mocks[3]
    assert priority.search(3) == mocks[2]

    priority.dequeue()
    assert priority.search(0) == mocks[1]

    priority.dequeue()
    assert priority.search(0) == mocks[3]

    priority.dequeue()
    assert priority.search(0) == mocks[2]


