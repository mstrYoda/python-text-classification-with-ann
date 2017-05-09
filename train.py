# -*- coding:utf-8 -*-


# ANN and Gradient Descent code from https://iamtrask.github.io//2015/07/27/python-network-part2/
import datetime
import numpy as np
import json
import time
from zemberek import Stemmer

training_data = []

training_data.append({"class":"siyaset", "sentence":"baskan tayyip erdogan"})
training_data.append({"class":"siyaset", "sentence":"Hukumetinde AB bakanligi olupta Avrupa'ya giremeyen tek ulkeyiz. AB Bakanligi kapatilsin yerine agac dikilsin."})
training_data.append({"class":"siyaset", "sentence":"VANDALLiGiN,DESPOTLUGUN.FASiZMiN,SOMURGECiLiGiN,ATAiSTLiGiN DEGiSMEYEN KALESi iKi YUZLU AVRUPA"})
training_data.append({"class":"siyaset", "sentence":"Binali Yildirim oglu Hollanda da bulununan 3 sirketini kapatip protesto etsin"})
training_data.append({"class":"siyaset", "sentence":"Merkel'den Hollanda'ya ne dense bos. Avrupa menfaat derdine dustu."})
training_data.append({"class":"siyaset", "sentence":"BuTuN TuRK DusMANLARiNi ALMAN SOFRASiNiN KiRiNTiSi iLE BESLEYiP TuRKiYEYi DiZE GETiREMEZSiN KART GAVUR"})
training_data.append({"class":"siyaset", "sentence":"Almanya Basbakani Merkel'den Hollanda'ya"})
training_data.append({"class":"siyaset", "sentence":"İçişleri Bakanımız Sn. @suleymansoylu ile memleketim Samsun'dayız. 16 Nisan Halk Oylaması'nda #EVET yolunda hemşehrilerimizle buluşacağız."})
training_data.append({"class":"siyaset", "sentence":"Demokrasimizden bedenimize kadar her yönüyle daha sağlıklı olduğumuz bir Türkiye özlemiyle #14MartTıpBayramı kutlu olsun."})
training_data.append({"class":"siyaset", "sentence":"Başbakanımız ve Genel Başkanımız Sn. Binali Yıldırım ile Özel Röportaj, bu akşam 19:30'da HABERTÜRK, SHOW TV ve BLOOMBERG HT ortak yayınında"})
training_data.append({"class":"siyaset", "sentence":"Atatürk'ün ulusçuluk görüşünün temelinde tam bağımsızlık yatar. "})
training_data.append({"class":"siyaset", "sentence":"13 Mart 1283 Mustafa Kemal'in Harp Okulu'na giriş günü.Harp Okulu'nu imha eden FETO ve kapatanlar Allah cezanızı verecek inşallah"})
training_data.append({"class":"siyaset", "sentence":"Cumhurbaşkanı Erdoğan ATV-A Haber Ortak Yayınına Katıldı "})
training_data.append({"class":"siyaset", "sentence":"Sirkeci'de aracımız AKP'nin sürekli faaliyet gösterdiği meydana sokulmuyor... Kim yasakladı??? Tabi ki faşist Hollanda!!! Irkçı Avrupa!!!"})
training_data.append({"class":"siyaset", "sentence":"Hollanda yaptıklarını telafi edinceye kadar bazı siyasi yaptırım kararları alınmıştır."})
training_data.append({"class":"siyaset", "sentence":"Başbakan 6 Mart'ta bu sözleri söylemişken Hollanda ziyareti için 14 Mart sonrası niçin beklenmedi? Ülkemiz neden gerilimin ortasına sokuldu?"})
training_data.append({"class":"siyaset", "sentence":"Hadi CHP, HDP, FETÖ, PKK, PYD-YPG, DHKP-C, eli kanlı aydınlıkçılar itiraz ediyor da, Avrupa ülkelerine ne oluyor, onlar niye hopluyor?"})
training_data.append({"class":"siyaset", "sentence":"Fabrika ziyaretimizde işçi kardeşlerimizden çalışma koşullarına ilişkin bilgi aldık. Hükümetimizden taleplerini dinledik,kolaylıklar diledik"})
training_data.append({"class":"siyaset", "sentence":"Kara Harp Okulumuzun yeni eğitim ve öğretim sezonunu törenle başlattık. Vatan ve Millet sevdalısı gençlerimiz bugün ders başı yaptı."})


