from django.shortcuts import render, redirect
from .models import Produk, Transaksi
from .forms import ProdukForm, TransaksiForm
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'laundry_app/home.html')

@login_required
def laporan_harian(request):
    today = timezone.now().date()
    transaksi_list = Transaksi.objects.filter(tanggal=today)
    return render(request, 'laundry_app/laporan_harian.html', {'transaksi_list': transaksi_list})

@login_required
def laporan_mingguan(request):
    today = timezone.now().date()
    minggu_lalu = today - timedelta(days=7)
    transaksi_list = Transaksi.objects.filter(tanggal__range=(minggu_lalu, today))
    return render(request, 'laundry_app/laporan_mingguan.html', {'transaksi_list': transaksi_list})

@login_required
def laporan_bulanan(request):
    today = timezone.now().date()
    bulan_lalu = today.replace(day=1)  # Awal bulan
    transaksi_list = Transaksi.objects.filter(tanggal__gte=bulan_lalu)
    return render(request, 'laundry_app/laporan_bulanan.html', {'transaksi_list': transaksi_list})

@login_required
def transaksi_penjualan(request):
    transaksi = Transaksi.objects.all().order_by('-tanggal')
    return render(request, 'laundry_app/transaksi_penjualan.html', {
        'transaksi': transaksi
    })

@login_required
def inisialisasi_produk():
    if Produk.objects.count() == 0:
        Produk.objects.create(nama='Cuci Kering', harga_per_kg=5000)
        Produk.objects.create(nama='Cuci Setrika', harga_per_kg=6000)
        Produk.objects.create(nama='Cuci Kering Setrika', harga_per_kg=7000)

@login_required
def transaksi_terakhir(request):
    transaksi = Transaksi.objects.latest('id')  # transaksi terakhir berdasarkan ID
    return render(request, 'laundry_app/detail_transaksi.html', {
        'transaksi': transaksi
    })

    # ✅ Fungsi biasa tanpa dekorator
def inisialisasi_produk():
    if Produk.objects.count() == 0:
        Produk.objects.create(nama='Cuci Kering', harga_per_kg=5000)
        Produk.objects.create(nama='Cuci Setrika', harga_per_kg=6000)
        Produk.objects.create(nama='Cuci Kering Setrika', harga_per_kg=7000)

@login_required
def daftar_produk(request):
    produk_list = Produk.objects.all()
    return render(request, 'laundry_app/daftar_produk.html', {'produk_list': produk_list})

@login_required
def tambah_produk(request):
    if request.method == 'POST':
        form = ProdukForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('daftar_produk')
    else:
        form = ProdukForm()
    return render(request, 'laundry_app/form_produk.html', {'form': form})

@login_required
def edit_produk(request, pk):
    produk = Produk.objects.get(pk=pk)
    form = ProdukForm(request.POST or None, instance=produk)
    if form.is_valid():
        form.save()
        return redirect('daftar_produk')
    return render(request, 'laundry_app/form_produk.html', {'form': form})

@login_required
def hapus_produk(request, pk):
    produk = Produk.objects.get(pk=pk)
    if request.method == 'POST':
        produk.delete()
        return redirect('daftar_produk')
    return render(request, 'laundry_app/konfirmasi_hapus.html', {'produk': produk})



@login_required
def tambah_produk(request):
    if request.method == 'POST':
        form = ProdukForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProdukForm()
    return render(request, 'laundry_app/form_produk.html', {'form': form})



@login_required
def tambah_transaksi(request):
    if request.method == 'POST':
        form = TransaksiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaksi_terakhir')
    else:
        form = TransaksiForm()
    return render(request, 'laundry_app/form_transaksi.html', {'form': form})

