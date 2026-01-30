#Dictionary -- Defined with key, value pair...can store multiple elements
#Collection of un ordered pars, but works based on the Index
#Ex1. Create dictionary
# Dic1 = {"key1":"value1","key2":"value2"}
# print(Dic1) #{'key1': 'value1', 'key2': 'value2'}
# print(Dic1["key1"]) #value1
# print(Dic1["key2"]) #alue2

#Ex2.
# Vehicle = {"Brand":"Hyundai","Model":'i20',"Year": 2010}
# print(Vehicle)
# print(Vehicle["Brand"]) #Hyundai
# print(Vehicle["Model"]) #i20
# print(Vehicle["Year"])  #2010

# Access elements using get()...............
# Vehicle.get("Brand")
# Vehicle.get("Model")
# Vehicle.get("Year")
# print(Vehicle.get("Brand"))
# print(Vehicle.get("Model"))
# print(Vehicle.get("Year"))

#E3. Update dictionary
# Vehicle["Brand"] = "Honda"
# Vehicle["Model"] = "Amaze"
# Vehicle["Year"] = 2020
# print(Vehicle)  #{'Brand': 'Honda', 'Model': 'Amaze', 'Year': 2020}

#Ex4. Reading elemets from dic
# for i in Vehicle:
#     print(i)
# for i in Vehicle.values():
#     print(i)
# for i in Vehicle.keys():
#     print(i)
# for x,y in Vehicle.items():
#     print(x,y)

#Ex4. Check for items in dic
# Vehicle = {"Brand":"Hyundai","Model":'i20',"Year": 2010}
# if "Model" in Vehicle:
#     print("Model in Vehicle")
# else:
#     print("Model not in Vehicle")
# print(len(Vehicle))
#
# #
# print(Vehicle["Brand" not in Vehicle])

# Ex Adding items to dic
# Vehicle = {"Brand":"Hyundai","Model":'i20',"Year": 2010}
# Vehicle["color"] = "red"
# print(Vehicle)

#$x Remove items from dic
Vehicle = {"Brand":"Hyundai","Model":'i20',"Year": 2010}
Vehicle.pop("Brand")
print(Vehicle)  #{'Model': 'i20', 'Year': 2010}

#Ex Copy dic
Vehicle1 = Vehicle
print(Vehicle1)









