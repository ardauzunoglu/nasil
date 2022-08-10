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
