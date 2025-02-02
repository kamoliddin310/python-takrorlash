# python-takrorlash

### Funksiyalar nima qiladi?

✔ Eng qimmat mahsulotni topish

✔ Eng arzon mahsulotni topish

✔ Berilgan turdagi mahsulotlarni chiqarish

✔ Narxi bo‘yicha saralash (o‘sish/kamayish tartibida)

✔ Yangi mahsulot qo‘shish va JSON faylga yozish


# Uyga Vazifa har bir mashqdan kamida 5 tadan bajaring

## Python Takrorlash

- **Tuple va list**
    1. Listda ism va familiyalar berilgan. Ushbu listdagi ma'lumotlarni **familiyasi** **bo'yicha** alfavit tartibida saralaydigan dastur yozing. (sort() metodini qo’llash mumkin emas)
        - Ismlar
            
            ```python
            Input:
             [
                'Otabek Karimov',
                'Javohir Abdullayev',
                'Xadicha Norqulova',
                'Madina Komilova',
                'Iskandar Rahmonov',
                'Fotima Ahmedova',
                'Sherzod Omonov',
                'Amir Saidov',
                'Xurshida Raximova',
                'Ravshan Tursunov',
                'Nigora Usmonova',
                'Bekzod Safarov',
                'Sardor Yo‘ldoshev',
                'Asliddin Oripov',
                'Bahodir Bobomurodov',
                'Tohir Mamadaliyev',
                'Muhabbat Xudoyberdiyeva',
                'Kamoliddin Fozilov',
                'Gulnoza Bozorova',
                'Zulfiya Obidova',
                'Sirojiddin To‘rayev',
                'Dilbar Xalilova',
                'Olim Qodirov',
                'Sevinch Saydullayeva',
                'Zokir Egamberdiyev',
                'Shahzod Norboev',
                'Muhammadbek Mahmudov',
                'Ruhsora Qosimova',
                'Alisher Yusupov',
                'Nasiba Qobilova',
                'Rustam Kenjaboyev',
                'Rahim Hakimov',
                'Shavkat Narziyev',
                'Feruza Tohirova',
                'Mohinur Azimova',
                'Suhrob Rasulov',
                'Dildora Abduraimova',
                'Umarxon Turg‘unov',
                'Kamol Sharipov',
                'Omina Xolmatova',
                'Habibulloh Saidov',
                'Sarvinoz Abdullayeva',
                'Abdulloh Fayzullayev',
                'Marjona Yoqubova',
                'Farhod Rasulov',
                'Nodir Norqulov',
                'Asilbek Zokirov',
                'Zebo Abdurahmonova',
                'Sherali Ismatov',
                'Abdulaziz Salimov',
                'Gulchehra Vohidova',
                'Muzaffar G‘aniyev',
                'Xolida O‘ktamova',
                'Elyor Rajabov',
                'Mironshoh Axmatov',
                'Sohiba Qo‘chqorova',
                'Shoira Turg‘unova',
                'Fayzullo Mamatov',
                'Ziyoda Xasanova',
                'Mansur Ergashov',
                'Akmal Abdurahmonov',
                'Karima Usmonova',
                'Dilnoza Salimova',
                'Ravshan Tohirov',
                'Baxtiyor Sobirov',
                'Gulhayo Karimova',
                'Nozima To‘raeva',
                'Husan Yusupov',
                'Raxima Rahimova',
                'Dilshod Toxirov',
                'Abdurasul Shamsiyev',
                'Gulchehra Ahmadjonova',
                'Muborak Xoliqova',
                'Diyor Alimov',
                'Dildora Rustamova',
                'Fotima Qudratova',
                'Husniddin Karimov',
                'Madina Jo‘rayeva',
                'Zubayda Ismoilova',
                'Sardor Zokirov',
                'Nigora Xasanova',
                'Azamat Saidov',
                'Zahro To‘xtasinova',
                'Sherali G‘aniyev',
                'Anora Boltaeva',
                'Zamira Tojiboyeva',
                'Azizbek Umarov',
                'Ulug‘bek Norqobilov',
                'Alisher G‘ofurov',
                'Aziza Narziyeva',
                'Jamshid Abdujalilov',
                'Hasan Mahmudov',
                'Habiba Ergasheva'
            ]
            
            ```
            
    2. Sizga faqat raqamlardan iborat list beriladi siz uni raqamga o'girib birni qoshib list qilib qaytarishingiz kerak,
        
        ```python
        Input: [1,2,3]
        Output: [1,2,4]
        __________________
        Input: [9]
        Output: [1,0]
        __________________
        Input: [9,9,9,9]
        Output: [1,0,0,0,0]
        ```
        
        Tushuntirish: 123 ga birni qoshilsa 124 va siz [1,2,4] qilib qaytarishingiz kerak
        
    3. Bizga list berilgan va foydalanuchi tomonidan bitta son kiritiladi. Agarda ikkita elementining yig'indisi kiritilgan songa teng bo'lsa shu elementlarning indexlarini ekranga chiqaruvchi dastur tuzing.
        
        ```python
        [1, 2, 33, 5, 6, 7, 7]
        **Input:** 3
        **Output:** 0, 1
        ____________
        **Input:** 8
        **Output:**
        0, 5
        0, 6
        1, 4
        ```
        
        Izoh: 
        
        1-misol: lst[0]+lst[1] = 3
        
        2-misol: 
        
        lst[0]+lst[5] = 8
        lst[0]+lst[6] = 8
        lst[1]+lst[4] = 8
        
    4. Foydalanuvchi listga istalgancha qiymat kiritadi, siz shu qiymatlar ichidan faqat bir marta takrorlangan raqamlar sonini chiqaradigan dastur yozing
        
        ```python
        Input:[4,1,2,1,2]
        Output: 1
        ___________
        Input:[1,2,3,1,1]
        Output: 2
        ```
        
        Izoh: 
        
        4 - bir marta takrorlangan. 1ta
        
        2 va 3 - bir marta takrorlangan. 2ta
        
    5. Tartiblangan toq va juftlari soni teng bo’lgan list elementlarining toq elementlarini o’sish tartibida, juft elementlarini esa kamayish tartibida joylab beradigan dastur yozing.
        
        ```python
        Input: [1,2,3,4,5,6,7,8,9,10]
        Output:[1,10,3,8,5,6,7,4,9,2]
        ```
        
    6. Listda bir nechta sonlar berilgan. Sonlar orasidan 1-raqami juft bo'lganlarni chiqaring.
        
        ```python
        Input: [123, 456, 789, 852, 12, 42, 61, 369]
        Output: [456, 852, 42, 61]
        ```
        
    7. Foydalanuvchi listga istalgancha qiymat kiritadi, siz shu qiymatlar ichidan faqat bir marta takrorlangan raqamlar sonini qaytaruvchi funksiya tuzing, unday sonlar yoq bolsa -1 qaytarsin.
        
        ```python
        Input:[4,1,2,1,2]
        Output: 1
        __________________
        Input:[1,2,3,1,1]
        Output: 2
        ```
        
