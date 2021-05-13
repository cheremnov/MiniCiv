import random
from src.unit import Unit


class Country_stat:

    def __init__(self, color):
        self.color = color
        self.resources = 100
        self.units = []
        self.cells = []

    def set_capital(self, capital_coords, vis_map):
        assert(vis_map.in_bounds(capital_coords[0], capital_coords[1]))
        self.capital = capital_coords

    def gen_unit_loc(self, units_num, spawn_area_size, vis_map):
        ''' Function generates initial unit locations in the hex map
        Major assumptions:
        1) Every unit belongs to the country
        2) All units spawn in the square over the country capital
        3) If the spawn location is unavailable, they spawn in the capital
        This function requires:
        1) The nation must have the capital
        '''
        possible_spawns = set()
        for x in range(self.capital[0] - spawn_area_size,
                       self.capital[0] + spawn_area_size):
            for y in range(self.capital[1] - spawn_area_size,
                           self.capital[1] + spawn_area_size):
                possible_spawns.add((x, y))
        for unit_idx in range(units_num):
            if len(possible_spawns) == 0:
                spawn_loc = self.capital
            else:
                spawn_loc = random.sample(possible_spawns, 1)[0]
                possible_spawns.remove(spawn_loc)
                if not vis_map.in_bounds(spawn_loc[0], spawn_loc[1]):
                    spawn_loc = self.capital

            unit = Unit()
            unit.set_cell((spawn_loc[0], spawn_loc[1]))
            self.add_unit(unit)

    def add_unit(self, unit):
        self.units.append(unit)

    def remove_unit(self, unit):
        self.units.remove(unit)

    def get_units(self):
        return self.units

    def clear_units(self):
        self.units = []

    def add_cell(self, cell):
        self.cells.append(cell)

    def remove_cell(self, cell):
        self.units.remove(cell)

    def get_cells(self):
        return self.cells

    def clear_cells(self):
        self.cells = []

    def get_color(self):
        return self.color

    def get_resources(self):
        return self.resources

    def set_resources(self, resources):
        self.resources = resources

    def change_resources(self, add):
        resources = self.resources + add

    def get_income(self):
        income = 0
        for unit in self.units:
            income = income + unit.get_income()
        return income
