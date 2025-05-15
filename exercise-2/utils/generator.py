import random
import uuid


def generate_email(name: str):
    domains = ["pokemail.com", "trainerhub.com", "league.net"]
    clean = name.lower().replace(" ", ".")
    return f"{clean}@{random.choice(domains)}"


def generate_trainers(names, regions, starters, total=15000):
    trainers = []

    for i in range(total):
        name_obj = random.choice(names)
        full_name = f"{name_obj['first_name']} {name_obj['last_name']}"
        region = random.choice(regions)
        starter = random.choice(starters)
        age = random.randint(10, 99)
        email = generate_email(full_name)
        trainer_uuid = str(uuid.uuid4())

        trainers.append({
            "trainers_id": i + 1,
            "name": full_name,
            "region": region,
            "starter_pokemon": starter,
            "age": age,
            "email": email,
            "uuid": trainer_uuid
        })
    
    return trainers