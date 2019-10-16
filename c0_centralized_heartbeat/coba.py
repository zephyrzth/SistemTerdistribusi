car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

motor = ["satu", "dua", "tiga"]
motor.insert(5, "empat")
motor.remove("dua")
#print(motor.index("empat"))

car.update({"brand": "Honda"})
a = car.pop("brand")
print(len(car))

#print(len(a))
#print(motor)