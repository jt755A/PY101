# ask user for length of room in m
# ask user for width of room in meters
# calculate area of room in m: w x l
# convert to sq feet (* 10.7639) and save value as result
# print area in sq feet and result in sq meters

# START
# GET length of room in m
# GET width of room in m
# SET area = width x length
# SET area_ft = (READ area) * 10.7639
# Round area_ft, 2 decimal places
# PRINT area, result
# END

# length_meters = float(input("Please enter the length of the room in meters: "))
# width_meters = float(input("Please enter the width of the room in meters: "))

# area_meters = length_meters * width_meters
# area_feet = round(area_meters * 10.7639, 2)
# print(f'The area in square meters is: {area_meters}. '
#       f'The area in square feet is: {area_feet}')

# Bonus: Modify the program to let the user specify the measurement type
# (meters or feet). Compute the area accordingly and print it and its
# conversion in parentheses.

# GET measurement type: meters, or feet
# GET length of room
# GET width of room
# SET area_chosen_type = READ(length) * READ(width)

# IF READ(measurement type) == meters
    # SET conversion = feet
# ELIF READ(measurement type) == feet
    # SET conversion = meters

# if READ(measurment type) == meters
    # SET area_conversion = READ (area_chosen_type) * 10.7639
# elif READ(measurment type) == feet
    # SET area_conversion = READ (area_chosen_type) / 10.7639
    
# PRINT 'The area of the room is READ(are_chosen_type) GET(measurement type)'
#       '(GET(area_conversion) GET(conversion).')
    
measurement_type = input(f'Please specify measurment type: 1) meters 2) feet\n')
while measurement_type not in ['1', '2']:
    print("That's not a valid choice. Choose either '1' or '2'.")
    measurement_type = input()


length = float(input("Please enter the length of the room: "))
width = float(input("Please enter the width of the room: "))
area_chosen_type = length * width

if measurement_type == '1':
    unit = 'square meters'
    area_conversion = area_chosen_type * 10.7369
    conversion_unit = 'square feet'
elif measurement_type == '2':
    unit = 'square feet'
    area_conversion = area_chosen_type / 10.7369
    conversion_unit = 'square meters'

    
print(f'The area of the room is {area_chosen_type:.2f} {unit} ' \
f'({area_conversion:.2f} {conversion_unit})')