- **Set va dict**
    
    **1-vazifa.** 3ta set berilgan, barcha setlar uchun **umumiy elementlarni** va **faqatgina birinchi set uchun tegishli** elementlarni chiqaring.
    
    ```python
    **Input:** 
    set1={"Artel","Alif","Yandex", "Google", "Meta"}
    set2={"Google", "Apple", "Amazon", "Meta"}
    set3={"Alibaba", "Uzum", "Meta", "Google", "Amazon"}
    
    **Output:** 
    Umumiy elementlar: Google, Meta
    Faqat birinchi setda mavjud: Artel, Alif, Yandex
    ```
    
    **2-vazifa.** Sonlardan iborat 2 ta set berilgan. Setlarning umumiy bo’lmagan elementlari yig’indisini chiqaring.
    
    ```python
    **Input:** 
    set1={2,3,4,5,6}
    set2={4,5,6,7,8,9}
    
    **Output:** 29
    ```
    
    *(chunki, ikkisi uchun umumiy bo’lmagan elementlar 2,3,7,8,9)*
    
    **3-masala.** Sonlardan iborat 2 ta set berilgan, bu setlardan 60dan kichik sonlarni o’chirib tashlang. So’ngra setlarning umumiy emementlarining o’rtacha qiymatini hisoblang.
    
    ```python
    **Input:** 
    set1={100, 20, 45, 80, 70, 50}
    set2={30, 55, 70, 60, 32, 100}
    
    **Output:** 85
    ```
    
    *(chunki 60dan katta umumiy elementlar 100, 70. (100+70)/2=85)*
    
    **dict**
    
    1. Bizda quyidagi dict berilgan.
        
        ```python
        days = {
            "January": 31,
            "February": 28,
            "March": 31,
            "April": 30,
            "May": 31,
            "June": 30,
            "July": 31,
            "August": 31,
            "September": 30,
            "October": 31,
            "November": 30,
            "December": 31,
        }
        ```
        
        (a) Foydalanuvchidan oy nomini kiritishini so'rang va oyda necha kun borligini aytish uchun lug'atdan foydalaning.
        
        ```python
        Input: Aprel
        Output:
        Aprel 30 kundan iborat
        ```
        
        (b) Barcha oylarni alifbo tartibida chop eting.
        
        ```python
        **Output:**
        April
        August
        December
        February
        January
        July
        June
        March
        May
        November
        October
        September
        ```
        
        (c) 31 kunlik barcha oylarni chop eting.
        
        ```python
        **Output:**
        August 31
        December 31
        January 31
        July 31
        March 31
        May 31
        October 31
        ```
        
        (d) Har oyda kunlar soni bo'yicha tartiblangan (kalit-qiymat) juftlarini chop eting
        
        ```python
        **Output:**
        28 February
        30 April
        30 June
        30 November
        30 September
        31 August
        31 December
        31 January
        31 July
        31 March
        31 May
        31 October
        ```
        
        (e) (a) qismidagi dasturni va lug'atni shunday o'zgartiringki, foydalanuvchi oy nomini qanday yozishni aniq bilishi shart emas. Ya'ni, ularga oy nomining dastlabki uchta harfini to'g'ri yozish kifoya.
        
        ```python
        **Output:**
        Input: Apr
        Output:
        Aprel 30 kundan iborat
        ```
        
    2. Foydalanuvchidan jamoa nomini, jamoaning qancha o'yin yutganini va qanchasini yutqazganini qayta-qayta kiritishni so'rang. Ushbu ma'lumotni lug'atda saqlang, bu yerda kalitlar jamoa nomlari, qiymatlar esa [g'alabalar, mag'lubiyatlar] shaklidagi ro'yxatlardir.
        
        ```python
        Input:
        Jamoa nomini kiriting (yoki 'exit' tugmasini bosing): Lions
        Lions jamoasining yutgan o‘yinlar sonini kiriting: 10
        Lions jamoasining yutqazgan o‘yinlar sonini kiriting: 5
        Jamoa nomini kiriting (yoki 'exit' tugmasini bosing): Tigers
        Tigers jamoasining yutgan o‘yinlar sonini kiriting: 7
        Tigers jamoasining yutqazgan o‘yinlar sonini kiriting: 8
        ...
        ```
        
        Hosil bo’lgan dict:
        
        ```python
        teams = {
            "Lions": [10, 5],      # 10 ta g‘alaba, 5 ta mag‘lubiyat
            "Tigers": [7, 8],      # 7 ta g‘alaba, 8 ta mag‘lubiyat
            "Bears": [6, 6],       # 6 ta g‘alaba, 6 ta mag‘lubiyat
            "Eagles": [12, 3],     # 12 ta g‘alaba, 3 ta mag‘lubiyat
            "Sharks": [4, 9],      # 4 ta g‘alaba, 9 ta mag‘lubiyat
            "Wolves": [9, 6],      # 9 ta g‘alaba, 6 ta mag‘lubiyat
            "Falcons": [8, 7],     # 8 ta g‘alaba, 7 ta mag‘lubiyat
        }
        ```
        
        (a) Yuqorida yaratilgan lug'atdan foydalanib, foydalanuvchiga jamoa nomini kiritishga va jamoaning g'alaba qozonish foizini chop etishga ruxsat bering.
        
        ```
        G'alaba foizini bilmoqchi bo'lgan jamoa nomini kiriting: Lions
        Lions jamoasining g‘alaba foizi: 66.67%
        ```
        
        (b) Lug'atdan foydalanib, har bir jamoaning g'alaba soni elementlari bo'lgan ro'yxat yarating.
        
        ```
        [10, 7, 6, 12, 4, 9, 8]
        ```
        
        (c) Lug'atdan foydalanib, g'alaba qozonish ko'rsatkichlari ijobiy bo'lgan barcha jamoalarning ro'yxatini yarating.
        
        ```
        G'alaba ko‘rsatkichi ijobiy bo‘lgan jamoalar: ['Lions', 'Eagles', 'Wolves','Falcons']
        ```
        
    3. 5 × 5 o'lchamli sonlar ro'yxatini yarating. Keyin kalitlari sonlar, qiymatlari esa sonning nechta uchrashini ko'rsatadigan lug'at yaratadigan dastur yozing. Keyin eng ko'p uchraydigan uchta sonni chop eting.
        
        ```
        
        5x5 Matritsa:
        [4, 9, 5, 7, 6]
        [3, 5, 6, 6, 1]
        [8, 5, 7, 5, 3]
        [9, 7, 6, 4, 2]
        [5, 6, 9, 8, 7]
        
        **Output:**
        Har bir sonning uchrashlari:
        4: 2
        9: 3
        5: 5
        7: 4
        6: 5
        3: 2
        1: 1
        8: 2
        2: 1
        
        Eng ko'p uchraydigan 3 ta son:
        5: 5 marta
        6: 5 marta
        7: 4 marta
        ```
        
    4. Sizga quyidagi satrlar ro'yxati berilgan:
        
        ```python
        L = ['aabaabac', 'cabaabca', 'aaabbcba', 'aabacbab', 'acababba']
        ```
        
        Foydalanuvchida faqat a**a**** tarzida qiymat kiritadi. Ya’ni hohlagancha * va hohlagancha harf yozadi. Siz usha harf usha o’rinda uchraydigan satrlarni chiqarishingiz kerak. * o’rnini solishtirmaysiz
        
        ```
        **Input:**
        Naqshni kiriting (masalan, a**a****): a**a****
        
        **Output:**
        Naqshga mos keladigan satrlar:
        aabaabac
        aabacbab
        ```
        
    5. Quyidagi lug'atlar berilgan:
        
        ```python
        d = [
         {
        	 "name": "Todd", 
        	 "phone": "555-1414", 
        	 "email": "[todd@mail.net](mailto:todd@mail.net)",
         },
         {
        	 "name": "Helga",
        	 "phone": "555-1618",
        	 "email": "[helga@mail.net](mailto:helga@mail.net)",
         },
         {
        	 "name": "Princess", 
        	 "phone": "555-3141", 
        	 "email": ""
         },
          {
        	  "name": "LJ", 
        	  "phone": "555-2718", 
        	  "email": "[lj@mail.net](mailto:lj@mail.net)"
          },
        ]
        
        ```
        
        Har qanday bunday lug'atni o'qib chiqadigan va quyidagilarni chop etadigan dastur yozing:
        
        1. Telefon raqami 8 bilan tugaydigan barcha foydalanuvchilar
        2. Elektron pochta manzili ko'rsatilmagan barcha foydalanuvchilar
        
        ```python
        **Output:**
        Telefon raqami 8 bilan tugaydigan foydalanuvchilar:
        Helga (555-1618)
        LJ (555-2718)
        
        Elektron pochta manzili ko'rsatilmagan foydalanuvchilar:
        Princess
        ```
        
    6. Rim raqamlarini oddiy sonlarga o'zgartiradigan dastur yozing. Mana mosliklar: M=1000, D=500, C=100, L=50, X=10, V=5, I=1. IV ning 4 ga va XL ning 40 ga teng ekanligini unutmang. 
        
        **!!! Shartni to’liq keltirish kerak**
        
    7. Oddiy sonlarni rim raqamlariga o'zgartiradigan dastur yozing.
        
        **!!! Shartni to’liq keltirish kerak**
        
