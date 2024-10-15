import PySimpleGUI as psg
from project1_main import read_meteor_data

# Read meteor data from the specified file
filename = "meteorite_landings_data.txt"
meteor_entries = read_meteor_data(filename)

# Layout for the GUI
layout = [
    [psg.Text('Enter minimum mass (grams):'), psg.InputText(key='min_mass_param')],
    [psg.Text('Enter minimum year:'), psg.InputText(key='min_year_param')],
    [psg.Button('Apply Filter'), psg.Button('EXIT')],
    [psg.Text('Mass Filter Results:')],
    [psg.Multiline(size=(100, 20), key='mass_results')],
    [psg.Text('Year Filter Results:')],
    [psg.Multiline(size=(100, 20), key='year_results')]
]

# Create the window
window = psg.Window('Meteorite Data Filtering', layout)

def filter_data_by_mass_year(min_mass, min_year):
    greater_mass_meteor = []
    recent_meteor = []

    # Iterate through the meteor entries and apply filters
    # Filter meteor entries based on mass and year
    for meteor in meteor_entries:
        # Ensure mass is a valid number
        if meteor.mass and meteor.mass.isdigit() and int(meteor.mass) >= min_mass:
            greater_mass_meteor.append(meteor)
        # Ensure year is a valid number
        if meteor.year and meteor.year.isdigit() and int(meteor.year) >= min_year:
            recent_meteor.append(meteor)

    return greater_mass_meteor, recent_meteor

# Writing filtered data to files
def write_to_file(filename, data_list):
    with open(filename, 'w') as file:
        for entry in data_list:
            file.write(entry.data_values_to_tab_sep_string() + '\n')

while True:
    event, values = window.read()

    # Exit the program if user closes window or presses EXIT
    if event == psg.WIN_CLOSED or event == 'EXIT':
        break

    # Apply filter when 'Apply Filter' button is pressed
    if event == 'Apply Filter':
        # Clear the results first
        window['mass_results'].update('')
        window['year_results'].update('')

        # Get values from input boxes
        try:
            min_mass_param = float(values['min_mass_param'])  # Convert to float for mass
            min_year_param = int(values['min_year_param'])    # Ensure year is int
        except ValueError:
            psg.popup_error("Please enter valid numeric values for mass and year.")
            continue  # Skip filtering if invalid input

        print(f'Min Mass: {min_mass_param}, Min Year: {min_year_param}')

        # Call the filtering function
        mass_filtered, year_filtered = filter_data_by_mass_year(min_mass_param, min_year_param)

        # Update the GUI with results and write to files
        if mass_filtered:
            window['mass_results'].update('\n'.join([entry.data_values_to_tab_sep_string() for entry in mass_filtered]))
            write_to_file('mass_filtered_data.txt', mass_filtered)
        else:
            print('No entries found for mass filter.')

        if year_filtered:
            window['year_results'].update('\n'.join([entry.data_values_to_tab_sep_string() for entry in year_filtered]))
            write_to_file('year_filtered_data.txt', year_filtered)
        else:
            print('No entries found for year filter.')

# Close the window
window.close()