training_data.append({"class":"spor", "sentence":"Antalyaspor'un Besiktas karari G.Saraylilari kizdirdi"})
training_data.append({"class":"spor", "sentence":"futbol seven insan da biraz seydir"})
training_data.append({"class":"spor", "sentence":"Castillo acilen bencil futbol oynamayi birakip takim oyununa katkida bulunmasi gerekiyor.Bugun takim halinde cok kotu"})
training_data.append({"class":"spor", "sentence":"Sahada sadece rakibe ustunluk saglamak, iyi futbol yetmiyor, kesinlikle hakemleri de yenmemiz gerekli ki maci kazanalim"})
training_data.append({"class":"spor", "sentence":"Büyük Trabzonsporumuzun Büyük Taraftarı! Her daim yanımızda olduğunuz için teşekkürler"})
training_data.append({"class":"spor", "sentence":"Bilyoner KBL 20. Hafta Maç Sonucu: Galatasaray 75-70 Canik Belediye | Tebrikler"})
training_data.append({"class":"spor", "sentence":"13 Mart ‘96 aklımızda, o ses hala kulaklarımızda: “Kupa bizim, kupa bizim, kupa bizim!”"})
training_data.append({"class":"spor", "sentence":"Sahada sadece rakibe ustunluk saglamak, iyi futbol yetmiyor, kesinlikle hakemleri de yenmemiz gerekli ki maci kazanalim"})
training_data.append({"class":"spor", "sentence":"Hisset, paylaş, parçası ol... Beşiktaş JK Müzesi sporseverleri bekliyor."})
training_data.append({"class":"spor", "sentence":"Denizlispor Instagram hesabında ortam alev alev yanıyor."})
training_data.append({"class":"spor", "sentence":"Atiker Konyaspor Maçının Hazırlıkları Başladı "})
training_data.append({"class":"spor", "sentence":"Manchester City, Bayern'in 25 milyon euro değer biçtiği Joshua Kimmich'i kadrosuna katmak istiyor."})
training_data.append({"class":"spor", "sentence":"Tudor'dan sürpriz hamle! Yıldız futbolcu için"})


training_data.append({"class":"teror", "sentence":"bölgesinde başlayan operasyondan kısa bir görüntü. Helikopterler Atak helikopteridir."})
training_data.append({"class":"teror", "sentence":"Senden ala teror destekcisi mi olur şerefsiz. Senin ben tipine sicayim. Dumbelek gavat nazi bozuntusu yavşak. Takiyeci ! Inadina HAYIR lan!"})
training_data.append({"class":"teror", "sentence":"1 yıl once bolucu  teror orgutu pkk #Güvenpark 'ta otobus duragindaki vatandaslarimizi bombayla katletti. Ruhlari şad olsun. #KahrolsunPkk"})
training_data.append({"class":"teror", "sentence":"Teror örgütü ilan ettikleri bir yapının, koskoca Türkiye devletinden daha etkili olduğunu ifade ediyr Bu ne kadar aciz olduğumuzun itirafıdr "})
training_data.append({"class":"teror", "sentence":"Avrupa 16 Nisan'da hayır çıksın diye ulkemize her kahpeliği yapmaya devam ediyor. Sözünü geçiremeyecekleri bir Türkiye'den çok korkuyorlar.."})
training_data.append({"class":"teror", "sentence":"TSK Yüksekova kırsalına düzenlenen hava harekatında 4 teröristin etkisiz hale getirildiğini ve 2 mevzinin imha edildiğini açıkladı."})
training_data.append({"class":"teror", "sentence":"İçişleri Bakanımız Süleyman Soylu Uludere kırsalında 11 teröristin öldürüldüğünü açıkladı."})
training_data.append({"class":"teror", "sentence":"Uludere sınır hattı Düğün Dağı-Karaçalı üs bölgeleri yakınlarında bugün 7 leş alınan bölgede devam eden çatışmada 13 leş daha alındı."})
training_data.append({"class":"teror", "sentence":"Uludere sınır hattında İHA ile tespit edilen 4 terörist öldürüldü."})
training_data.append({"class":"teror", "sentence":"Chp teror Orgutu Gibi Tavir Icinde almanya talimati Verdi Baykali Istiyor Ic savasa zemin Hazirliyir Chp Biz Haziriz Akilli Olun macerayi bi"})


