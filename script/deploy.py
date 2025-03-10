from src import favorites
from moccasin.boa_tools import VyperContract
from moccasin.config import get_active_network

def deploy_favorites() -> VyperContract:
    print("Deploying...")
    favorites_contract: VyperContract = favorites.deploy()
    starting_number: int = favorites_contract.retrieve()
    print(f"Starting number: {starting_number}")

    favorites_contract.store(42)
    new_number: int = favorites_contract.retrieve()
    print(f"New number: {new_number}")

    active_network = get_active_network()

    if active_network.has_explorer():
        result = active_network.moccasin_verify(favorites_contract)
        result.wait_for_verification()

    return favorites_contract


def moccasin_main():
    deploy_favorites()
    print("Deployed!")