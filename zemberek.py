# -*- coding:utf-8 -*-

import jpype


class Stemmer():

    def __init__(self):
        jpype.startJVM("/Library/Java/JavaVirtualMachines/jdk1.8.0_77.jdk/Contents/Home/jre/lib/jli/libjli.dylib",
                    "-Djava.class.path=/Users/macbook/PycharmProjects/ANN/zemberek-tum-2.0.jar", "-ea")
        # Türkiye Türkçesine göre çözümlemek için gerekli sınıfı hazırla
        Tr = jpype.JClass("net.zemberek.tr.yapi.TurkiyeTurkcesi")

        # tr nesnesini oluştur
        self.tr = Tr()

        # Zemberek sınıfını yükle
        Zemberek = jpype.JClass("net.zemberek.erisim.Zemberek")

        # zemberek nesnesini oluştur
        self.zemberek = Zemberek(self.tr)

    def stem_list(self,words):
        for kelime in words:
            if kelime.strip()>'':
                kelime = unicode(kelime.decode('utf-8'))
                yanit = self.zemberek.kelimeCozumle(kelime)
                if yanit:
                    #print unicode(yanit[0]).encode('utf-8')
                    #kok = jpype.JClass('net.zemberek.yapi.Kok')
                    kok = yanit[0]
                    #print unicode(kok.kok()).encode('utf-8').split(' ')[0]
                else:
                    print("{} ÇÖZÜMLENEMEDİ".format(kelime))

    def stem_str(self, word):
        kelime = unicode(word.decode('utf-8'))
        yanit = self.zemberek.kelimeCozumle(kelime)
        if yanit:
            # print unicode(yanit[0]).encode('utf-8')
            kok = yanit[0]
            #print unicode(kok.kok()).encode('utf-8').split(' ')[0]
            return unicode(kok.kok()).encode('utf-8').split(' ')[0]
        else:
            print word
            return word

    def stem(self,obj):
        if isinstance(obj,list):
            return self.stem_list(obj)
        elif isinstance(obj,str):
            return self.stem_str(obj)

    def close(self):
        #JVM kapat
        jpype.shutdownJVM()