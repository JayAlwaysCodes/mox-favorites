from src import favorites
from moccasin.boa_tools import VyperContract
from moccasin.config import get_active_network


def deploy_favorites() -> VyperContract:
    active_network = get_active_network()
    print("Currently on network: ", active_network.name)

    favorites_contract: VyperContract = favorites.deploy()
    print("Starting favorite number: ", favorites_contract.retrieve())
    favorites_contract.store(77)
    print("Ending favorite number: ", favorites_contract.retrieve())

    if active_network.has_explorer():
        print("Verifying contract on explorer...")
        result = active_network.moccasin_verify(favorites_contract)
        result.wait_for_verification()
    return favorites_contract


def moccasin_main() -> VyperContract:
    return deploy_favorites()