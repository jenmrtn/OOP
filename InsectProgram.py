import InsectClass as i
mosquito= i.Insect("mosquito",2,2)
housefly= i.Insect('housefly',2,4)
#my_insect= i.Insect()

#my_insect.flightlength()
mosquito.flightlength()
housefly.flightlength()

print(f'The {mosquito.get_name()} can fly: {mosquito.get_flight()} miles')

