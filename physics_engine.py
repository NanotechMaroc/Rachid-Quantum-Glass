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
import random

# خوارزمية احتمالية الاصطدام بالنقاط النانوية
def quantum_hit_simulation(photons_count):
    hits = 0
    trapped_energy = 0
    
    for i in range(photons_count):
        # احتمال 70% أن يصطدم الفوتون بنقطة نانوية (كفاءة عالية)
        probability = random.random()
        if probability < 0.70:
            hits += 1
            trapped_energy += 1.24 # طاقة افتراضية بالـ eV
            
    return hits, trapped_energy

# محاكاة سقوط 1000 فوتون شمس على زجاج رشيد
total_photons = 1000
captured, total_energy = quantum_hit_simulation(total_photons)

print(f"--- نتائج المحاكاة الكمومية ---")
print(f"تم اصطياد {captured} فوتون من أصل {total_photons}")
print(f"إجمالي الطاقة المحصودة: {total_energy:.2f} وحدة طاقة")
# محاكي الطاقة الشمسية لمدينة ورزازات - مشروع رشيد 2026
def simulate_daily_yield(city_name, glass_area_m2):
    # شدة الإشعاع التقريبية لكل ساعة (من 6 صباحاً لـ 6 مساءً)
    solar_intensity_w_m2 = [50, 150, 400, 700, 900, 1000, 950, 800, 500, 200, 50]
    efficiency = 0.70  # كفاءة النقاط الكمومية (خوارزمية رشيد)
    
    total_energy_kwh = 0
    print(f"--- تقرير الطاقة لمدينة {city_name} ---")
    print("الساعة | الطاقة المولدة (وات)")
    print("-" * 30)
    
    for hour, intensity in enumerate(solar_intensity_w_m2, 6):
        generated = intensity * glass_area_m2 * efficiency
        total_energy_kwh += (generated / 1000) # تحويل لـ كيلوواط ساعة
        print(f"{hour:02d}:00 | {generated:.1f} W")
        
    return total_energy_kwh

# تطبيق المحاكاة على نافذة مساحتها 2 متر مربع في ورزازات
area = 2 
daily_total = simulate_daily_yield("Ouarzazate", area)

print("-" * 30)
print(f"إجمالي الطاقة اليومية للنافذة: {daily_total:.2f} kWh")
