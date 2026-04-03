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
# نسخة متطورة: حساب زاوية الانكسار داخل الزجاج
def calculate_refraction(angle_in_degrees, n_glass=1.5):
    # n_air = 1.0 (معامل انكسار الهواء)
    angle_radians = math.radians(angle_in_degrees)
    
    # قانون سنيل: n1 * sin(theta1) = n2 * sin(theta2)
    sin_theta2 = math.sin(angle_radians) / n_glass
    angle_out_radians = math.asin(sin_theta2)
    
    return math.degrees(angle_out_radians)

# تجربة شعاع ساقط بزاوية 45 درجة
angle_in = 45
angle_out = calculate_refraction(angle_in)
print(f"الشعاع سقط بزاوية {angle_in} وانكسر داخل الزجاج بزاوية {angle_out:.2f}")
