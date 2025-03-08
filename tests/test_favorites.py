from script.deploy import deploy_favorites

def test_starting_values():
    favorites_contract = deploy_favorites()

    assert favorites_contract.retrieve() == 42

def test_can_change_value():
    #Arrange
    favorites_contract = deploy_favorites()
    #Act
    favorites_contract.store(99)
    #Assert
    assert favorites_contract.retrieve() == 99

def test_can_add_person():
    #Arrange
    new_person = "Jay"
    favorite_number = 17
    favorites_contract = deploy_favorites()
    #Act
    favorites_contract.add_person(new_person, favorite_number)
    #Assert
    assert favorites_contract.list_of_people(0) == (favorite_number, new_person)