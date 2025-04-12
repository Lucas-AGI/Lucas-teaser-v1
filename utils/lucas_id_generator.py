__version__ = "v0.9"

def get_lucas_id_version():
    return __version__

import random
import string

def generate_lucas_id():
    """
    Generates a unique symbolic ID in the format:
    LUCΔS-ΩXXXX-SFX where:
    - ΩXXXX is a 4-digit number prefixed with Greek Omega
    - SFX is a random symbolic suffix (e.g., AIΘ, ΣYB)
    """
    prefix = "LUCΔS"
    core = "Ω" + ''.join(random.choices(string.digits, k=4))
    suffix = random.choice(["AIΘ", "ΣYB", "NXΩ", "ΦRA", "ETH"])
    return f"{prefix}-{core}-{suffix}"

if __name__ == "__main__":
    print(f"LUCΔS ID Generator · Version {get_lucas_id_version()}")
