from django.db import models

# Produk Laundry
class Produk(models.Model):
    nama = models.CharField(max_length=100)  # nama produk bebas, tidak pakai choices
    harga_per_kg = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.nama} - Rp{self.harga_per_kg:,.0f}"


# Transaksi Penjualan
class Transaksi(models.Model):
    tanggal = models.DateField(auto_now_add=True)
    nama_pelanggan = models.CharField(max_length=100)
    produk = models.ForeignKey(Produk, on_delete=models.CASCADE)
    berat_kg = models.DecimalField(max_digits=5, decimal_places=2)

    def total_harga(self):
        return self.berat_kg * self.produk.harga_per_kg

    def __str__(self):
        return f"{self.nama_pelanggan} - {self.produk.nama} ({self.berat_kg} kg)"
