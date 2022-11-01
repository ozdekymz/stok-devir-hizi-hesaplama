
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
import mysql.connector

class stokDevirhizi(QWidget):
    def __init__(self,parent=None):
        super(stokDevirhizi,self).__init__(parent)        
        grid=QGridLayout()
#Label tanımlama:
        grid.addWidget(QLabel(""),0,0,1,2)
        grid.addWidget(QLabel("Stok kodu(STU)"),1,0)
        grid.addWidget(QLabel("Ürün adı"),2,0)
        grid.addWidget(QLabel("Son kullanma tarihi(SKT)"),3,0)
        grid.addWidget(QLabel("Satılan Ürünlerin Toplam Maliyeti(TL)"),4,0)
        grid.addWidget(QLabel("Dönem Başı Envanteri(Stok Miktarı)"),5,0)
        grid.addWidget(QLabel("Dönem Sonu Envanteri(Stok Miktarı)"),6,0) 
#Input girişi:        
        self.stokKod=QLineEdit()
        grid.addWidget(self.stokKod,1,1)
        self.urunAd=QLineEdit()
        grid.addWidget(self.urunAd,2,1)
        self.tarih=QDateEdit(calendarPopup=True)
        grid.addWidget(self.tarih,3,1)
        self.topMaliyet=QLineEdit()
        grid.addWidget(self.topMaliyet,4,1)
        self.donemBasiEnvanter=QLineEdit()
        grid.addWidget(self.donemBasiEnvanter,5,1)
        self.donemSonuEnvanter=QLineEdit()
        grid.addWidget(self.donemSonuEnvanter,6,1)
#Buton Tanımlama:
        hesaplaDugme=QPushButton("Hesapla")
        hesaplaDugme.clicked.connect(self.devirHesapla)
        grid.addWidget(hesaplaDugme,7,0,1,1)
        temizle=QPushButton("Temizle")        
        temizle.clicked.connect(self.temizle)
        grid.addWidget(temizle,7,1)
        kaydet=QPushButton("Kaydet")
        kaydet.clicked.connect(self.kaydet)
        grid.addWidget(kaydet,7,2)
        kayitAktar=QPushButton("Kayıt Aktar")
        kayitAktar.clicked.connect(self.kayitAktar)
        grid.addWidget(kayitAktar,0,2,8,1)
#Kayıt göster sağ:
        grid.addWidget(QLabel("Stok Kodu(STU):"),1,4)
        grid.addWidget(QLabel("Ürün Adı:"),2,4)
        grid.addWidget(QLabel("Son Kullanma Tarihi(SKU)"),3,4)
        grid.addWidget(QLabel("Satılan Ürünlerin Toplam Maliyeti(TL):"),4,4)
        grid.addWidget(QLabel("Dönem Başı Envanteri(Stok Miktarı):"),5,4)
        grid.addWidget(QLabel("Dönem Sonu Envanteri(Stok Miktarı):"),6,4)        
#Kayıt aktarma labellerı:        
        self.stokKodLabel=QLabel()
        self.urunAdLabel=QLabel()
        self.tarihLabel=QLabel()
        self.topMaliyetLabel=QLabel()                
        self.donemBasiEnvanterLabel=QLabel()
        self.donemSonuEnvanterLabel=QLabel()
        
        grid.addWidget(self.stokKodLabel,1,5)
        grid.addWidget(self.urunAdLabel,2,5)
        grid.addWidget(self.tarihLabel,3,5)
        grid.addWidget(self.topMaliyetLabel,4,5)
        grid.addWidget(self.donemBasiEnvanterLabel,5,5)
        grid.addWidget(self.donemSonuEnvanterLabel,6,5)
