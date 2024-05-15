import math
# Defines the mesurments for the various can sizes
num1_picnic_radius = 6.83
num1_picnic_height = 10.16
num1_tall_radius = 7.78
num1_tall_height = 11.91
num2_radius = 8.73
num2_height = 11.59
num2half_radius = 10.32
num2half_height = 11.91
num3_radius = 10.79
num3_height = 17.78
num5_radius = 13.02
num5_height = 14.29
num6_radius = 5.40
num6_height = 8.89
num8_radius = 6.83
num8_height = 7.62
num10_radius = 15.72
num10_height = 17.78
num211_radius = 6.83
num211_height = 12.38
num300_radius = 7.62
num300_height = 11.27
num303_radius = 8.10
num303_height = 11.11
def main():
    """
    This function 
    computes the volume, 
    surface area, 
    and storage efficiency
    for each of the can sizes
    """

# computes the volume for each of the can sizes
    num1_vol = compute_volume(num1_picnic_radius, num1_picnic_height)
    num1_tall_vol = compute_volume(num1_tall_radius, num1_tall_height)
    num2_vol = compute_volume(num2_radius, num2_height)
    num2half_vol = compute_volume(num2half_radius, num2half_height)
    num3_vol = compute_volume(num3_radius, num3_height)
    num5_vol = compute_volume(num5_radius, num5_height)
    num6_vol = compute_volume(num6_radius, num6_height)
    num8_vol = compute_volume(num8_radius, num8_height)
    num10_vol = compute_volume(num10_radius, num10_height)
    num211_vol = compute_volume(num211_radius, num211_height)
    num300_vol = compute_volume(num300_radius, num300_height)
    num303_vol = compute_volume(num303_radius, num303_height)

# computes the surface area for each of the can sizes
    num1_sa = compute_surface_area(num1_picnic_radius, num1_picnic_height)
    num1_tall_sa = compute_surface_area(num1_tall_radius, num1_tall_height)
    num2_sa = compute_surface_area(num2_radius, num2_height)  
    num2half_sa = compute_surface_area(num2half_radius, num2half_height)
    num3_sa = compute_surface_area(num3_radius, num3_height)  
    num5_sa = compute_surface_area(num5_radius, num5_height)
    num6_sa = compute_surface_area(num6_radius, num6_height)
    num8_sa = compute_surface_area(num8_radius, num8_height)
    num10_sa = compute_surface_area(num10_radius, num10_height)
    num211_sa = compute_surface_area(num211_radius, num211_height)
    num300_sa = compute_surface_area(num300_radius, num300_height)
    num303_sa = compute_surface_area(num303_radius, num303_height)

# computes the storage efficiency for each of the can sizes
    num1_eff = round(compute_efficancy(num1_vol, num1_sa),2)
    num1_tall_eff = round(compute_efficancy(num1_tall_vol, num1_tall_sa),2)
    num2_eff = round(compute_efficancy(num2_vol, num2_sa),2)
    num2half_eff =round(compute_efficancy(num2half_vol, num2half_sa),2)
    num3_eff = round(compute_efficancy(num3_vol, num3_sa),2)
    num5_eff = round(compute_efficancy(num5_vol, num5_sa),2)
    num6_eff = round(compute_efficancy(num6_vol, num6_sa),2)
    num8_eff = round(compute_efficancy(num8_vol, num8_sa),2)
    num10_eff = round(compute_efficancy(num10_vol, num10_sa),2)
    num211_eff = round(compute_efficancy(num211_vol, num211_sa),2)
    num300_eff = round(compute_efficancy(num300_vol, num300_sa),2)
    num303_eff = round(compute_efficancy(num303_vol, num303_sa),2)

# displays the storage efficiency for each of the can sizes
    print(f"#1 Picnic: {num1_eff}")
    print(f"#1 Tall: {num1_tall_eff}")
    print(f"#2: {num2_eff}")
    print(f"#2.5: {num2half_eff}")
    print(f"#3 cylinder: {num3_eff}")
    print(f"#5: {num5_eff}")
    print(f"#6Z: {num6_eff}")
    print(f"#8Z short: {num8_eff}")
    print(f"#10:  {num10_eff}")
    print(f"#211: {num211_eff}")
    print(f"#300: {num300_eff}")
    print(f"#303: {num303_eff}")

def compute_volume(radius, height):
    volume =math.pi * (radius**2) * height
    return volume

def compute_surface_area(radius, height):
    surface_area = 2 * math.pi*radius * (radius+height)
    return surface_area

def compute_efficancy(volume, surface):
    efficancy= volume/surface
    return efficancy

main()
