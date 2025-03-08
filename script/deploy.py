from src import favorites

def deploy_favorites():
    print("Deploying...")
    favorites_contract = favorites.deploy()
    starting_number = favorites_contract.retrieve()
    print(f"Starting number: {starting_number}")

    favorites_contract.store(42)
    new_number = favorites_contract.retrieve()
    print(f"New number: {new_number}")

    return favorites_contract


def moccasin_main():
    deploy_favorites()
    print("Deployed!")