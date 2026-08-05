import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN =8901966728:AAEPIgrGOHSDFI1t_E2hxQ0Qu2dNCCwXzFc

AREAS = ["الحلة المركز","الكفل","القاسم","المسيب","الهاشمية","المدحتية","جبله","الطليعة","الاسكندرية","المحاويل","ابي غرق","نادر","الشوملي","الطهمازية","الدهلة","بني سعد","الوردية","الجزرة","عنانه","البو علوان","الدبلة","الخسروية","حي بابل","حي الامام","حي الحسين","حي الشهداء","حي الطيارة","حي الصحة","حي الجزائر","حي نادر الاولى","حي نادر الثانية","حي نادر الثالثة","حي الجامعة","حي الكرامة","حي الزهراء","حي العسكري","حي الاساتذة","حي الاكرمين","منطقة 60","منطقة 80","منطقة الجمعية","شارع 40","شارع 60","شارع الكورنيش","شارع الحلة ديوانية","طريق حلة كربلاء","طريق حلة نجف","طريق حلة بغداد","منطقة الدور","منطقة المعمل","منطقة الثورة","منطقة التجنيد","منطقة المحاربين","منطقة ابو خستة","منطقة البكرلي","منطقة السنية","منطقة الحصين","منطقة الرارنجية","منطقة الجفل","منطقة النخيلة","منطقة الدولاب","منطقة عوفي","منطقة البهبهاني"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = "👑 بوت بابل ابو جود 2026\n\nاختر رقم المنطقة:\n\n"
    for i, a in enumerate(AREAS, 1):
        msg += f"{i}. {a}\n"
    await update.message.reply_text(msg)

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        n = int(update.message.text.strip())
        if 1 <= n <= len(AREAS):
            await update.message.reply_text(f"📍 اخترت: {AREAS[n-1]}")
        else:
            await update.message.reply_text(f"اكتب رقم من 1 الى {len(AREAS)}")
    except:
        await update.message.reply_text("دز رقم فقط حبيبي")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
    app.run_polling()

if __name__ == "__main__":
    main()
