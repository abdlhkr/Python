# Global BinaryTree nesnesi,
import tkinter as tk

class Ogrenci:
    def __init__(self, ad, vize, final):
        self.ad = ad
        self.vize = vize
        self.final = final
        self.sonuc = None
        self.durum = None  # Harf notu için durum
        self.hesapla()

    def hesapla(self):
        """Not ortalamasını hesaplar."""
        self.sonuc = self.vize * 0.4 + self.final * 0.6

    def __str__(self):
        return f"{self.ad} ({self.sonuc:.2f}, {self.durum})"



class Node:
    def __init__(self, value):
        self.value = value  # Düğümdeki değer (Ogrenci nesnesi olabilir)
        self.left = None    # Sol çocuk
        self.right = None   # Sağ çocuk

    def __str__(self):
        return str(self.value)


class BinaryTree:
    def search_by_name(self, name):
        """İsme göre öğrenci arar (ağaçta arama yaparak)."""
        return self._search_by_name(self.root, name)

    def _search_by_name(self, node, name):
        if node is None:
            return None
        results = []
        if node.value.ad == name:
            results.append(node.value)
        results.extend(self._search_by_name(node.left, name) or [])
        results.extend(self._search_by_name(node.right, name) or [])
        return results

    def __init__(self):
        self.root = None  # Ağacın kök düğümü
        self.students = []  # Tüm öğrencilerin listesi (çan için)

    def insert(self, ogrenci):
        """Ağaca yeni bir öğrenci ekler."""
        self.students.append(ogrenci)  # Çan hesaplama için listeye ekle
        if not self.root:
            self.root = Node(ogrenci)
        else:
            self._insert(self.root, ogrenci)

    def _insert(self, current_node, ogrenci):
        if ogrenci.sonuc < current_node.value.sonuc:  # Sonuç notuna göre sıralama
            if current_node.left is None:
                current_node.left = Node(ogrenci)
            else:
                self._insert(current_node.left, ogrenci)
        else:
            if current_node.right is None:
                current_node.right = Node(ogrenci)
            else:
                self._insert(current_node.right, ogrenci)
    def inorder_traversal(self, node):
        """Ağacı sıralı (in-order) gezerek elemanları yazdırır."""
        if node:
            self.inorder_traversal(node.left)
            print(f"{node.value.ad}: {node.value.sonuc:.2f} - {node.value.durum} \n")
    def calculate_can(self):
        """Çan notunu hesaplar ve her öğrenci için harf notunu atar."""
        # Çan: Öğrencilerin sonuçlarının ortalaması
        can = sum(student.sonuc for student in self.students) / len(self.students)
        print(f"\nÇan Ortalaması: {can:.2f}")

        # Çan sistemine göre harf notlarını ata
        for student in self.students:
            if student.sonuc >= can + 20:
                student.durum = "AA"
            elif student.sonuc >= can + 10:
                student.durum = "BA"
            elif student.sonuc >= can:
                student.durum = "BB"
            elif student.sonuc >= can - 10:
                student.durum = "CB"
            elif student.sonuc >= can - 20:
                student.durum = "CC"
            else:
                student.durum = "FF"

tree = BinaryTree()

def arayuz():
    root = tk.Tk()
    root.title("Öğrenci Bilgi Sistemi")
    root.geometry("600x600")

    def ekle():
        ad = ad_entry.get()
        vize = float(vize_entry.get())
        final = float(final_entry.get())
        ogrenci = Ogrenci(ad, vize, final)
        tree.insert(ogrenci)
        tree.calculate_can()  # Çan hesaplamasını burada yeniden yap
        ad_entry.delete(0, tk.END)
        vize_entry.delete(0, tk.END)
        final_entry.delete(0, tk.END)


    def listele():
        listbox.delete(0, tk.END)
        def add_to_listbox(node):
            if node:
                add_to_listbox(node.left)
                listbox.insert(tk.END, f"{node.value.ad}: {node.value.sonuc:.2f} - {node.value.durum}")
                print(f"{node.value.ad}: {node.value.sonuc:.2f} - {node.value.durum} \n")
                add_to_listbox(node.right)
                with open("dosya.txt", "a") as dosya:
                    dosya.write(f"{node.value.ad}: {node.value.sonuc:.2f} - {node.value.durum}\n")

        add_to_listbox(tree.root)

    def can_hesapla():
        tree.calculate_can()
        

    def ara():
        ad = ara_entry.get()
        ogrenciler = tree.search_by_name(ad)
        listbox.delete(0, tk.END)  # Temizle önce
        if ogrenciler:
            for ogrenci in ogrenciler:
                listbox.insert(tk.END, f"{ogrenci.ad}: Vize: {ogrenci.vize}, Final: {ogrenci.final}, Sonuç: {ogrenci.sonuc:.2f}, Durum: {ogrenci.durum}")
        else:
            listbox.insert(tk.END, "Öğrenci bulunamadı.")

    ad_label = tk.Label(root, text="Ad:")
    ad_label.pack()
    ad_entry = tk.Entry(root)
    ad_entry.pack()
    vize_label = tk.Label(root, text="Vize:")
    vize_label.pack()
    vize_entry = tk.Entry(root)
    vize_entry.pack()

    final_label = tk.Label(root, text="Final:")
    final_label.pack()
    final_entry = tk.Entry(root)
    final_entry.pack()

    ekle_button = tk.Button(root, text="Ekle", command=ekle)
    ekle_button.pack()

    can_hesapla_button = tk.Button(root, text="Çan Hesapla", command=can_hesapla)
    can_hesapla_button.pack()

    listele_button = tk.Button(root, text="Listele", command=listele)
    listele_button.pack()

    ara_label = tk.Label(root, text="Öğrenci Ara:")
    ara_label.pack()
    ara_entry = tk.Entry(root)
    ara_entry.pack()
    ara_button = tk.Button(root, text="Ara", command=ara)
    ara_button.pack()
    listbox = tk.Listbox(root,width=60, height=50)
    listbox.pack()
    
    root.mainloop()

# Test için başlangıçta birkaç öğrenci ekleyelim
ogr1 = Ogrenci("Ahmet", 70, 80)
ogr2 = Ogrenci("Mehmet", 60, 90)
ogr3 = Ogrenci("Ayşe", 80, 85)
ogr4 = Ogrenci("Fatma", 50, 65)
ogr5 = Ogrenci("Ali", 30, 40)

tree.insert(ogr1)
tree.insert(ogr2)
tree.insert(ogr3)
tree.insert(ogr4)
tree.insert(ogr5)

# Çan hesaplama ve harf notu atama
tree.calculate_can()

arayuz()

# Öğrencileri ekleyip test etme
tree = BinaryTree()
ogr1 = Ogrenci("Ahmet", 70, 80)
ogr2 = Ogrenci("Mehmet", 60, 90)
ogr3 = Ogrenci("Ayşe", 80, 85)
ogr4 = Ogrenci("Fatma", 50, 65)
ogr5 = Ogrenci("Ali", 30, 40)

tree.insert(ogr1)
tree.insert(ogr2)
tree.insert(ogr3)
tree.insert(ogr4)
tree.insert(ogr5)

# Çan hesaplama ve harf notu atama
tree.calculate_can()

# Ağacı sıralı gezerek yazdırma
print("\nSıralı gezinme:")
tree.inorder_traversal(tree.root)
