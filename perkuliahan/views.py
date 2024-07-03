from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Tambah_jurusan,Edit_Jurusan,TambahMahasiswa,EditMahasiswa,TambahDosen
from django.contrib import messages
from .models import Jurusan,Mahasiswa,Dosen

# Create your views here.
def dashboard(request):
    return render(request,'dashboard.html')

def profil(request):
    return render(request,'profil.html')

def matakuliah(request):
    return render(request,'matakuliah.html')

def mahasiswa(request):
    return render(request,'mahasiswa.html')

def jurusan(request):
    # select * from jurusan
    jurusan = Jurusan.objects.all()

    context={
        'tite':'DATA JURUSAN',
        'jurusan':jurusan,
    }
    return render(request,'jurusan.html',context)

def tambah_jurusan(request):
    
    if request.method == "POST":
        form = Tambah_jurusan(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Disimpan')
            return redirect('manage_jurusan')
    else:
        form = Tambah_jurusan()

    context = {
        'title':'Form Tambah Jurusan',
        'form': form,
    }
    return render(request,'tambah_jurusan.html',context)

def edit_jurusan(request,jurusanid):

    jurusan = Jurusan.objects.get(id=jurusanid)

    if request.method == "POST":
        form = Edit_Jurusan(request.POST,instance = jurusan)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Berhasil Diubah')
            return redirect('manage_jurusan')
    else:
        form = Edit_Jurusan(instance=jurusan)

    context = {
        'title':'FORM UPDATE JURUSAN',
        'form':form,
    }
    return render(request,'edit_jurusan.html',context)

def hapus_jurusan(request,jurusanid):
    jurusan = Jurusan.objects.get(id = jurusanid)
    jurusan.delete()
    messages.success(request,'Data Dihapus')
    return redirect('manage_jurusan')

def mahasiswa(request):
    mhs = Mahasiswa.objects.all()# select * from mahasiswa
    
    context ={
        'title':'DATA MAHASISWA',
        'mhs':mhs,
    }
    return render(request,'mahasiswa.html',context)

def tambah_mahasiswa(request):
    
    if request.method == 'POST':
        form = TambahMahasiswa(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Mahasiswa Disimpan')
            return redirect('manage_mahasiswa')
    else:
        form = TambahMahasiswa()
        
    context = {
        'title':'TAMBAH MAHASISWA',
        'form':form,
    }
    return render(request,'tambah_mahasiswa.html',context)

def edit_mahasiswa(request,mhsid):
    #editmhs = Mahasiswa.objects.get(id = mhsid)
    editmhs = Mahasiswa.objects.filter(id = mhsid).first()
    
    if request.method == 'POST':
        form = EditMahasiswa(request.POST,instance=editmhs)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Mahasiswa Di ubah')
            return redirect('manage_mahasiswa')
    else:
        form = EditMahasiswa(instance=editmhs)
        
    context = {
        'title':'EDIT DATA MAHASISWA',
        'form':form,
    }
    return render(request,'edit_mahasiswa.html',context)

def hapus_mahasiswa(request,mhsid):
    delmhs = Mahasiswa.objects.filter(id = mhsid).first()
    delmhs.delete()
    messages.success(request,'Data Dihapus')
    return redirect('manage_mahasiswa')
    
    
def dosen(request):
    dosen = Dosen.objects.all()
    
    context={
        'dosen':dosen,
    }
    return render(request,'dosen.html',context)

def tambah_dosen(request):
    
    if request.method == 'POST':
        form = TambahDosen(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Data Ddosen Disimpan')
            return redirect('manage_dosen')
    else:
        form = TambahDosen()
    
    context = {
        'form':form,
    }
    return render(request,'tambah_dosen.html',context)

def viewdosen(request,dosenid):
    dosen = Dosen.objects.filter(id = dosenid).first()
    
    context = {
        'dosen': dosen,
    }
    return render(request,'viewdosen.html',context)