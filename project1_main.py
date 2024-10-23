from meteor_data_class import MeteorDataEntry


def read_meteor_data(filename):
    """Reads meteor data from the given file and returns the entries."""
    meteor_entries = []

    with open(filename, 'r') as file:
        # Skip the header line
        header = file.readline()

        for line in file:
            data_fields = line.strip().split('\t')
            data_fields = (data_fields + [''] * 12)[:12]

            individual_entry = MeteorDataEntry(
                data_fields[0], data_fields[1], data_fields[2], data_fields[3], data_fields[4],
                data_fields[5], data_fields[6], data_fields[7], data_fields[8], data_fields[9],
                data_fields[10], data_fields[11]
            )
            meteor_entries.append(individual_entry)

    return meteor_entries


def filter_meteors_by_mass(meteor_entries):
    """Filters meteor entries by mass greater than 2,900,000 grams."""
    MeteorsWithMassGreater = []
    massTableNumber = 0

    for entry in meteor_entries:
        if entry.mass and int(entry.mass) > 2900000:
            massTableNumber += 1
            MeteorsWithMassGreater.append([massTableNumber, entry.name, entry.mass])

    return MeteorsWithMassGreater


def filter_meteors_by_year(meteor_entries):
    """Filters meteor entries that fell in the year 2013 or after."""
    meteorsWithYearGreater = []
    yearTableNumber = 0

    for entry in meteor_entries:
        if entry.year and int(entry.year) >= 2013:
            yearTableNumber += 1
            meteorsWithYearGreater.append([yearTableNumber, entry.name, entry.year])

    return meteorsWithYearGreater


def print_mass_table(mass_data):
    """Prints the mass table."""
    print(f"{'No.'.ljust(5)} {'Name'.ljust(30)} {'Mass (g)'.rjust(10)}")
    print("=" * 50)
    for entry in mass_data:
        print(f"{str(entry[0]).ljust(5)} {entry[1].ljust(30)} {str(entry[2]).rjust(10)}")


def print_year_table(year_data):
    """Prints the year table."""
    print(f"{'No.'.ljust(5)} {'Name'.ljust(30)} {'Year'.rjust(6)}")
    print("=" * 50)
    for entry in year_data:
        print(f"{str(entry[0]).ljust(5)} {entry[1].ljust(30)} {str(entry[2]).rjust(6)}")


def main():
    """Main function to execute the meteor filtering program."""
    filename = "meteorite_landings_data.txt"
    meteor_entries = read_meteor_data(filename)

    MeteorsWithMassGreater = filter_meteors_by_mass(meteor_entries)
    MeteorsWithYearGreater = filter_meteors_by_year(meteor_entries)

    print("\nTable 1: Meteorites Weighing More Than 2,900,000 Grams")
    print_mass_table(MeteorsWithMassGreater)

    print("\nTable 2: Meteorites That Fell in the Year 2013 or After")
    print_year_table(MeteorsWithYearGreater)


