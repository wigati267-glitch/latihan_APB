from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('laporan/harian/', views.laporan_harian, name='laporan_harian'),
    path('laporan/mingguan/', views.laporan_mingguan, name='laporan_mingguan'),
    path('laporan/bulanan/', views.laporan_bulanan, name='laporan_bulanan'),

    # Transaksi
    path('penjualan/', views.transaksi_penjualan, name='transaksi_penjualan'),
    path('penjualan/tambah/', views.tambah_transaksi, name='tambah_transaksi'),
    path('penjualan/terakhir/', views.transaksi_terakhir, name='transaksi_terakhir'),
    path('produk/', views.daftar_produk, name='daftar_produk'),
    path('produk/tambah/', views.tambah_produk, name='tambah_produk'),
    path('produk/edit/<int:pk>/', views.edit_produk, name='edit_produk'),
    path('produk/hapus/<int:pk>/', views.hapus_produk, name='hapus_produk'),
]

