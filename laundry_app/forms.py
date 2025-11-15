from django import forms
from .models import Produk, Transaksi

class ProdukForm(forms.ModelForm):
    class Meta:
        model = Produk
        fields = ['nama', 'harga_per_kg']

class TransaksiForm(forms.ModelForm):
    class Meta:
        model = Transaksi
        fields = ['nama_pelanggan', 'produk', 'berat_kg']
