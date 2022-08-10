![nasıl?](https://raw.githubusercontent.com/ardauzunoglu/nasil/main/readme/nasil-readme.png)

nasıl? prosedürel veri içeren rehberlerde yer alan yönergeleri, rehber havuzundaki diğer rehberlerle eşleştirerek bir rehberde yer alan kompleks, anlaması zor veya uzman bilgisi gerektiren yönergeleri kullanıcının kolaylıkla tamamlamasını sağlamayı amaçlayan bir platformdur. 

[nasil.herokuapp.com](https://nasil.herokuapp.com)

# Kullanılan Veri Seti

nasıl? platformunun geliştirilmesinde kullanılan veri setleri temelde ikiye ayrılmaktadır: <br> 

1 - nasıl? platformunda içerik olarak kullanılan veri setleri: <br>
- wikihow-tr
- all-results

2 - nasıl? platformunun ve nasıl? platformunda içerik olarak kullanılan veri setlerinin geliştirilmesinde kullanılan veri setleri: <br>
- annotated-step-goal
- step2goal
- wikihow-icerik

## wikihow-tr

nasıl?'da yer alan rehberlerden oluşan wikihow-tr veri setine ulaşmak için [tıklayabilirsiniz]().

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

annotated-step-goal veri setine ulaşmak için [tıklayabilirsiniz]().

## step2goal
step2goal, wikihow-tr veri setinde yer alan her bir rehberdeki her bir adımın içerisinde bulunduğu rehber ile eşleştiği bir veri setidir. step2goal, reranking modelinin eğitimi sırasında kullanılmıştır.

step2goal veri setine ulaşmak için [tıklayabilirsiniz]().

## wikihow-icerik
wikihow-icerik, wikihow-tr veri setinin yalnızca kategori, yöntem, kısım ve adım bilgisi içeren daha kompakt bir versiyonudur. wikihow-icerik, wikihow-tr'den farklı olarak tüm rehberleri tek bir dosyada barındırmaktadır. wikihow-icerik, reranking modelinin eğitimi sırasında kullanılmıştır.

wikihow-icerik veri setine ulaşmak için [tıklayabilirsiniz]().

# Kullanılan Modeller

## En Yakın 30 Rehber Eldesi

annotated-step-goal veri seti üzerinde denenen çeşitli algoritmaların ve Sentence Transformer modellerinin performansları aşağıdaki gibidir:

<table>
  <tr>
    <td> </td>
    <td colspan="3">Dev</td>
    <td colspan="3">Train</td>
  </tr>
  <tr>
    <td>Model</td>
    <td>R@1</td>
    <td>R@10</td>
    <td>R@30</td>
    <td>R@1</td>
    <td>R@10</td>
    <td>R@30</td>
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
    <td>distiluse-base-multilingual-cased</td>
    <td>0.183</td>
    <td>0.282</td>
    <td>0.331</td>
    <td>0.073</td>
    <td>0.129</td>
    <td>0.158</td>
  </tr>
  <tr>
    <td>BERTurk Sentence Transformer</td>
    <td>0.496</td>
    <td>0.640</td>
    <td>0.667</td>
    <td>0.262</td>
    <td>0.423</td>
    <td>0.499</td>
  </tr>
  <tr>
    <td>Fine-tuned BERTurk Sentence Transformer</td>
    <td>0.640</td>
    <td>0.760</td>
    <td>0.782</td>
    <td>0.337</td>
    <td>0.562</td>
    <td>0.651</td>
  </tr>
</table>

R@1 = Gold rehberin, elde edilen otuz rehber arasında birinci sırada olma oranı. <br>
R@10 = Gold rehberin, elde edilen otuz rehber arasında ilk on sırada olma oranı. <br>
R@30 = Gold rehberin, elde edilen otuz rehber arasında olma oranı. <br>
