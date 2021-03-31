import random #metine bakılarak yazılma durumunda, rastgele bir metin seçmesi için "random" modülünü ekledik.
import datetime #başlama ve bitiş zamanını alarak yazım esnasında geçen zamanı bulmak için "datetime" modülünü ekledik.

#Metin mi seçeceksin, kendin mi yazı yazacaksın? 
baslangic = input("Metin ile mi çalışmak istersiniz yoksa kendiniz mi birşeyler yazacaksınız? Seçiniz(Metin/Kendim/KURALLAR): ")
baslangic = baslangic.upper()

############################################
metin1 = "\n\nDil kişinin duygularını açıklamasını, diğer kişilerle yakınlaşıp bağlantı kurmasını sağlar. Bütün milletleri var eden, onların sürekliliğini sağlayan son derece önemli unsurlardan biride dildir. Dil bir medeniyet olayıdır ancak bir medeniyetin kurduğu dil başka bir medeniyetin düşündüklerini söyleyemez. Söylemeye de yetmez. Kaderciliğin hakim olduğu en hayati olaylarla, din buyruklarının iç içe bulunduğu ve tenkitçi düşünceye de yer vermeyen bir medeniyetten uzaklaşılmıştır. Bunun yerine din ile devlet işlerinin birbirinden ayrıldığı hür ve ilmi düşünme imkanlarının bulunduğu tenkitçi düşünceyle yeniliklere sürekli açık olan bir medeniyete geçilmiştir. Türk milleti ülkesinin yüksek bağımsızlığını korumasını bildiği gibi dilini de yabancı diller boyunduruğundan kurtararak medeni dünyadaki yerini sağlayamamış olsaydı cumhuriyetimizin sürekliliği de tehlikeye düşebilirdi. Dilin milli ve zengin olması milli duygunun gelişmesinde başlıca etkendir. Türk dili dillerin en gelişmişlerinden ve en zenginlerindendir. Artık konuşurken ve yazarken kullandığımız dil ortaktır. Bu ortaklık her an her yerde ve her şekilde anlaşabilmemizi ve okuyup yazmada güçlük çekmememizi de sağlamıştır. Dilimiz gelişmiştir ve gelişecektir."           "Borçlu, diğer fesih sebepleri yanında ihaleye fesat karıştırıldığını da iddia ederek ihalenin feshi istemiyle icra mahkemesine başvurmuş, mahkemece ihale salonuna teminat yatırarak katılan kişiler dışında kimsenin alınmadığı, ihalede aleniyet ilkesine uyulmadığı kabul edilerek yapılan ihalenin feshine karar verildiği anlaşılmıştır. İhalenin amacına ulaşmasını, malın gerçek değerinde satılmasını, ihalenin sağlıklı ve normal şartlarda yapılmasını engelleyici, dürüstlük kuralları ile bağdaşmayan davranışlarda bulunulması ve ihaleye katılıma engel olunması ihaleye fesat niteliğindedir. İhaleye katılmak isteyenlerin teminat yatırması zorunlu olup, teminat yatırmayanların ihale mahallinde ihalenin sağlıklı şekilde yürütülmesini engelleyecek tavırda bulunmaları halinde icra müdürü gerekli tedbirleri ve önlemleri alabilir. Somut olayda icra müdür yardımcısının ihalenin sağlıklı şekilde yürütülmesini sağlamak amacıyla teminat yatırmayanları ihale salonu dışına çıkarmasında engel bir durum yoktur. Kaldı ki tanık olarak beyanına başvurulan polis memurlarının ifadelerine göre ihale yapılan yerin kapısının açık olduğu anlaşılmıştır. O halde mahkemece, borçlunun şikayet dilekçesinde ihaleye fesat sebebi olarak ileri sürdüğü vakıalara ilişkin hususlar ile diğer fesih nedenleri ile ilgili değerlendirme yapılarak oluşacak sonuca göre bir karar verilmesi gerekirken, şikayet dilekçesinde ileri sürülmeyen aleniyet ilkesi ihlal edildiği gerekçesiyle ihalenin feshine karar verilmesi isabetsizdir."
metin2 = "\n\nBorçlu, diğer fesih sebepleri yanında ihaleye fesat karıştırıldığını da iddia ederek ihalenin feshi istemiyle icra mahkemesine başvurmuş, mahkemece ihale salonuna teminat yatırarak katılan kişiler dışında kimsenin alınmadığı, ihalede aleniyet ilkesine uyulmadığı kabul edilerek yapılan ihalenin feshine karar verildiği anlaşılmıştır. İhalenin amacına ulaşmasını, malın gerçek değerinde satılmasını, ihalenin sağlıklı ve normal şartlarda yapılmasını engelleyici, dürüstlük kuralları ile bağdaşmayan davranışlarda bulunulması ve ihaleye katılıma engel olunması ihaleye fesat niteliğindedir. İhaleye katılmak isteyenlerin teminat yatırması zorunlu olup, teminat yatırmayanların ihale mahallinde ihalenin sağlıklı şekilde yürütülmesini engelleyecek tavırda bulunmaları halinde icra müdürü gerekli tedbirleri ve önlemleri alabilir. Somut olayda icra müdür yardımcısının ihalenin sağlıklı şekilde yürütülmesini sağlamak amacıyla teminat yatırmayanları ihale salonu dışına çıkarmasında engel bir durum yoktur. Kaldı ki tanık olarak beyanına başvurulan polis memurlarının ifadelerine göre ihale yapılan yerin kapısının açık olduğu anlaşılmıştır. O halde mahkemece, borçlunun şikayet dilekçesinde ihaleye fesat sebebi olarak ileri sürdüğü vakıalara ilişkin hususlar ile diğer fesih nedenleri ile ilgili değerlendirme yapılarak oluşacak sonuca göre bir karar verilmesi gerekirken, şikayet dilekçesinde ileri sürülmeyen aleniyet ilkesi ihlal edildiği gerekçesiyle ihalenin feshine karar verilmesi isabetsizdir. Bu itibarla, temyiz itirazlarının kabulü ile mahkeme kararının yukarıda yazılı nedenlerle bozulmasına, peşin alınan harcın istek halinde iadesine, ilamın tebliğinden itibaren on gün içinde karar düzeltme yolu açık olmak üzere, oybirliği ile karar verildi. Borçlu, diğer fesih sebepleri yanında ihaleye fesat karıştırıldığını da iddia ederek ihalenin feshi istemiyle icra mahkemesine başvurmuş, mahkemece ihale salonuna teminat yatırarak katılan kişiler dışında kimsenin alınmadığı, ihalede aleniyet ilkesine uyulmadığı kabul edilerek yapılan ihalenin feshine karar verildiği anlaşılmıştır. İhalenin amacına ulaşmasını, malın gerçek değerinde satılmasını, ihalenin sağlıklı ve normal şartlarda yapılmasını engelleyici, dürüstlük kuralları ile bağdaşmayan davranışlarda bulunulması ve ihaleye katılıma engel olunması ihaleye fesat niteliğindedir. İhaleye katılmak isteyenlerin teminat yatırması zorunlu olup, teminat yatırmayanların ihale mahallinde ihalenin sağlıklı şekilde yürütülmesini engelleyecek tavırda bulunmaları halinde icra müdürü gerekli tedbirleri ve önlemleri alabilir. Somut olayda icra müdür yardımcısının ihalenin sağlıklı şekilde yürütülmesini sağlamak amacıyla teminat yatırmayanları ihale salonu dışına çıkarmasında engel bir durum yoktur."
metin3 = "\n\nBilhassa kamu desteğine ihtiyaç duyan alanlardaki yatırımlara, ekonominin uzun vadede potansiyelini artırmaya yönelik tedbirlere ve verilen takvim çerçevesinde programların tamamlanabilmesi ihtimaline odaklanılmalıdır. Yapılan yatırımlar karşısında sağlanacak değere odaklanılmalıdır. Bu değerin artırılması kapsamında özel sektörün insan kaynakları yatırımları ve altyapı konusundaki rolüne dikkat edilmelidir. Proje seçimi, değerlendirmesi, tasarım ve uygulama yöntemlerine dikkat edilmelidir. Bu kapsamda daha rekabeti teşvik edecek proje seçim tekniklerine, ihtiyaçların tespiti için daha sistematik tekniklere, ihtiyaçlara yönelik olarak ısmarlama paketlere ve tedarikte daha esnek metotlara önem verilmelidir. Tedbir düzeyinde göstergeler eksik olup, ayrıca bölgelerarası tedbirler için her İBBS 2 bölgesindeki gelişmeleri içeren bir açıklama bulunmalıdır. Ayrıca ilerleme raporlarında harcama tahminlerinde yapılan revizyonların sebepleri açıklanmalıdır. Aynı hedef grup için farklı alanlara tahsis edilen destekler çakışabilmektedir. Bilhassa kamu desteğine ihtiyaç duyan alanlardaki yatırımlara, ekonominin uzun vadede potansiyelini artırmaya yönelik tedbirlere ve verilen takvim çerçevesinde programların tamamlanabilmesi ihtimaline odaklanılmalıdır. Yapılan yatırımlar karşısında sağlanacak değere odaklanılmalıdır. Bu değerin artırılması kapsamında özel sektörün insan kaynakları yatırımları ve altyapı konusundaki rolüne dikkat edilmelidir. Proje seçimi, değerlendirmesi, tasarım ve uygulama yöntemlerine dikkat edilmelidir. Bu kapsamda daha rekabeti teşvik edecek proje seçim tekniklerine, ihtiyaçların tespiti için daha sistematik tekniklere, ihtiyaçlara yönelik olarak ısmarlama paketlere ve tedarikte daha esnek metotlara önem verilmelidir. Tedbir düzeyinde göstergeler eksik olup, ayrıca bölgelerarası tedbirler için her İBBS 2 bölgesindeki gelişmeleri içeren bir açıklama bulunmalıdır. Ayrıca ilerleme raporlarında harcama tahminlerinde yapılan revizyonların sebepleri açıklanmalıdır. Aynı hedef grup için farklı alanlara tahsis edilen destekler çakışabilmektedir."
metin = [metin1,metin2,metin3] #metinleri rastgele çekebilmek için listeye ekledik, tombala çekilecek torba gibi düşünebilirsiniz...

