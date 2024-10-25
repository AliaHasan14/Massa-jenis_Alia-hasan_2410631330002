def hitung_massa_dari_massa_jenis(rho,v):
    m = rho * v
    return m

def hitung_volume_dari_massa_jenis(rho,m):
    v = m/rho
    return v

def hitung_massa_jenis(m,v):
    rho = m/v
    return rho

def menu():
    print("Program untuk menghitung massa jenis")
    print("1. Hitung massa (m = rho * v)")
    print("2. Hitung volume (v = m/rho)")
    print("3. Hitung massa jenis (rho = m/v)")

    pilihan = input("Masukan pilihan (1/2/3):")

    if pilihan == '1':
        rho = float(input("masukan massa jenis dalam kg/m**3:"))
        v = float(input("masukan volume dalam m**3: "))
        m = hitung_massa_dari_massa_jenis(rho,v)
        print(f"massa: {m} kg")

    elif pilihan == '2':
        rho = float(input("Masukan massa jenis dalam kg/m**3: "))
        m = float(input("masukan massa dalam kg: "))
        v = hitung_volume_dari_massa_jenis(rho,m)
        print(f"volume: {v}m**3")

    elif pilihan == '3':
        m = float(input("masukan masssa dalam kg: "))
        v = float(input("masukan volume dalam m**3: "))
        rho = hitung_massa_jenis(m,v)
        print(f"massa jenis: {rho}kg/m**3")

    else :
        print("pilihan tidak sesuai,silahkan pilih 1/2/3")

if __name__=="__main__":
   menu()