import pytest
from script.deploy import deploy_favorites

@pytest.fixture(scope="session")
def favorites_contract():
    favorites_contract = deploy_favorites()
    return favorites_contract