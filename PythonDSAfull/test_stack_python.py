
from PythonStack import Stack,Stack2,Stack3
import pytest
new_stack = Stack()
stack_2 = Stack2(3)

newStack = Stack3()

@pytest.mark.stack
def test_stack():
    assert new_stack.isEmpty()
    assert new_stack.pushElement(34)
    assert new_stack.pushElement(45)
    assert new_stack.pushElement(56)
    assert new_stack.pushElement(23)
    # assert new_stack.popItem()
    assert new_stack.popItem()
    assert new_stack.peekElement()


@pytest.mark.stack2
def test_stack2():
    assert stack_2.pushElement(78)
    assert stack_2.pushElement(5)
    assert stack_2.pushElement(2)

    assert stack_2.isFull()

@pytest.mark.stack3
def test_linked_list_stack():
    assert newStack.isEmpty()
    assert newStack.pushValue(78)
    assert newStack.pushValue(70)
    assert newStack.pushValue(98)
    assert newStack.pushValue(10)

