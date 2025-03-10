
def test_starting_values(favorites_contract):

    assert favorites_contract.retrieve() == 42

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