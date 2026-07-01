class phone:
    def app(self):
        print("In built apps")
    
    def screen(self):
        print("Touch screen")
    
    def charging_port(self):
        print("type-c")

class vivo(phone):
    def os(self):
        print("Origin OS")
    
    def speciality(self):
        print("Camera")
    

class asus(phone):
    def os(self):
        print("Android")
    
    def speciality(self):
        print("Gaming")

a = asus()
v = vivo()

print("Asus")
a.app()
a.screen()
a.charging_port()
a.os()
a.speciality()

print("\n")
print("Vivo")
v.app()
v.screen()
v.charging_port()
v.os()
v.speciality()