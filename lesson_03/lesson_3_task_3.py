
from address import Address
from mailing import Mailing

to_address = Address (660115, "Иркутск", "Ленина", 45, 33 )
from_address = Address (660115, "Иркутск", "Желябова", 10, 20)
track = "Отправление"
cost = 2800

mailing = Mailing (to_address, from_address, cost, track)

print(mailing)