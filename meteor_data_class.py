class MeteorDataEntry:
    def __init__(self, name, id, nametype, recclass, mass, fall, year, reclat, reclong, geolocation, state, countries):
        self.name = name
        self.id = id
        self.nametype = nametype
        self.recclass = recclass
        self.mass = self._to_float(mass)  # Mass converted to float or None
        self.fall = fall
        self.year = self._to_int(year)    # Year converted to int or None
        self.reclat = reclat
        self.reclong = reclong
        self.geolocation = geolocation
        self.state = state
        self.countries = countries

    def _to_float(self, value):
        """Helper: Convert value to float or return None if invalid."""
        try:
            return float(value) if value else None
        except ValueError:
            return None

    def _to_int(self, value):
        """Helper: Convert value to int or return None if invalid."""
        try:
            return int(value) if value else None
        except ValueError:
            return None

    def data_values_to_tab_sep_string(self):
        """Returns a tab-separated string of the meteor entry values."""
        return (f"(name={self.name}, id={self.id}, nametype={self.nametype}, "
                f"recclass={self.recclass}, mass={self.mass}, fall={self.fall}, "
                f"year={self.year}, reclat={self.reclat}, reclong={self.reclong}, "
                f"geolocation={self.geolocation}, state={self.state}, "
                f"countries={self.countries})")
