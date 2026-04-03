# محرك الفيزياء الأولي لزجاج رشيد الكمومي
import math

def calculate_photon_energy(wavelength_nm):
    # ثابت بلانك وسرعة الضوء
    h = 6.626e-34 
    c = 3.0e8
    wavelength_m = wavelength_nm * 1e-9
    
    # قانون الطاقة: E = (h * c) / wavelength
    energy = (h * c) / wavelength_m
    return energy

# تجربة لاصطياد الأشعة تحت الحمراء (800 نانومتر)
ir_wavelength = 800
energy = calculate_photon_energy(ir_wavelength)

print(f"طاقة الفوتون عند {ir_wavelength} نانومتر هي: {energy} جول")
