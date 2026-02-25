# from farm import *

class StoreHouse:

    def __init__(self):
        self.crops = {}

    def __str__(self):
        fin_str = ''
        if not self.crops:
            return 'Empty storehouse'
        for name, amount in self.crops.items():

            if name == list(self.crops.keys())[-1]:
                fin_str += f"{amount} {name}{'s' if amount != 1 else ''}"
            else:
                fin_str += f"{amount} {name}{'s' if amount != 1 else ''},"

        return 'Storehouse has ' + fin_str


class Vehicle:
    def __init__(self):
        self.fuel_capacity = 50
        self.fuel = 50
        self.fuel_consumption = 0.1

    def ride(self, dist):
        if dist > self.fuel / self.fuel_consumption:
            raise ValueError ('Too far...')
        else:
            self.fuel -= dist * self.fuel_consumption


class Field:

    def __init__(self, crop_type, area):
        self.crop_type = crop_type
        self.area = area
        self.crops = area


    def __str__(self):
        return f"{self.area}ha field with {self.crops} corns on it"

class HarvestMixin:
    pass

class Tractor(Vehicle, HarvestMixin):
    fuel_capacity = 300
    __crop_harvest = 0
    __type_crop = ""

    def __init__(self, harvest_capacity=40):
        super().__init__()
        self.fuel_capacity = Tractor.fuel_capacity
        self.harvest_capacity = harvest_capacity
        self.fuel = Tractor.fuel_capacity


    def harvest(self, harvest):
        fuel = max(0, self.fuel - harvest.area * 10)
        crops = max(0, self.harvest_capacity - harvest.area)

        if fuel == 0:
            harvested = self.fuel // 10
            print(self.harvested)
        elif crops == 0:
            
        else:
            harvested = harvest.area

        if harvest.crop_type != self.__type_crop and self.__type_crop:
            raise ValueError ('Cannot harvest two crops at once')

        self.__type_crop = harvest.crop_type
        self.harvested = [harvested + self.__crop_harvest, harvest.crop_type]

        self.__crop_harvest += harvested
        self.fuel = fuel
        harvest.crops -= harvested

    def refill(self, amount=0):
        if amount:
            self.fuel = min(self.fuel + amount, self.fuel_capacity)
        else:
            self.fuel = self.fuel_capacity

    def unload_to(self, place):

        self.harvested = [0, None]
        place.crops.setdefault(self.__type_crop, 0)
        place.crops[self.__type_crop] += self.__crop_harvest
        self.__crop_harvest = 0
        self.__type_crop = None






storehouse = StoreHouse()
assert str(storehouse) == 'Empty storehouse'
assert storehouse.crops == {}

# У фермера є власне авто, на якому він добирається до ферми
car = Vehicle()
assert car.fuel_capacity == 50  # За замовчуванням бак авто 50л
assert car.fuel == 50  # На початку всі авто заправлені "до повного"
assert car.fuel_consumption == 0.1  # Розхід палива - 10л/100км

# Планувати заїхати задалеко не вдасться
try:
    car.ride(501)
    assert False, "Should raise error"
except ValueError as e:
    assert str(e) == 'Too far...'

assert car.fuel == 50  # Ще нікуди не поїхали

car.ride(400)
assert car.fuel == 10  # після 400км залишилось ще 10л


# Добравшись на ферму, фермер оглядає поля
field1 = Field('corn', 100)
assert str(field1) == '100ha field with 100 corns on it'

assert field1.crop_type == 'corn'
assert field1.area == 100  # 100 гектарів
assert field1.crops == 100  # На кожному гектарі росте одна одиниця урожаю


# Руками збирати урожай з цілого поля - пропаща справа, нам на допомогу прийде трактор
tractor = Tractor(harvest_capacity=40)
assert isinstance(tractor, Vehicle)
assert isinstance(tractor, HarvestMixin)
assert tractor.harvest_capacity == 40  # Трактор вміщує 40 одиниць урожаю
assert tractor.fuel_capacity == 300  # Оце так бак
assert Tractor.fuel_capacity == 300

small_field = Field('corn', 1)
tractor.harvest(small_field)
assert tractor.harvested == [1, 'corn']
assert tractor.fuel == 290, tractor.fuel  # На збір урожаю з 1 гектара йде 10л пального

assert small_field.crops == 0

# На малому полі все зібрали, приступаємо до більшого
tractor.harvest(field1)
print(tractor.harvested)
assert tractor.harvested == [30, 'corn']  # Трактор зібрав лише 30 рослин
assert tractor.fuel == 0  # Бо закінчилось пальне
print(field1.crops)
assert field1.crops == 71  # На другому полі зібрали 29 рослин (і ще одна була зібрана на маленькому)
assert str(field1) == '100ha field with 71 corns on it'

tractor.refill(10)  # долили з каністри 10л
assert tractor.fuel == 10

tractor.refill()  # до повного
assert tractor.fuel == 300

# Пора збирати моркву
field2 = Field('carrot', 50)
try:
    tractor.harvest(field2)
    assert False, "Should raise error"
except ValueError as e:
    assert str(e) == 'Cannot harvest two crops at once'

# Потрібно вивантажити кукурудзу, перш ніж збирати моркву
tractor.unload_to(storehouse)
assert tractor.harvested == [0, None]
assert str(storehouse) == 'Storehouse has 30 corns', str(storehouse)
assert storehouse.crops == {'corn': 30}

tractor.harvest(field2)
assert tractor.harvested == [30, 'carrot']  # Трактор зібрав лише 30 рослин
assert tractor.fuel == 0  # Бо закінчилось пальне
assert field2.crops == 20

# Дозаправка і продовжуємо
tractor.refill()
tractor.harvest(field2)
# Хоча на полі ще є урожай і паливо в баці - ми зупинились, бо трактор переповнений
print(field2.crops)
assert field2.crops == 10
assert tractor.fuel == 200
assert tractor.harvested == [40, 'carrot']

tractor.unload_to(storehouse)
assert tractor.harvested == [0, None]
assert str(storehouse) == 'Storehouse has 30 corns, 40 carrots', str(storehouse)
assert storehouse.crops == {'corn': 30, 'carrot': 40}

# Пустим трактором повністю дозбируємо урожай
tractor.harvest(field2)
assert field2.crops == 0
assert tractor.fuel == 100
assert tractor.harvested == [10, 'carrot']

tractor.unload_to(storehouse)
assert str(storehouse) == 'Storehouse has 30 corns, 50 carrots', str(storehouse)

# Аж раптом буря знищила комору з усіма запасами
del storehouse.crops
assert storehouse.crops == {}


tractor.refill()
try:
    tractor.ride(3001)
    assert False
except FuelError:
    pass

# Щоб збільшити тривалість роботи, виробник покращив характеристики трактора
Tractor.upgrade_specs(fuel_capacity=400)

new_tractor = Tractor(harvest_capacity=40)
new_tractor.ride(3001)

assert Tractor.fuel_capacity == 400
assert Tractor(harvest_capacity=40).fuel_capacity == 400
assert tractor.fuel_capacity == 300  # На існуючі трактори зміна не поширюється
