import numpy as np
from scipy.interpolate import interp1d, UnivariateSpline

def interpolate_mil(d_target):
    # Menambahkan titik data baru ke dalam array distances dan mil_values
    distances = np.array([
        100, 150, 200, 250, 292.1, 300, 338.7, 350, 400, 450, 500, 550, 
        600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 
        1100, 1150, 1200, 1250, 1300, 1350
    ])
    mil_values = np.array([
        1558, 1538, 1517, 1496, 1478.7, 1475, 1459.0, 1453, 1431, 1409, 1387, 1364, 
        1341, 1317, 1292, 1267, 1240, 1215, 1190, 1167, 1144, 1121, 
        1098, 1076, 1055, 1034, 1013, 994
    ])
    
    # Menggunakan interpolasi spline untuk hasil yang lebih akurat
    spline_func = UnivariateSpline(distances, mil_values, k=3, s=0)
    return spline_func(d_target)

def is_number(input_string):
    """Fungsi untuk memeriksa apakah input bisa dikonversi menjadi float."""
    try:
        number = float(input_string)
        print(f"Berhasil mengkonversi '{input_string}' menjadi {number}")
        return True
    except ValueError:
        print(f"Gagal mengkonversi '{input_string}' menjadi float")
        return False

def main():
    print("=== Interpolasi Mil dari Data Game ===")
    
    while True:
        # Meminta input jarak dari pengguna
        user_input = input("\nMasukkan jarak target (meter) atau ketik 'exit' untuk keluar: ").strip()
        
        # Debug: Menampilkan input untuk melihat karakter
        print(f"Input diterima: '{user_input}' (Panjang: {len(user_input)})")
        
        if user_input.lower() == 'exit':
            print("Terima kasih telah menggunakan program ini.")
            break
        
        # Validasi input numerik
        if is_number(user_input):
            d_target = float(user_input)
            mil = interpolate_mil(d_target)
            print(f"\nPada jarak {d_target} meter, nilai mil adalah: {mil:.2f} mil")
        else:
            print("Input tidak valid. Mohon masukkan nilai numerik atau 'exit' untuk keluar.")

if __name__ == "__main__":
    main()