training_data.append({"class":"haber", "sentence":"ÖSYM, KPSS sınav ücretlerini yeniden değerlendireceğini açıkladı.Olumlu bir gelişme.Sınav ücreti sembolik olmalı."})
training_data.append({"class":"haber", "sentence":"Hollanda polisinin köpek saldırısında yaralanan Türk vatandaşı yaşadıklarını anlattı "})
training_data.append({"class":"haber", "sentence":"TRT'de skandal: 'Psikoloji' programı yaptırılan kişi sahte doktor çıktı "})
training_data.append({"class":"haber", "sentence":"Şu üsttekiler, Türkiye'nin Fransa'ya ihraç ettiği başlıca ürünler. Alttakiler de onlardan aldıklarımız. Başka da diyeceğim yoktur."})
training_data.append({"class":"haber", "sentence":"Bakan Elvan son rakamı açıkladı: 82 milyarlık yatırım başvurusu"})
training_data.append({"class":"haber", "sentence":"ASELSAN'dan elektronik harp sistemleri için sözleşme"})
training_data.append({"class":"haber", "sentence":"Piyanist filminden bir kare değil, Halep'te gerçek hayat"})
training_data.append({"class":"haber", "sentence":"Akit yazarı: Hollanda konusunda sağduyulu hareket etmek gerek; Kemal Bey'in gazına gelmeyin!"})
training_data.append({"class":"haber", "sentence":"Metrobüste mendil satan bir çocuk yorgunluğa dayanamadı ve bir yolcunun dizine başını koyup uykuya daldı."})
training_data.append({"class":"haber", "sentence":"Bugünkü yorumum: Borsa, dolar ve altın..."})
training_data.append({"class":"haber", "sentence":"Bugün dünya üzerindeki 700 milyon 'kadın' 18 yaşından önce evlendirilmiş . Bu yazıda Bangladeş'in 'kadınları' anlatılıyor"})

def dataEkle(kategori):
    with open(kategori+'.txt', 'r') as myFile:
        satir = myFile.readline()
        while satir != '' and satir != None:
            obj = {"class":"{}".format(kategori), "sentence":"{}".format(satir)}
            training_data.append(obj)
            satir = myFile.readline()

dataEkle('haber')
dataEkle('teror')
dataEkle('siyaset')
dataEkle('spor')


stemmer = Stemmer()

def myStemmer(word):
    # kelime köklerini bulma işlemi yapılacak
    word = stemmer.stem(word)
    return word.lower()

def myTokenize(sentence):
    # cümleyi kelimelerine ayırıyor
    sentence = sentence.strip()
    return sentence.split(' ')

words = []
classes = []
documents = []
ignore_words = ['?']

# loop through each sentence in our training data
for pattern in training_data:
    # tokenize each word in the sentence
    w = myTokenize(pattern['sentence'])
    # add to our words list
    words.extend(w)
    # add to documents in our corpus
    documents.append((w, pattern['class']))
    # add to our classes list
    if pattern['class'] not in classes:
        classes.append(pattern['class'])

# stem and lower each word and remove duplicates
# words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]

words = [myStemmer(w) for w in words]
stemmer.close()

words = [w.replace('ğ', 'g') for w in words]
words = [w.replace('Ğ', 'g') for w in words]
words = [w.replace('Ç', 'c') for w in words]
words = [w.replace('ç', 'c') for w in words]
words = [w.replace('ü', 'u') for w in words]
words = [w.replace('Ü', 'u') for w in words]
words = [w.replace('Ü', 'u') for w in words]
words = [w.replace('Ö', 'o') for w in words]
words = [w.replace('ö', 'o') for w in words]
words = [w.replace('İ', 'i') for w in words]
words = [w.replace('I', 'i') for w in words]
words = [w.replace('ı', 'i') for w in words]
words = [w.replace('Ş', 's') for w in words]
words = [w.replace('ş', 's') for w in words]
words = [w.replace('\'', '') for w in words]
words = [w.replace('"', '') for w in words]
words = [w.replace('?', '') for w in words]
words = [w.replace('!', '') for w in words]
words = [w.replace('.', '') for w in words]
words = [w.replace(',', '') for w in words]
words = [w.replace(':', '') for w in words]
words = [w.replace(';', '') for w in words]
words = [w.replace('#', '') for w in words]
words = [w.replace('|', '') for w in words]
words = [w.replace('(', '') for w in words]
words = [w.replace(')', '') for w in words]
words = [w.replace('@', '') for w in words]
words = [w.replace('-', ' ') for w in words]

words = list(set(words))

# remove duplicates
classes = list(set(classes))

#print (len(documents), "documents")
#print (len(classes), "classes", classes)
#print (len(words), "unique stemmed words", words)


# create our training data
training = []
output = []
# create an empty array for our output
output_empty = [0] * len(classes)

# training set, bag of words for each sentence
for doc in documents:
    # initialize our bag of words
    bag = []
    # list of tokenized words for the pattern
    pattern_words = doc[0]

    # create our bag of words array
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    training.append(bag)
    # output is a '0' for each tag and '1' for current tag
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    output.append(output_row)

