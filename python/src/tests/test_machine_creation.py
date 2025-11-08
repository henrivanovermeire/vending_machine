from ..src.vending_machine import VendingMachine

def test_create_empty_machine():
	machine = VendingMachine()
	assert machine is not None

def test_create_machine_from_state():
    machine = VendingMachine([1,2,3,4])
    assert machine is not None
