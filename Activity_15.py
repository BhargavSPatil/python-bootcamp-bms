import math
def inputs():                                               #input values
    l = float(input("Enter the length of tromboloid: "))
    b = float(input("Enter the breadth of tromboloid: "))
    h = float(input("Enter the height of tromboloid: "))
    return l, b, h

def char_dimension(l, b, h):                #calculating characteristic dimension(k)
    k = (l**2 + b**2 + h**2)
    return k

def calc_vol_tromb(b, h, k):                    #calculating volume of tromboloid
    vol_tromb = ((b**2)*(h**2))/math.sqrt(k)
    return vol_tromb

def calc_rad_sphere(vol_tromb):             #calculating radius of sphere having same volume as tromboloid
    rad_cube = (3*vol_tromb)/(4*math.pi)
    rad_sphere = (rad_cube)**(1/3)
    return rad_sphere

def display(vol_tromb, rad_sphere):                                 #printing out the values
    print("The volume of the tromboloid is %.3f" %(vol_tromb))
    print("The radius of the sphere having the same volume of the given tromboloid is %.3f" %(rad_sphere))

def main():
    l, b, h = inputs()
    k = char_dimension(l, b, h)
    vol_tromb = calc_vol_tromb(b, h, k)
    rad_sphere = calc_rad_sphere(vol_tromb)
    display(vol_tromb, rad_sphere)

main()
