import discord
from discord.ext import commands
import os, random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def merhaba(ctx):
    await ctx.send(f"Merhaba {bot.user}! ben çevreyle alakalı bilgilendirme için varım seni bilgilendirmemi ister misin?")

@bot.command()
async def evet(ctx):
    await ctx.send(f"Dünyada 8 milyar insan var ve bunların çeyareğinin çeyreği bile yere aynı anda çöp atsa neredeyse bir dağ oluşur")
    await ctx.send(f"daha çok bilgilenmek istiyorsan DEVAM (küçük harflerle) yaz")
    await ctx.send(f"eğer geri dönüşüm kutuları ile alakalı bilgi almak istiyorsan GERİ_DÖNÜŞÜM (küçük harflerle) yaz")

@bot.command()
async def hayır(ctx):
    await ctx.send(f"{bot.user} bi bilgi öğrencen altı üstü çok zorlion ha")
    await ctx.send(f"Neyse bak {bot.user} Dünyada 8 milyar insan var ve bunların çeyareğinin çeyreği bile yere aynı anda çöp atsa neredeyse bir dağ oluşur ve sen bunu yapmaya devam edicen bunun sonucu senin gibiler yüzünden ADALAR OLUŞUYOR ")
    await ctx.send(f"bu yüzden eğer yere çöp atarsan {bot.user} kötü şeyler olur (panel kullanıp bilgilerini etrafa yayarım) oyezden yere çöp atma")
    await ctx.send(f"daha çok bilgilenmek istiyorsan DEVAM (küçük harflerle) yaz")
    await ctx.send(f"eğer geri dönüşüm kutuları ile alakalı bilgi almak istiyorsan GERİ_DÖNÜŞÜM (küçük harflerle) yaz")

@bot.command()
async def devam(ctx):
    await ctx.send(f"Çevre dostu insansız otomobiller için batarya üretimi o kadar da çevre dostu değildir ama insanlar bunu çok umursamıyor") 
    await ctx.send(f"Atmosferin sadece %21'i oksijendir, %78'i azot, %1'i su buharı,neon... dan oluşur ve azot arttıkça ozon tabakası incelir ozon tabakası incelirse küresel ısınma gerçekleşir ve bunun sonucu iyi olmaz")
    await ctx.send(f"Yüksek teknolojili roketler fırlatıldığında, atmosfere büyük miktarda kirletici madde salınır ve ozon tabakası incelir")

@bot.command()
async def geri_dönüşüm(ctx):
    await ctx.send(f"Geri döüşüm kutularının bi kaç çeşidi vardır bunlar
                     MAVİ: Kâğıt / Karton atıkları
                     SARI: Plastik atıkları
                     YEŞİL: Cam atıkları
                     GRİ: Metal atıkları
                     KAHVERENGİ: Organik atıklar
                     SİYAH: Geri dönüşemeyen atıklar
                     ŞEFFAF: Yemek artıkları
                     MOR: Ekmek artkları
                     TURUNCU: Tıbbi atıklar içindir")
    await ctx.send(f"Bu kutular belirli aralıklarla toplanır sonra ayrıştırılır ve yeniden kullanılabilmesi için belirli testlerden geçerler (geri dönüşebilenler için geçerli)")                

bot.run("...")