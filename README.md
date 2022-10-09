# Movie bot recap - ийг автоматжуулж монгол хэл дээр унших

# NOTE: This is fun project nothing serious

Ажиллагааны зарчим

```sh
1. Тухайн бичлэгний **srt** (subtitle) болон бичлэгийг онлайн түүлээр татна. (manual)
2. **srt** файлыг **json** -рүү хөрвүүлнэ.
3. Тухайн **json**-ийг орчуулахад бэлэн болгоно.
4. Орчуулга хийнэ. (google-translate selenium)
5. Орчуулсан текстээ уншуулна. (chimege free-api)
6. Үүссэн voice-уудыг анхны timestamp-тай давхцуулж өгнө.
7. Эцэст нь анхны бичлэгтэй холбоно.
```

Алдаанууд (одоогийн)

```sh
**BUG** Монголруу орчуулах үед өгүүлбэрийн бүтэц алдагдана. Subtitle болохоор өгүүлбэр дуусаагүй үед таслаад байгаа.
**FIX IDEA** Анхны бүх subtitle-ийг нийлүүлж нэг цогцолбор болгоно. Дараа нь өгүүлбэр бүрээр задлаад анхны timestamp-тай уяна.

**BUG** Chimege-ээр уншуулах үед ард талын хөдөө хээр талын ая яваад байгаа. Demo api ашиглаж байгаа болохоор салгаж авч чадахгүй байгаа.

**BUG** Уншуулсан текстээ тухайн timestamp-ийн хурдтай тааруулж хурдан бас удаас болгоно.
```