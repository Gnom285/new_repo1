
from smartphone import Smartphone

catalog = [
    Smartphone(mark="Samsung", model="A33", number="+79123456789"),
    Smartphone(mark="Samsung", model="S22", number="+79234567891"),
    Smartphone(mark="Apple", model="13", number="+79345678912"),
    Smartphone(mark="Xiaomi", model="S2", number="+79456789123"),
    Smartphone(mark="Realme", model="15T", number="+79567891234"),
]

for Smartphone in catalog:
    print(f"{Smartphone.mark} - {Smartphone.model} - {Smartphone.number}")