print documents[110]

# compute sigmoid nonlinearity
def sigmoid(x):
    output = 1 / (1 + np.exp(-x))
    return output


# convert output of sigmoid function to its derivative
def sigmoid_output_to_derivative(output):
    return output * (1 - output)


def clean_up_sentence(sentence):
    sentence_words = sentence.split(' ')
    return sentence_words


def train(X, y, hidden_neurons=10, alpha=1, epochs=50000, dropout=False, dropout_percent=0.5):
    print ("Training with %s neurons, alpha:%s, dropout:%s %s" % (
    hidden_neurons, str(alpha), dropout, dropout_percent if dropout else ''))
    print ("input matrix: %sx%s    Output matrix: %sx%s" % (len(X), len(X[0]), 1, len(classes)))
    np.random.seed(1)

    last_mean_error = 1
    # randomly initialize our weights with mean 0
    synapse_0 = 2 * np.random.random((len(X[0]), hidden_neurons)) - 1
    synapse_1 = 2 * np.random.random((hidden_neurons, len(classes))) - 1

    prev_synapse_0_weight_update = np.zeros_like(synapse_0)
    prev_synapse_1_weight_update = np.zeros_like(synapse_1)

    synapse_0_direction_count = np.zeros_like(synapse_0)
    synapse_1_direction_count = np.zeros_like(synapse_1)

    for j in iter(range(epochs + 1)):

        # Feed forward through layers 0, 1, and 2
        layer_0 = X
        layer_1 = sigmoid(np.dot(layer_0, synapse_0))

        if (dropout):
            layer_1 *= np.random.binomial([np.ones((len(X), hidden_neurons))], 1 - dropout_percent)[0] * (
            1.0 / (1 - dropout_percent))

        layer_2 = sigmoid(np.dot(layer_1, synapse_1))

        # how much did we miss the target value?
        layer_2_error = y - layer_2

        if (j % 10000) == 0 and j > 5000:
            # if this 10k iteration's error is greater than the last iteration, break out
            if np.mean(np.abs(layer_2_error)) < last_mean_error:
                print ("delta after " + str(j) + " iterations:" + str(np.mean(np.abs(layer_2_error))))
                last_mean_error = np.mean(np.abs(layer_2_error))
            else:
                print ("break:", np.mean(np.abs(layer_2_error)), ">", last_mean_error)
                break

        # in what direction is the target value?
        # were we really sure? if so, don't change too much.
        layer_2_delta = layer_2_error * sigmoid_output_to_derivative(layer_2)

        # how much did each l1 value contribute to the l2 error (according to the weights)?
        layer_1_error = layer_2_delta.dot(synapse_1.T)

        # in what direction is the target l1?
        # were we really sure? if so, don't change too much.
        layer_1_delta = layer_1_error * sigmoid_output_to_derivative(layer_1)

        synapse_1_weight_update = (layer_1.T.dot(layer_2_delta))
        synapse_0_weight_update = (layer_0.T.dot(layer_1_delta))

        if (j > 0):
            synapse_0_direction_count += np.abs(
                ((synapse_0_weight_update > 0) + 0) - ((prev_synapse_0_weight_update > 0) + 0))
            synapse_1_direction_count += np.abs(
                ((synapse_1_weight_update > 0) + 0) - ((prev_synapse_1_weight_update > 0) + 0))

        synapse_1 += alpha * synapse_1_weight_update
        synapse_0 += alpha * synapse_0_weight_update

        prev_synapse_0_weight_update = synapse_0_weight_update
        prev_synapse_1_weight_update = synapse_1_weight_update

    now = datetime.datetime.now()

    # persist synapses
    synapse = {'synapse0': synapse_0.tolist(), 'synapse1': synapse_1.tolist(),
               'datetime': now.strftime("%Y-%m-%d %H:%M"),
               'words': words,
               'classes': classes
               }
    synapse_file = "synapses.json"

    with open(synapse_file, 'w') as outfile:
        json.dump(synapse, outfile, indent=4, sort_keys=True)
    print ("saved synapses to:", synapse_file)

def run():
    #giriş verisi X = tüm cümlelerin bag of words vektörünün dizisi
    X = np.array(training)
    #çıkış verisi y = her cümlenin bow için karşılığı olan toplam class dizisi
    y = np.array(output)

    start_time = time.time()

    train(X, y, hidden_neurons=10, alpha=0.1, epochs=50000, dropout=True, dropout_percent=0.01)

    #geçen süre
    elapsed_time = time.time() - start_time
    print ("processing time:", elapsed_time, "seconds")




#run()