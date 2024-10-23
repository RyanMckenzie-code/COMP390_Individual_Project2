import PySimpleGUI as psg
from project1_main import read_meteor_data


filename = "meteorite_landings_data.txt"
meteor_entries = read_meteor_data(filename)

def format_meteor_data_for_gui(entry):
    return (
        f"{entry.name if entry.name is not None else ''}\t\t\t"
        f"{entry.id if entry.id is not None else ''}\t\t\t"
        f"{entry.nametype if entry.nametype is not None else ''}\t\t\t"
        f"{entry.recclass if entry.recclass is not None else ''}\t\t\t"
        f"{entry.mass if entry.mass is not None else ''}\t\t\t"
        f"{entry.fall if entry.fall is not None else ''}\t\t\t"
        f"{entry.year if entry.year is not None else ''}\t\t\t"
        f"{entry.reclat if entry.reclat is not None else ''}\t\t\t"
        f"{entry.reclong if entry.reclong is not None else ''}\t\t\t"
        f"{entry.geolocation if entry.geolocation is not None else ''}\t\t\t"
        f"{entry.state if entry.state is not None else ''}\t\t\t"
        f"{entry.countries if entry.countries is not None else ''}"
    )

def format_meteor_data_for_file(entry):
    """Formats the meteor entry data for file output with aligned columns."""
    # Use fixed widths that should accommodate most entries
    return (
        f"{str(entry.name)[:50]:<50}\t"  # Name, truncated to 50 characters
        f"{str(entry.id)[:20]:<20}\t"      # ID, truncated to 20 characters
        f"{str(entry.nametype)[:25]:<25}\t" # Nametype, truncated to 25 characters
        f"{str(entry.recclass)[:25]:<25}\t" # Recclass, truncated to 25 characters
        f"{str(entry.mass)[:20]:<20}\t"        # Mass, truncated to 20 characters
        f"{str(entry.fall)[:20]:<20}\t"        # Fall, truncated to 20 characters
        f"{str(entry.year)[:20]:<20}\t"        # Year, truncated to 20 characters
        f"{str(entry.reclat)[:20]:<20}\t"      # Reclat, truncated to 20 characters
        f"{str(entry.reclong)[:20]:<20}\t"     # Reclong, truncated to 20 characters
        f"{str(entry.geolocation)[:30]:<30}\t" # Geolocation, truncated to 30 characters
        f"{str(entry.state)[:20]:<20}\t"      # State, truncated to 20 characters
        f"{str(entry.countries)[:30]:<30}\n"   # Countries, truncated to 30 characters
    )

def filter_meteors_by_mass(meteor_entries, min_mass):
    """Filters meteor entries by mass greater than the specified minimum mass."""
    return [entry for entry in meteor_entries if entry.mass and entry.mass > min_mass]

def filter_meteors_by_year(meteor_entries, min_year):
    """Filters meteor entries that fell in the year greater than or equal to the specified minimum year."""
    return [entry for entry in meteor_entries if entry.year and entry.year > min_year]


layout = [
    [psg.Text('Minimum Mass Limit (Grams Exclusive): >'), psg.InputText(key='min_mass_param')],
    [psg.Text('Minum Year Limit (0-2012 Exclusive): >'), psg.InputText(key='min_year_param')],
    [psg.Button('Apply Filter'), psg.Button('EXIT')],
    [psg.Text('Mass Filter Results:')],
    [psg.Multiline(size=(70, 10), key='mass_results', disabled=True, horizontal_scroll=True)],
    [psg.Text('Year Filter Results:')],
    [psg.Multiline(size=(70, 10), key='year_results', disabled=True, horizontal_scroll=True)],
]


window = psg.Window('Meteorite Data Filtering', layout)

def write_to_file(filename, data):
    """Writes formatted meteor data to a text file with aligned columns."""
    with open(filename, 'w') as file:
        # Write the header with aligned columns
        header = (
            f"{'Name':<50}\t"
            f"{'ID':<20}\t"
            f"{'Nametype':<25}\t"
            f"{'Recclass':<25}\t"
            f"{'Mass':<20}\t"
            f"{'Fall':<20}\t"
            f"{'Year':<20}\t"
            f"{'Reclat':<20}\t"
            f"{'Reclong':<20}\t"
            f"{'Geolocation':<30}\t"
            f"{'State':<20}\t"
            f"{'Countries':<30}\n"
        )
        file.write(header)
        file.write('-' * 350 + '\n')
        for entry in data:
            file.write(format_meteor_data_for_file(entry))

while True:
    event, values = window.read()

    # Exit the program if user closes the window or presses EXIT
    if event == psg.WIN_CLOSED or event == 'EXIT':
        break


    if event == 'Apply Filter':
        window['mass_results'].update('')
        window['year_results'].update('')

        # Get input values
        try:
            min_mass_param = float(values['min_mass_param'])
            min_year_param = int(values['min_year_param'])
        except ValueError:
            psg.popup_error("Please enter valid numeric values for mass and year.")
            continue


        mass_filtered = filter_meteors_by_mass(meteor_entries, min_mass_param)
        year_filtered = filter_meteors_by_year(meteor_entries, min_year_param)

        # Update the GUI and write to files
        if mass_filtered:
            formatted_mass_results = '\n'.join([format_meteor_data_for_gui(entry) for entry in mass_filtered])
            window['mass_results'].update(
                f"{'Name':<30}\t\t\t"
                f"{'ID':<10}\t\t\t"
                f"{'Nametype':<15}\t\t\t"
                f"{'Recclass':<15}\t\t\t"
                f"{'Mass':<10}\t\t\t"
                f"{'Fall':<10}\t\t\t"
                f"{'Year':<10}\t\t\t"
                f"{'Reclat':<10}\t\t\t"
                f"{'Reclong':<10}\t\t\t"
                f"{'Geolocation':<20}\t\t\t"
                f"{'State':<10}\t\t\t"
                f"{'Countries':<15}\n"
                f"{'-' * 600}\n{formatted_mass_results}"
            )
            write_to_file('mass_filtered_data.txt', mass_filtered)
        else:
            psg.popup("No entries found for the mass filter.")

        if year_filtered:
            formatted_year_results = '\n'.join([format_meteor_data_for_gui(entry) for entry in year_filtered])
            window['year_results'].update(
                f"{'Name':<30}\t\t\t"
                f"{'ID':<10}\t\t\t"
                f"{'Nametype':<15}\t\t\t"
                f"{'Recclass':<15}\t\t\t"
                f"{'Mass':<10}\t\t\t"
                f"{'Fall':<10}\t\t\t"
                f"{'Year':<10}\t\t\t"
                f"{'Reclat':<10}\t\t\t"
                f"{'Reclong':<10}\t\t\t"
                f"{'Geolocation':<20}\t\t\t"
                f"{'State':<10}\t\t\t"
                f"{'Countries':<15}\n"
                f"{'-' * 600}\n{formatted_year_results}"
            )
            write_to_file('year_filtered_data.txt', year_filtered)
        else:
            psg.popup("No entries found for the year filter.")

# Close the window
window.close()
