import phonenumbers
from phonenumbers import carrier, timezone, geocoder
print(""" 
░█████╗░░██████╗██╗░░░██╗░█████╗░██╗░░░░░██████╗░░█████╗░
██╔══██╗██╔════╝██║░░░██║██╔══██╗██║░░░░░██╔══██╗██╔══██╗
██║░░██║╚█████╗░╚██╗░██╔╝███████║██║░░░░░██║░░██║██║░░██║
██║░░██║░╚═══██╗░╚████╔╝░██╔══██║██║░░░░░██║░░██║██║░░██║
╚█████╔╝██████╔╝░░╚██╔╝░░██║░░██║███████╗██████╔╝╚█████╔╝
░╚════╝░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═════╝░░╚════╝░ """)
phn = input("Enter a mobile Number with Country Code: ")
my_number = phonenumbers.parse(phn, "GB")
print(phonenumbers.is_valid_number(my_number))
print(carrier.name_for_number(my_number, "en"))
print(timezone.time_zones_for_number(my_number))
print(geocoder.description_for_number(my_number, 'en'))
