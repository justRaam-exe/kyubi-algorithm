class Ninja:
    def __init__(self, name, chakra=0):
        self.name = name
        self.chakra = chakra
        self.children = []

def find_ninja(name, all_ninja):
    for ninja in all_ninja:
        if ninja.name == name:
            return ninja
    return None

def share_chakra(ninja, decay):
    for child in ninja.children:
        if ninja.chakra >= decay:
            child.chakra = decay
            ninja.chakra -= decay  # kurangi chakra pemberi
            print(f"{ninja.name} membagikan {decay} chakra ke {child.name} (sisa: {ninja.chakra})")
            share_chakra(child, decay)  # hanya lanjut kalau chakra diterima
        else:
            print(f"{ninja.name} TIDAK CUKUP chakra untuk {child.name} (dibutuhkan: {decay}, sisa: {ninja.chakra})")

def show_chakra(ninja, level=0):
    print("  " * level + f"{ninja.name}: {ninja.chakra}")
    for child in ninja.children:
        show_chakra(child, level + 1)

all_ninja = []

# Input root ninja
root_name = input("Masukkan nama ninja utama: ")
root_chakra = int(input(f"Masukkan jumlah chakra untuk {root_name}: "))
root = Ninja(root_name, root_chakra)
all_ninja.append(root)

# Input anak-anak dari root saja
n = int(input(f"Berapa banyak ninja yang akan menerima chakra langsung dari {root_name}?: "))
for _ in range(n):
    child_name = input("Masukkan nama ninja penerima chakra: ")
    
    child = find_ninja(child_name, all_ninja)
    if child is None:
        child = Ninja(child_name)
        all_ninja.append(child)

    root.children.append(child)

# Masukkan nilai decay chakra
decay = int(input("Masukkan jumlah chakra yang dibagikan ke setiap ninja: "))
print("\nDistribusi Chakra:")
share_chakra(root, decay)

# Tampilkan hasil
print("\nChakra Akhir Tiap Ninja:")
show_chakra(root)
