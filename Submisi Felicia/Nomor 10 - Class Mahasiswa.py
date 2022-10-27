class Mahasiswa:
    def __init__(self, nama, id, angkatan, jurusan):
        self.nama = nama
        self.id = id
        self.angkatan = angkatan
        self.jurusan = jurusan
        
    def print_biodata(self):
        print('BIODATA MAHASISWA')
        # Using triple quotes instead will mess with indentations
        print(
            f'ID: {self.id} \n'
            f'Nama: {self.nama} \n'
            f'Angkatan: {self.angkatan} \n'
            f'Jurusan: {self.jurusan} \n'
        )
        
mahasiswa_1 = Mahasiswa('Ani', 1, 2017, 'Akuntansi')
mahasiswa_2 = Mahasiswa('Dede', 2, 2018, 'Desain')
mahasiswa_3 = Mahasiswa('Hanis', 3, 2019, 'Hukum')

mahasiswa_1.print_biodata()
mahasiswa_2.print_biodata()
mahasiswa_3.print_biodata()