#Buton sağ:
        oncekiKayit=QPushButton("Önceki Kayıt")        
        oncekiKayit.clicked.connect(self.oncekiKayit)
        grid.addWidget(oncekiKayit,7,4)
        
        sonrakiKayit=QPushButton("Sonraki Kayıt")
        sonrakiKayit.clicked.connect(self.sonrakiKayit)
        grid.addWidget(sonrakiKayit,7,5)

        grid.addWidget(QLabel("Stok Devir Hızı:"),8,0)
        self.sonuc=QLabel("")
        grid.addWidget(self.sonuc, 8, 1)
        
        self.setLayout(grid)
        self.setWindowIcon(QIcon("logo.png"))
        self.setWindowTitle("Stok Devir Hızı Hesaplama Uygulaması")
        self.resize(1000,100)
                        
    def temizle(self):
        self.stokKod.setText("")
        self.urunAd.setText("")        
        self.topMaliyet.setText("")
        self.donemBasiEnvanter.setText("")
        self.donemSonuEnvanter.setText("")
        self.tarih.clear()
        
    def kaydet(self):
        stokKod = self.stokKod.text()
        urunAd = self.urunAd.text()
        topMaliyet = self.topMaliyet.text()
        donemBasiEnvanter = self.donemBasiEnvanter.text()
        donemSonuEnvanter = self.donemSonuEnvanter.text()        
        tarih = self.tarih.date()
        t=tarih.toPyDate() #kaydederken tarih olarak algılatır.
        

        baglanti=mysql.connector.connect(user="root",password="",host="127.0.0.1",database="programlama_veritabani")
        isaretci=baglanti.cursor()
        isaretci.execute('''INSERT INTO stok_devir(stok_kodu,urun_adi,sk_tarih,top_maliyet,donem_basi_envanter,donem_sonu_envanter)
VALUES ("%s","%s","%s","%s","%s","%s")'''%(stokKod,urunAd,t,topMaliyet,donemBasiEnvanter,donemSonuEnvanter)) #%s:string,%d:int,%0.1f:float
        baglanti.commit()
        baglanti.close()

    def kayitAktar(self):
        stokKod = self.stokKod.text()
        urunAd = self.urunAd.text()
        tarih = self.tarih.date()
        t = tarih.toPyDate()
        tarih = str(t)
        topMaliyet=self.topMaliyet.text()
        donemBasiEnvanter=self.donemBasiEnvanter.text()
        donemSonuEnvanter=self.donemSonuEnvanter.text()
        
        
        
        self.stokKodLabel.setText(stokKod)
        self.urunAdLabel.setText(urunAd)
        self.tarihLabel.setText(tarih)
        self.topMaliyetLabel.setText(topMaliyet)        
        self.donemBasiEnvanterLabel.setText(donemBasiEnvanter)
        self.donemSonuEnvanterLabel.setText(donemSonuEnvanter)
        
    def oncekiKayit(self):
        if self.stokKodLabel.text():
            stokKod=self.stokKodLabel.text()
            baglanti=mysql.connector.connect(user="root",password="",host="127.0.0.1",database="programlama_veritabani")
            isaretci=baglanti.cursor()
            isaretci.execute('''SELECT id FROM stok_devir WHERE stok_kodu="%s" '''%stokKod)
            row=isaretci.fetchall()
            for r in row:
                res = int(''.join(map(str,r)))
                res=res-1
                isaretci.execute('''SELECT * FROM stok_devir WHERE id="%s"'''%res)
                gelenler = isaretci.fetchall()
                for row in gelenler:
                    self.stokKodLabel.setText(row[1])
                    self.urunAdLabel.setText(row[2])
                    self.tarihLabel.setText(row[3])
                    self.topMaliyetLabel.setText(row[4])
                    self.donemBasiEnvanterLabel.setText(row[5])
                    self.donemSonuEnvanterLabel.setText(row[6])                    
            baglanti.close()
    def sonrakiKayit(self):
         if self.stokKodLabel.text():
            stokKod=self.stokKodLabel.text()
            baglanti=mysql.connector.connect(user="root",password="",host="127.0.0.1",database="programlama_veritabani")
            isaretci=baglanti.cursor()
            isaretci.execute('''SELECT id FROM stok_devir WHERE stok_kodu="%s" '''%stokKod)
            row=isaretci.fetchall()
            for r in row:
                res = int(''.join(map(str,r)))
                res=res+1
                isaretci.execute('''SELECT * FROM stok_devir WHERE id="%s"'''%res)
                gelenler = isaretci.fetchall()
                for row in gelenler:
                    self.stokKodLabel.setText(row[1])
                    self.urunAdLabel.setText(row[2])
                    self.tarihLabel.setText(row[3])
                    self.topMaliyetLabel.setText(row[4])
                    self.donemBasiEnvanterLabel.setText(row[5])
                    self.donemSonuEnvanterLabel.setText(row[6])                    
            baglanti.close()

        
    def devirHesapla(self):        
        mal=0
        try:mal=int(self.topMaliyet.text())
        except:pass
        donemBas=0
        try:donemBas=int(self.donemBasiEnvanter.text())
        except:pass
        donemSon=0
        try:donemSon=int(self.donemSonuEnvanter.text())
        except:pass             
        if not mal:
            error_dialog.showMessage('Lütfen Toplam Maliyet Giriniz!,Aksi takdirde ilgili işlem yapılamayacaktır.')            
        if not donemBas:
            error_dialog.showMessage('Lütfen Dönem Başı Envanterini Giriniz!,Aksi takdirde ilgili işlem yapılamayacaktır.')
        if not donemSon:
            error_dialog.showMessage('Lütfen Dönem Sonu Envanterini Giriniz!,Aksi takdirde ilgili işlem yapılamayacaktır.')
        else:
            sonuc= mal / ((donemBas + donemSon) / 2)
            self.sonuc.setText('<font color=blue size=5>%d</font'%sonuc)
            
        

app =QApplication([])
error_dialog = QtWidgets.QErrorMessage()
error_dialog.setWindowTitle("UYARI")
error_dialog.setWindowIcon(QIcon("logo2.png"))
window=stokDevirhizi()
window.show()
app.exec_()