- **Funksiya**
    1. Ichma ich list qabul qiluvchi va quyidagicha dictionary qaytaruvchi function tuzing
        
        ```python
        Input:
        [
            [1, "Jean Castro", "V"],
            [2, "Lula Powell", "V"],
            [3, "Brian Howell", "VI"],
            [4, "Lynne Foster", "VI"],
            [5, "Zachary Simon", "VII"],
        ]
        
        Otput:
        {
            1: ["Jean Castro", "V"],
            2: ["Lula Powell", "V"],
            3: ["Brian Howell", "VI"],
            4: ["Lynne Foster", "VI"],
            5: ["Zachary Simon", "VII"],
        }
        ```
        
    2. List qabul qilib, listning elementlarining toq elementlarini usish tartibida, juft elementlarini kamayish tartibida oz ornida tartiblab chiqaruvchi funksiya tuzing.
        
        ```python
        Input: [1,2,3,4,5,6,7,8,9,10]
        Output:[1,10,3,8,5,6,7,4,9,2]
        ```
        
    3. Quyidagi list ichidan Yoshi 18 dan katta va mashinasi 1 tadan ko`p hamma insonlar ismini chiqaruvchi function tuzing.
        
        ```python
        Input:
        [
            {"Name": "Asil", "age": 9, "cars": 3},
            {"Name": "Laziz", "age": 19, "cars": 2},
            {"Name": "Sardor", "age": 25, "cars": 7},
            {"Name": "Og`abek", "age": 5, "cars": 5},
        ]
        Output:
        {"Name": "Laziz", "age": 19, "cars": 2},
        {"Name": "Sardor", "age": 25, "cars": 7},
        ```
        
    4. List ichidagi har bir tuple qiymatlarinig yig'indisini yangi listga joylashtiradigan funksiya yozing.
        
        ```python
        Input:     [(1, 2), (2, 3), (3, 4)]
        Output:  [3, 5, 7]
        —————————————————————————
        Input:      [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
        Output:   [9, -1, 7, 8]
        ```
        
    5. Funksiya orqali Listda bir nechta sonlarni input orqali kiriting va ushbu sonlar orasidan 1-raqami juft bo'lganlarni chiqaring.
        
        ```python
        Input: [123, 456, 789, 852, 12, 42, 61, 369]
        Output: [456, 852, 42, 61]
        ```
        
    6. Function tuzing. Bu function natural sonlardan iborat list qabul qiladi. Va shu sonlardan yasash mumkin bo'lsan eng katta qiymatni qaytaradi:
        
        ```python
        Input:     [1, 2, 3]
        Output: 321
        ———————————————————
        Input:    [61, 228, 9]
        Output: 961228
        ```
        
    7. Foydalanuvchi listga istalgancha qiymat kiritadi, siz shu qiymatlar ichidan faqat bir marta takrorlangan raqamlar sonini qaytaruvchi funksiya tuzing, unday sonlar yoq bolsa -1 qaytarsin.
        
        ```python
        Input:[4,1,2,1,2]
        Output: 1
        _______________
        Input:[1,2,3,1,1]
        Output: 2
        ```
        
    8. isAnagram() function tuzing, bu function oziga ikki soz qabul qilib, bu sozlar anagram yoki yoqligini aniqlasin.
        
        NOTE: Anagram sozlar, ozaro bir xil harflardan tashkil topgan, ammo umuman boshqa boshqa so`zlar.
        
        ```
        Input: anagram,nagaram
        Output: True
        ___________
        Input: car,tac
        Output: False
        ```
        
    9. Foydalanuvchi aniq 4 xonali son kiritadi, shu sonning har ikki raqami yig'indisini chiqaruvchi function tuzing.
        
        ```python
        Input: 1234
        Output: 3,7
        ```
        
    10. List qabul qiladigan va shu list ichidagi istalgan 3 ta elementi raqamlar yig`indisi 0 ga teng bo`lgan sonlarni alohida list, qolganini alohida listga solib qaytaradigan function yozing. Agar bunday sonlar bo`lmasa bo`sh list qaytarsin.
        
        Har bir list umumiy bitta list ichida bo`lishi shart.
        
        ```python
        Input: [-1,0,1,2,-1,-4]
        Output: [[-1, 0, 1], [2, -1, -4]]
        ```
        
        Tushuntirish:
        
        - -1 + 0 + 1 =  0
    11. Foydalanuvchidan N sonini qabul qiling, va N sonini ildizini topuvchi function tuzing.
        
        Agar ildiz chiqmaydigan son bo`lsa -1 qaytarsin.
        
        **Kutubxonalar, functionlardan foydalanish mumkin emas.**
        
        ```python
        Input: 9
        Output: 3
        
        Input: 81
        Output: 9
        
        Input: 82
        Output: -1
        ```
        
    12. Foydalanuvchi istlagan xonali son kiritadi va sizning vazifangiz ushbu sonni birliklar, o’nliklar, yuzliklar va hokazo xonalar yig’indisi yoyilmasiga aylantirib chiqaradigan funksiya tuzish. strga yig'ib qaytarsin.
        
        ```python
        input: 123
        output: 100+20+3
        
        input: 4213
        output: 4000+200+10+3
        ```
        
    13. Dictionary berilgan ushbu dictionaryda kaliti juft o’rindagi qiymatlarni kaliti toq o’rindagi bilan almashtiradigan va chiqaradigan funksiya yarating.
        
        ```python
        Input: 
        dict1={1:ABC, 2:DEF, 3:GHI, 4:JKL, 5:MNO}
        Output:
        dict1={1:DEF, 2:ABC, 3:JKL, 4:GHI, 5:MNO}
        ```
        
    14. Foydalanuvchi gap kiritadi kiritgan gapni ekranga chop eting. 5 ta taqiqlanuvchi so’zlar mavjud agar foydalanuvchi shu sozlardan foydalangan bo’lsa shu so’z uzunligicha ‘*’ belgisini ekranga chop eting.
        
        Masalan:
        
        Taqiqlanuvchi so’zlar: [“salom”, “eshmat”, “toshmat”, “dunyo”, “noutbuk”]
        
        ```python
        Input: "SaloM do'stim eshmat bugun men yangi noutbuk sotib oldim"
        Output: *** do'stim **** bugun men yangi ***** sotib oldim
        ```
        
- **Lambda**
    1. Berilgan ikki satr anagram ekanligini aniqlaydigan funksiya. Izoh: Anagram degani uzunligi bir xil, tarkibidagi harflar bir hil, lekin o'rni har xil
        
        ```python
        Kirish: "ab", "ba"
        Chiqish: True
        ```
        
    2. Berilgan satrdan faqat raqamlarini qaytaradigan funksiya
        
        ```python
        Kirish: w34r1
        Chiqish: 341
        ```
        
    3. Kabisa yili ekanligini aniqlaydigan funksiya
        
        ```python
        Input: 2023
        Output: False
        ```
        
    4. Quyidagi ro'yxatni bal bo'yicha tartiblaydigan lambda funksiya yozing
        
        ```python
        Input: [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
        Output: [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
        ```
        
    5. Quyidagi ro'yxatni model bo'yicha tartiblaydigan lambda funksiya yozing
        
        ```python
        Input: [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
        Output: [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}]
        ```
        
    6. Berilgan ikki ro'yxatdan kesishadigan ro'yxat hosil qiladigan funksiya yozing
        
        ```python
        **Input:** 
        [1, 2, 3, 5, 7, 8, 9, 10]
        [1, 2, 4, 8, 9]
        
        **Output**: [1,2,8,9]
        ```
        
    7. Juft va toq sonlarni sanab beradigan funksiya
        
        ```python
        **Kirish**: [1, 2, 3, 5, 7, 8, 9, 10]
        
        **Chiqish**: {"toq": 5, "juft": 3}
        ```
        
- **Filter va map**
    1. Berilgan ro'yxat elementlaridan faqat sonlarni ajratib olib yangi ro'yxat hosil qiladigan funksiya
        
        ```python
        Kirish: ["2w3e", "er4", "56%"]
        Chiqish: [23,4,56]
        ```
        
    2. list dagi tub sonlarni yangi listga o'zlashtiring:
        
        ```
        ages = [5, 12, 17, 18, 24, 32, 19, 0, 21]
        Output: [5, 17, 19]
        ```