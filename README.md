![nasıl?](https://raw.githubusercontent.com/ardauzunoglu/nasil/main/readme/nasil-readme.png)

nasıl? prosedürel veri içeren rehberlerde yer alan yönergeleri, rehber havuzundaki diğer rehberlerle eşleştirerek bir rehberde yer alan kompleks, anlaması zor veya uzman bilgisi gerektiren yönergeleri kullanıcının kolaylıkla tamamlamasını sağlamayı amaçlayan bir platformdur. 

[na-sil.herokuapp.com](https://na-sil.herokuapp.com)

# README.md İçeriği

[Kullanılan Veri Seti](#kullanılan-veri-seti) <br>
[Kullanılan Modeller](#kullanılan-modeller) <br>
[nasıl? Websitesi](#nasıl-websitesi) <br>
[Geliştirici Ekip](#geliştirici-ekip) <br>

# Örnek

![ornek](https://raw.githubusercontent.com/ardauzunoglu/nasil/main/readme/ornek.gif)

# Kullanılan Veri Seti

nasıl? platformunun geliştirilmesinde kullanılan veri setleri temelde ikiye ayrılmaktadır: <br> 

1 - nasıl? platformunda içerik olarak kullanılan veri setleri: <br>
- wikihow-tr
- all-results

2 - nasıl? platformunun ve nasıl? platformunda içerik olarak kullanılan veri setlerinin geliştirilmesinde kullanılan veri setleri: <br>
- annotated-step-goal
- step2goal
- wikihow-icerik
- tdd-corpus

## wikihow-tr

nasıl?'da yer alan rehberlerden oluşan wikihow-tr veri setine ulaşmak için [tıklayabilirsiniz](https://drive.google.com/drive/folders/1dk9GKE58Q6lv2R0Dsj5lxnB2TGQ8W7Hy?usp=sharing).

### Veri Seti Eldesi
wikihow-tr, [Wikihow corpus](https://drive.google.com/file/d/1ufBrqYoHTFoBtSxwYks6i_iR9HqmobxR/view) veri setinin "Cars and Other Vehicles" (Arabalar ve Diğer Araçlar), "Computers and Electronics" (Bilgisayar ve Elektronik), "Health" (Sağlık), "Hobbies and Crafts" (Hobiler ve El Sanatları), "Home and Garden" (Ev ve Bahçe), "Pets and Animals" (Evcil Hayvanlar ve Hayvanlar) kategorilerinde yer alan rehberlerin [ÇeVeri](https://github.com/ardauzunoglu/ceveri) aracılığıyla Türkçeleştirilmesi sonucu elde edilmiştir.

### Veri Seti Künyesi
wikihow-tr toplamda 50112 adet rehber barındırmakta olup toplamda 899MB yer kaplamaktadır. Veri setinde yer alan kategorilerin barındırdıkları rehber sayıları aşağıdaki gibidir:

| Arabalar ve Diğer Araçlar | Bilgisayar ve Elektronik | Sağlık | Hobiler ve El Sanatları | Ev ve Bahçe  | Evcil Hayvanlar ve Hayvanlar | 
| ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- |
| 2350 | 15416 | 10310 | 8800 | 9461 | 3775 |

wikihow-tr kapsamında her bir rehber ayrı bir json dosyasında tutulmaktadır. json dosyasında rehbere ait rehber başlığı, rehber bağlantısı, rehber açıklaması, kategori hiyerarşisi, rehberin yazarına ait bilgiler, rehberin en son güncellenme bilgisi, rehberin görüntülenme sayısı, rehbere ait oylama, rehbere yönelik videoya ait bağlantı, ilgili rehberlerin başlıkları ve bu rehberlere ait görseller, rehbere yönelik uyarılar ve tavsiyeler, kullanıcılar tarafından sorulan sorular ve bu sorulara verilen yanıtlar, rehber içerisinde yapılan referanslara ait bağlantılar, rehberin diğer dillerde yer alan çevirilerine ait bağlantılar ve bu çevirilerin başlıkları, ve de en önemlisi rehberde geçen yöntemler, kısımlar ve adımlar yer almaktadır. 

[Örnek bir dosya](https://drive.google.com/file/d/16-RK7zBTQhI5diMzjIxIeuFF6nAs831_/view?usp=sharing).

## all-results

all-results, wikihow-tr veri setinde yer alan tüm rehberlerdeki tüm adımlar için sentence transformer kullanılarak en yakın 30 rehberin retrieve edilmesi sonrası eğittiğimiz reranking modeli ile bu 30 rehberin yeniden sıralanması sonucu elde edilmiştir ve wikihow-tr veri setinde yer alan tüm rehberlerdeki tüm adımlara ait eşleşme bilgilerini içermektedir. 

all-results veri setine ulaşmak için [tıklayabilirsiniz]().

## annotated-step-goal
annotated-step-goal, wikihow-tr veri seti içerisinde yer alan ve wikihow editörleri tarafından gerçekleştirilmiş adım & rehber eşleşmelerini barındırmaktadır. annotated-step-goal, reranking modelinin eğitimi sırasında kullanılmıştır.

annotated-step-goal veri setine ulaşmak için [tıklayabilirsiniz](https://drive.google.com/file/d/1tl7ejoSFckjPihhVigghxBfzVMrmUo8U/view?usp=sharing).

## step2goal
step2goal, wikihow-tr veri setinde yer alan her bir rehberdeki her bir adımın içerisinde bulunduğu rehber ile eşleştiği bir veri setidir. step2goal, reranking modelinin eğitimi sırasında kullanılmıştır.

step2goal veri setine ulaşmak için [tıklayabilirsiniz](https://drive.google.com/file/d/1LXicnsaEpTHD-9qMUWo4n_atv59XtRuG/view?usp=sharing).

## wikihow-icerik
wikihow-icerik, wikihow-tr veri setinin yalnızca kategori, yöntem, kısım ve adım bilgisi içeren daha kompakt bir versiyonudur. wikihow-icerik, wikihow-tr'den farklı olarak tüm rehberleri tek bir dosyada barındırmaktadır. wikihow-icerik, reranking modelinin eğitimi sırasında kullanılmıştır.

wikihow-icerik veri setine ulaşmak için [tıklayabilirsiniz](https://drive.google.com/file/d/1GQKs_JbJb6ZfWiz6XYo_KjnlaQDm2byp/view?usp=sharing).

## TDD-Corpus

mC4 Türkçe Corpus, OSCAR Türkçe Corpus ve SketchEngine Türkçe Corpus'un birleşiminden kopya dokümantasyonların temizlenmesi sonucu elde edilen ham corpus'tur. Türkçe Sentence Transformer modelinin eğitiminde kullanılmıştır.

TDD-Corpus veri setine ulaşmak için [tıklayabilirsiniz](https://data.tdd.ai/#/69212ac7-a7e3-4405-8a10-b0bf7feb54dd).

# Kullanılan Modeller

Adım & rehber eşleşmesi iki basamakta gerçekleştirilmektedir. İlk basamak sentence transformer kullanarak wikihow-tr veri setinde yer alan her bir adım için en yakın 30 rehberin (cosine_similarity_score değerinin en yüksek olduğu 30 rehber) elde edilmesiyken ikinci basamak elde edilen 30 rehberin reranking modelinin kullanılmasıyla yeniden sıralanmasıdır.

## En Yakın 30 Rehber Eldesi

wikihow-tr veri setinde yer alan her bir adım için sentence transformer kullanılarak en yakın 30 rehber elde edilmektedir. Bu süreçte öncelikle wikihow-tr veri setinde yer alan rehber başlıkları sentence transformer kullanılarak encode edilerek embeddinglere dönüştürülmekte, devamında ise FAISS kütüphanesi kullanılarak her bir adım için anlamsal benzerlik araması (semantic similarity search) gerçekleştirilmektedir. Bu arama sonucunda en yüksek cosine_similarity_score değerine sahip 30 rehber bulunmaktadır. En yakın 30 rehber eldesi işleminin gerçekleştirildiği kodu görmek isterseniz [en30-rehber-eldesi.ipynb](https://github.com/ardauzunoglu/nasil/blob/main/en30_rehber_eldesi.ipynb) dosyasını ziyaret edebilirsiniz.

annotated-step-goal veri seti üzerinde denenen çeşitli algoritmaların ve Sentence Transformer modellerinin performansları aşağıdaki gibidir:

<table>
  <tr>
    <td> </td>
    <td align="center" colspan="3">Dev</td>
    <td align="center" colspan="3">Train</td>
  </tr>
  <tr>
    <td>Model</td>
    <td align="center">R@1</td>
    <td align="center">R@10</td>
    <td align="center">R@30</td>
    <td align="center">R@1</td>
    <td align="center">R@10</td>
    <td align="center">R@30</td>
  </tr>
  <tr>
    <td>BM25L</td>
    <td>0.116</td>
    <td>0.267</td>
    <td>0.331</td>
    <td>0.034</td>
    <td>0.108</td>
    <td>0.142</td>
  </tr>
  <tr>
    <td>BM25Opaki</td>
    <td>0.128</td>
    <td>0.269</td>
    <td>0.331</td>
    <td>0.041</td>
    <td>0.112</td>
    <td>0.146</td>
  </tr>
  <tr>
    <td>BM25+</td>
    <td>0.131</td>
    <td>0.269</td>
    <td>0.331</td>
    <td>0.041</td>
    <td>0.112</td>
    <td>0.145</td>
  </tr>
  <tr>
    <td>BERTurk (Zero-shot)</td>
    <td>0.165</td>
    <td>0.293</td>
    <td>0.320</td>
    <td>0.065</td>
    <td>0.134</td>
    <td>0.155</td>
  </tr>
  <tr>
    <td>distiluse-base-multilingual-cased</td>
    <td>0.183</td>
    <td>0.282</td>
    <td>0.331</td>
    <td>0.073</td>
    <td>0.129</td>
    <td>0.158</td>
  </tr>
  <tr>
    <td>Türkçe Sentence Transformer</td>
    <td>0.496</td>
    <td>0.640</td>
    <td>0.667</td>
    <td>0.262</td>
    <td>0.423</td>
    <td>0.499</td>
  </tr>
  <tr>
    <td>Fine-tuned Türkçe Sentence Transformer</td>
    <td><strong>0.640</strong></td>
    <td><strong>0.760</strong></td>
    <td><strong>0.782</strong></td>
    <td><strong>0.337</strong></td>
    <td><strong>0.562</strong></td>
    <td><strong>0.651</strong></td>
  </tr>
</table>

R@1 = Gold rehberin, elde edilen otuz rehber arasında birinci sırada olma oranı. <br>
R@10 = Gold rehberin, elde edilen otuz rehber arasında ilk on sırada olma oranı. <br>
R@30 = Gold rehberin, elde edilen otuz rehber arasında olma oranı. <br>

### Türkçe Sentence Transformer Eğitimi

En yakın 30 rehber eldesi aşamasında kullanılması amacıyla Türkçe sentence transformer eğitilmiştir. Eğitilen Türkçe sentence transformer modeli hem literatürde bulunan Türkçe sentence transformer açığını kapatmaktadır hem de en yakın 30 rehber eldesinde çoklu dilli sentence transformer modellerine ve BM25 algoritmasının varyasyonlarına kıyasla yüksek performans sergilemektedir. 

![Türkçe Sentence Transformer Modeli](https://raw.githubusercontent.com/ardauzunoglu/nasil/main/readme/Türkçe-Sentence-Transformer.png)

Türkçe Sentence Transformer'ın eğitiminde TDD'den alınan 240GB'lık [TDD-Corpus](https://data.tdd.ai/#/69212ac7-a7e3-4405-8a10-b0bf7feb54dd) veri seti kullanılmıştır. TDD-Corpus'ta yer alan dokümasyonlar, öncelikle cümlelere ayrılmış ve devamında Python'ın `random` kütüphanesi kullanılarak rastgele cümle çiftleri oluşturulmuştur. SNLI-tr ve MNLI-tr kullanılarak fine-tune edilen ConvBERTurk modelinin kullanılmasıyla, oluşturulan cümle çiftleri "entailment", "contradiction" ve "neutral" olmak üzere üç seçenek arasından etiketlenmiştir. Daha sonrasında confidence score kullanılarak filtreme yapılmış ve düşük confidence score'una sahip cümle çiftleri elenmiştir. Filtreme sonrası elde kalan 80 milyon cümle çifti ile birlikte ConvBERTurk modeli kullanılarak Türkçe Sentence Transformer modeli eğitilmiştir. Eğitim aşamasında [training_nli_v2.py](https://github.com/UKPLab/sentence-transformers/blob/master/examples/training/nli/training_nli_v2.py) ve [training_stsbenchmark_continue_training.py](https://github.com/UKPLab/sentence-transformers/blob/master/examples/training/sts/training_stsbenchmark_continue_training.py) dosyaları kullanılmıştır. Eğitilen Türkçe Sentence Transformer'ın SNLI-tr ve MNLI-tr üzerinde fine-tune edilmesinin en yakın 30 rehber eldesindeki performansını iyileştirdiği gözlemlenmiştir.  

### Türkçe Sentence Transformer Model Kartı
**Base model**: ConvBERTurk <br>
**Max sequence length**: 256 <br>
**Dimensions**: 768 <br>
**Score functions**: dot-product, cosine similarity, euclidean distance <br>
**Size**: 420MB <br>
**Pooling**: Mean pooling <br>
**Loss**: Contrastive loss <br>
**Data**: TDD-Corpus'un işlenmesiyle elde edilen 80 milyon cümle çifti <br>


Türkçe Sentence Transformer modeline ulaşmak için [tıklayabilirsiniz](https://drive.google.com/drive/folders/1eEBsFnCvD1wxo3q5uPNhcKo4W8dhvIk3?usp=sharing).

## En Yakın 30 Rehberin Yeniden Sıralanması

Anlamsal benzerlik araması sonucu elde edilen en yakın 30 rehber eğittiğimiz reranking modeli ile yeniden sıralanmaktadır. 

annotated-step-goal veri seti üzerinde gerçekleştirilen yeniden sıralama işleminin sağladığı iyileştirme aşağıdaki gibidir (gold rehber elde edilen en yakın 30 rehber arasında yer almıyorsa 30. sıradaki rehber ile değiştirilmiştir):
<table>
  <tr>
    <td> </td>
    <td align="center" colspan="3">Dev</td>
    <td align="center" colspan="3">Train</td>
  </tr>
  <tr>
    <td></td>
    <td align="center">R@1</td>
    <td align="center">R@10</td>
    <td align="center">R@30</td>
    <td align="center">R@1</td>
    <td align="center">R@10</td>
    <td align="center">R@30</td>
  </tr>
  <tr>
    <td>Yeniden Sıralama Öncesi</td>
    <td>0.640</td>
    <td>0.760</td>
    <td>1</td>
    <td>0.337</td>
    <td>0.562</td>
    <td>1</td>
  </tr>
  <tr>
    <td>Yeniden Sıralama Sonrası</td>
    <td>0.756</td>
    <td>0.973</td>
    <td>1</td>
    <td>0.776</td>
    <td>0.974</td>
    <td>1</td>
  </tr>
  <tr>
    <td>Fark</td>
    <td><strong>+0.116 (+18%)</strong></td>
    <td><strong>+0.213 (+28%)</strong></td>
    <td><strong>+0 (+0%)</strong></td>
    <td><strong>+0.439 (+130%)</strong></td>
    <td><strong>+0.412 (+73%)</strong></td>
    <td><strong>+0 (+0%)</strong></td>
  </tr>
</table>

### Reranking Modelinin Eğitimi

Zaman tasarrufu sağlamakla birlikte, rehber başlıklarını ve rehberlerde yer alan adımları ayrı ayrı encode etmek adımlardaki bilgilerin başlıkların encode edilmesinde kullanılamaması nedeniyle optimal performansı sağlayamamaktadır. Bu sebepten ötürü, her bir adımı elde edilen en yakın 30 rehberdeki her bir rehberle birleştirdikten sonra BERTurk modeline besleyerek adım-rehber çiftlerini encode ediyoruz. Adım-rehber çiftinin oluşturulmasında aşağıdaki formül kullanılmaktadır:

`[CLS] bglm [AD] adım [RE] rehber [SEP]`

Formülde yer alan [AD] ve [RE] tokenleri, pretrained BERTurk modelinde rezerve edilen özel tokenlerdir. [AD] tokeni adımın başlangıcını, [RE] tokeni ise rehberin başlangıcını simgelemektedir. bglm, bağlam bilgisi olup bir adıma yönelik bağlam bilgisi içermektedir. Bağlam bilgisi, adımdan önce ya da sonra gelen adımlar veya adımın yer aldığı rehberin başlığı olabilir. 

İkinci basamakta hesaplanan benzerlik skoru aşağıdaki formül kullanılarak elde edilmektedir:

<img src="https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BYellow%7Dsim_2%20%3D%20proj%28%5Cmu_c%28s%2C%20g_i%29%29%20&plus;%20%5Clambda%20sim_1%28s%2C%20g_i%29%7D"/>

<img src="https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BYellow%7D%20%5Cmu_c%7D"/> → BERTurk modeli, çıktı olarak embedding vermektedir.

<img src="https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BYellow%7D%20proj%7D"/> → d-boyutlu bir vektör alıp onu <img src="https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BYellow%7D%20W%20%5Cepsilon%20R%5E%7Bd%20x%201%7D%7D"/> ağırlık matrix'ine sahip bir skalere dönüştüren fonksiyon.

<img src="https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BYellow%7D%20%5Clambda%20%7D"/> → ilk basamaktaki benzerlik skorunun ağırlığı.

<img src="https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BYellow%7D%20s%20%7D"/> → adım.

<img src="https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BYellow%7D%20g_i%20%7D"/> → en yakın 30 rehber arasındaki i. rehber.

Hem <img src="https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BYellow%7D%20%5Clambda%20%7D"/> hem de <img src="https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BYellow%7D%20W%20%7D"/> back-propagation ile optimize edilen değerlerdir.

Eğitimde kullanılan loss fonksiyonu aşağıdaki formül ile hesaplanmaktadır:

<img src="https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BYellow%7D%20-%20log%28softmax%28%5Cfrac%7Bsim_2%28s%2C%20g_i%29%7D%7B%5Csum%20%28g_j%20%5Cepsilon%20C%28s%29%29%20sim_2%28s%2C%20g_i%29%7D%29%29%7D"/>

<img src="https://latex.codecogs.com/svg.latex?%7B%5Ccolor%7BYellow%7D%20C%28s%29%7D"/> → elde edilen en yakın 30 rehber.

Reranking modelinin eğitiminde üç farklı veri setinden (step2goal, wikihow-icerik, ve annotated-step-goal) faydalanılmaktadır. Reranking modelinin eğitimi (train.py) ve kullanımı (inference.py) için kullanılan kod dosyalarına bakmak için [reranking](https://github.com/ardauzunoglu/nasil/tree/main/reranking) klasörüne göz atabilirsiniz.

### Reranking Modelinin Kullanımı

Reranking modeli, wikihow-tr veri setinde yer alan tüm adımlar için en yakın 30 rehber eldesi gerçekleştirildikten sonra kullanılmaktadır. Türkçe sentence transformer ile elde edilen 30 rehberi, adıma ait bağlam bilgisi (adımdan önce ya da sonra gelen adım, veya adımın içinde bulunduğu rehberin başlığı) kullanarak yeniden sıralamaktadır, böylece daha başarılı bir eşleşme gerçekleştirilmektedir. 

En yakın 30 rehber eldesi işleminin gerçekleştirildiği kodu görmek isterseniz [yeniden_sıralama.ipynb](https://github.com/ardauzunoglu/nasil/blob/main/yeniden_sıralama.ipynb) dosyasını ziyaret edebilirsiniz.

Reranking modelini indirmek için [tıklayabilirsiniz](https://drive.google.com/file/d/1-IYkVzdWwPk0BXmMfV66PoYBkpkFWtc-/view?usp=sharing).

# nasıl? Websitesi

## Geliştirme

nasıl? websitesi frontend'de HTML5, CSS3 ve JavaScript kullanırken backend'de Python'ın Flask kütüphanesinden faydalanmaktadır. wikihow-tr veri setinde bulunan rehberler, boto3 kütüphanesi kullanılarak Amazon Web Services (AWS)'in ilk 5GB için ücretsiz sunduğu S3 platformunda depolanmaktadır. Çalışma akışı, repository'deki app.py dosyası ve templates klasörü altındaki .html dosyaları üzerinden yürümekte olup Heroku platformuna deploy edilmiştir.

## Kullanım

**Adım 1**: Ana sayfaya gidin.<br>
[na-sil.herokuapp.com](https://na-sil.herokuapp.com) adresi üzerinden ana sayfaya gidin.

**Adım 2**: Takip etmek istediğiniz rehberi aratın.<br>
Ana sayfadaki arama çubuğunu kullanarak takip etmek istediğiniz rehberi veya ihtiyacınız olan bir rehbere ait birkaç anahtar kelimeyi aratabilirsiniz. nasıl? aradığınız rehberi veya aradığınız anahtar kelimelerin yer aldığı rehberleri size sunacaktır.

**Adım 3**: Rehberi takip edin.<br>
Yaptığınız arama sonucunda karşınıza çıkan rehberlerden isteğinize en uygun olanı seçin ve seçtiğiniz rehberi takip edin.

**Adım 4**: Anlamadığınız adımın üzerine tıklayın.
Rehberi takip ederken nasıl yapılacağını anlamadığınız bir adım olursa bu adımın üzerine tıklayın. Böylece, nasıl?, size o adımla eşleştirdiği yeni rehberleri sunacaktır. Eşleştirilen rehberler arasından istediğiniz rehberi seçebilirsiniz. Anlamadığınız adımla ilgili seçtiğiniz rehberi takip ederek o adımı daha kolay bir şekilde, daha kısa bir zaman zarfında tamamlayarak takip ettiğiniz asıl rehbere dönebilirsiniz.

**Adım 5**: İsteğinizi gerçekleştirene kadar tekrar edin.
İsteğinizi gerçekleştirene, amacınıza ulaşana veya sorununuzu çözene dek 4. adımı tekrar edin. Gerçekleştirmeye çalıştığınız eylemi başarana (takip ettiğiniz asıl rehberi sonlandırana) dek anlamadığınız veya tamamlayamadığınız başka adımlar olursa 4. adımı ziyaret edin. Böylece vakit, para ve emek kaybetmeden, pek çok tarayıcı sekmesi açmadan, kısa süre içerisinde, düzenli bir şekilde rehberi tamamlayacaksınız.

## Hedefler
### Güncel Durum
nasıl?, güncel olarak tamamı WikiHow kaynağından olmak üzere 6 adet ana, 142 adet alt kategoriden toplamda 50 bin 112 adet rehber içermektedir.

### Gelecek Hedeflerimiz
**1 - Veri Tabanının Genişletilmesi**<br>
Veri tabanımıza yeni içerikler ekleyerek nasıl? platformunun sağladığı desteğin kapsamını genişletmeyi hedefliyoruz. Bu hedefimiz doğrultusunda öncelikli amacımız WikiHow kaynağında bulunan çeşitli kategorileri (örneğin Seyahat, Sporlar ve Fitness, vb.) Türkçeleştirerek veri tabanımıza kazandırmak, devamında ise WikiHow kaynağının dışına çıkarak yeni kaynaklara (örneğin Instructables, doityourself, IFixIt, vb.) yelken açmak ve veri tabanımızı giderek genişletmek.

**2 - Alt Sistemlerin Oluşturulması**<br>
nasıl?, geniş bir kategori havuzu kapsamında farklı kategorilerden pek çok sayıda rehberi her düzeyden bilgi seviyesine sahip kullanıcılar için daha anlaşılır, takip edilebilir ve tamamlanabilir hale getirmeyi amaçlamaktadır. Bu amaç doğrultusunda tüm rehberler ve adımlar tek bir havuza toplanmış olup birbirinden bağımsız iki kategoriden veyahut alandan iki rehber aynı süreçten geçmektedir. Veri tabanımızın giderek genişlemesiyle elde edeceğimiz yüksek miktarda Türkçe veri ile oluşturmayı planladığımız alt sistemler ile birlikte veri tabanımızı kategorilere/alanlara ayırıp, her bir kategoride/alanda uzmanlaşacak derin öğrenme modelleri eğitmeyi ve böylece "nasıl? - Okul", "nasıl? - Sağlık", "nasıl? - Mutfak" gibi alt hizmetler sunmayı amaçlıyoruz.

**3 - nasıl? - Görsel**<br>
Geliştirmeyi planladığımız "nasıl? - Görsel" eklentisi ile metin temelli bilgilerin aktarmada yetersiz kaldığı yönergeler için birer medya formu (ilk aşamada resim) üretmeyi ve böylece kullanıcılara çoklu-yönlü bilgi sunarak işlerini kolaylaştırmayı planlıyoruz.

# Geliştirici Ekip
Geliştirici Ekip: **Yayla** <br>
Takım Kaptanı: **Arda Uzunoğlu** → [Github](https://github.com/ardauzunoglu), [Twitter](https://twitter.com/ardauzunogluuu) <br>
Takım Danışmanı: **Gözde Gül Şahin** → [Github](https://github.com/gozdesahin), [Twitter](https://twitter.com/gozde_gul_sahin), [Website](https://gozdesahin.github.io) <br>
