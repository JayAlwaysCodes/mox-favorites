
def test_starting_values(favorites_contract):

    assert favorites_contract.retrieve() == 77

def test_can_change_value(favorites_contract):
    #Arrange
    #Act
    favorites_contract.store(99)
    #Assert
    assert favorites_contract.retrieve() == 99

def test_can_add_person(favorites_contract):
    #Arrange
    new_person = "Jay"
    favorite_number = 17
    #Act
    favorites_contract.add_person(new_person, favorite_number)
    #Assert
    assert favorites_contract.list_of_people(0) == (favorite_number, new_person)

def test_initial_bool_value(favorites_contract):
    # Test that `my_bool` is initialized to False
    assert favorites_contract.get_bool() == False

def test_set_bool(favorites_contract):
    # Call `set_bool()` to update `my_bool` to True
    favorites_contract.set_bool()

    # Verify that `my_bool` is now True
    assert favorites_contract.get_bool() == True

def test_set_bool_twice(favorites_contract):
    # Call `set_bool()` multiple times (should remain True)
    favorites_contract.set_bool()
    favorites_contract.set_bool()

    # Verify that `my_bool` is still True
    assert favorites_contract.get_bool() == True