from src import favorites

def deploy():
    print("Deploying...")
    favorites_contract = favorites.deploy()
    starting_number = favorites_contract.retrieve()
    print(f"Starting number: {starting_number}")


def moccasin_main():
    deploy()
    print("Deployed!")