#Bu metinler önümüze rastgele gelecek metinler olup, yanlış hatırlamıyorsan adalet bakanlığı katiplik yazım sınavlarında
#kullanılan metinler olup internette onlarca sınav metnine ulaşabilirsiniz...
#########################################

if baslangic == "METİN" or baslangic == "METIN":
    print("Birazdan karşınıza bir metin belirecek ve sizden hazır olduğunuzda bunu yazmanız beklenecek.Lütfen hazır olunuz.")
    seciliMetin = random.choice(metin) #rastgele metin getirecek kod
    girdi = input("Metni görmek ve yazmaya başlamak için ENTER basınız. ENTER bastığınız anda yazmaya başlayabilirsiniz.") 
    ilkAn = datetime.datetime.now() #yazmaya başlarkenki zaman
    print(seciliMetin)
    metinGiris = input("Yazınız: ") #gördüğünüz metni yazacağınız yer
    bittiAn = datetime.datetime.now() #metnin bitiş anındaki zaman
    metinBitti = input("ENTER...")
    sure = bittiAn - ilkAn # geçen süre
    print(f"sure: {sure}")
    
elif baslangic == "KENDİM" or baslangic == "KENDIM":
    print("Metninizi girmek için gelen ekranda ENTER basınız. Metninizi yazın ve ardından çift ENTER basarak programı bitirin ve sürenizi görün.")
    girdi = input("Yazmaya başlamak için ENTER basınız. ENTER bastığınız anda yazmaya başlayabilirsiniz.")
    ilkAn = datetime.datetime.now()
    metinGiris = input("Yazınız: ")
    bittiAn = datetime.datetime.now()
    metinBitti = input("ENTER...")
    sure = bittiAn - ilkAn
    print(f"sure: {sure}")
elif baslangic == "KURALLAR":
    print("METİN: Program size bir metin verecek ve bunu yazmanızı isteyecek. İzlemeniz gereken adımlar: \n1-ENTER\n2-ENTER+ENTER \n\n1 numaralı ENTER girişi ile beraber hemen yazmaya başlamalısınız...\n2- numaralı ENTER anlarında hızla çift ENTER tıklayarak yazma işlemini ve programı bitirip sürenizi görebilirsiniz. \n\nKENDİM: Enter basarak metninizi yazmaya başlayın ardından ENTER tuşu ile yazmayı bitirip aynı tuş ile sürenizi görün.")
else:
    pass