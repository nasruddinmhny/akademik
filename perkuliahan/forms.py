from django import forms
from .models import Jurusan,Mahasiswa,Dosen
from django.forms import NumberInput


class Tambah_jurusan(forms.ModelForm):
    class Meta:
        model = Jurusan #tmodel -> table table jurusan
        fields = '__all__'#menggunakan semua field yang terdapat pada table jurusan
        
    def clean_kodejurusan(self):
        clean_data = super().clean()
        kodejur = clean_data.get('kodejurusan')
        
        if Jurusan.objects.filter(kodejurusan = kodejur).first():
            raise forms.ValidationError("kode jurusan sudah ada")
        return kodejur
    
    def clean_namajurusan(self):
        clean_data = super().clean()
        namajur = clean_data.get('namajurusan')
        
        if Jurusan.objects.filter(namajurusan = namajur).first():
            raise forms.ValidationError("nama jurusan sudah ada")
        return namajur

class Edit_Jurusan(forms.ModelForm):
     class Meta:
        model = Jurusan #tmodel -> table table jurusan
        fields = '__all__'#menggunakan semua field yang terdapat pada table jurusan
        
class TambahMahasiswa(forms.ModelForm):
    class Meta:
        model = Mahasiswa
        fields = '__all__'
       
    def clean_nim(self):
        clean_data = super().clean()
        nimMhs = clean_data.get('nim')
        
        if Mahasiswa.objects.filter(nim = nimMhs).first():
            raise forms.ValidationError("Nim sudah ada")
        return nimMhs
    
    def clean_email(self):
        clean_data = super().clean()
        emailmhs = clean_data.get('email')
        
        if Mahasiswa.objects.filter(email = emailmhs).first():
            raise forms.ValidationError("email sudah ada")
        return emailmhs
        
        
class EditMahasiswa(forms.ModelForm):
    class Meta:
        model = Mahasiswa
        fields = '__all__'
    

class TambahDosen(forms.ModelForm):
    class Meta:
        model = Dosen
        fields = '__all__'

    tgllahir = forms.DateField(label='Tanggal Ujikom',widget=NumberInput(attrs={'type': 'date'}))
