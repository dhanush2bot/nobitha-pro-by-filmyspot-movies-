import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter

RUN_STRINGS = (
    "ಓ.. ಆಧಿಕಾರಂ... ಹಳೆಯದಂತೆ ನಿಮ್ಮದೇ.... ಯಾವ ಬದಲಾವಣೆಯೂ ಇಲ್ಲ..... ನಿರ್ಣಯವನ್ನು ಹೇಗೆನ್ನಿಸುತ್ತದೆ....!!!",
    "ಅಲ್ಲಾ... ಬಾಲ್ಯದವರ ಒಬ್ಬೊ... ಮಗನನ್ನು...",
    "ನನಗೆ ಬರೆಯಲು ಇಲ್ಲ ಅರಿಯದು ಸಾರೇ.... ಓದಲು ಅರಿಯಲಾಗದು....",
    "ಇಂದು ನಿನಗೆ ಇನ್ನು ಬರುವುದಿಲ್ಲ... ಇಂದಿನ ಹಳ್ಳಿ ಆಗಿಹೋಯಿತು.....",
    "ಚಾರವಾದದರಲ್ಲಿ ನಂಬಿಕೆ ಇಲ್ಲದಿದ್ದರೆ ಕನಲ್ ಹೊರಗೆ ಬೀಳುತ್ತದೆ.",
    "ಒಂದೇ ಜೀವನವೇ ಉಳಿದಿದೆ ಮನಸ್ಸಿನಲ್ಲಿಯೇ ನೋಡಿಕೊಳ್ಳುವುದಾದರೆ, ಸ್ವರ್ಗವಿಲ್ಲ ನರಕವಿಲ್ಲ, 'ಒಂದೇ ಜೀವನ', ಅದು ಎಲ್ಲಿ ಹೇಗೆ ಬೇಕೆನ್ನುವುದು ಅವನವನು ನಿರ್ಧಾರಿಸುತ್ತಾನೆ",
    "ವಾಟ್ ಎ ಬೋಂಬೆಸ್ಟಿಕ್ ಎಕ್ಸ್‌ಪ್ಲೋಶನ್! ಸಚ್ ಎ ಟೆರಿಫಿಕ್ ಡಿಸ್ಕ್ಲೋಸ್!!",
    "ಗೋ ಏವೇ ಸ್ಟಪ್ಪಿಡ್ ಇನ್ ದಿ ಹೌಸ್ ಆಫ್ ಮೈ ವೈಫ್‌ ಆಂಡ್ ಡಾಟರ್ ಯೂವಿಲ್ ನೋಟ್ ಸಿ ಏನಿ ಮಿನಿಟ್ ಆಫ್ ದಿ ಟುಡೇ... ಇರಿ ಹೋಗಿ...",
    "ಐ ಕಾನ್ ಡು ದಾಟ್‌ ಡು ಕಾನ್ ಐ ದಾಟ್‌",
    "ಕ್ರೀಂ ಬಿಸ್ಕಟಿಲ್‌ ಕ್ರೀಂ ಉಂಟನ್ನು ಕರುತಿ ಟೈಗರ್ ಬಿಸ್ಕಟಿಲ್‌ ಟೈಗರ್ ಉಂಟಾಗಣಮೆನ್ನಿಲ್ಲ. ಪಣಿ ಪಾಳುಂ ಮೋನೆ...",
    "ಪಟ ಪೇಟಿಚ್ಚು ಪಂತಳತ್ತು ಚೆನ್ನಪ್ಪೋ ಪಂತೋಂ ಕುತ್ತಿ ಪಟ ಪಂತಳತ್ತೋಟ್ಟೆನ್ನುವಾಯಿಲ್ಲೋ.",
    "ಎನ್ನೆ ಕರ್ತ್ತಾವೇ.... ನೀ ನನ್ನನ್ನು ಒಳ್ಳೆಯವನಾಗಿಸಲು ಒಪ್ಪೂಲ್ಲ ಅಲ್ಲೆ.",
    "ಕಾರ್ ಎಂಜಿನ್ ಔಟ್ಟ್ ಕಂಪ್ಲೀಟ್ಲಿ......",
    "ತಳ್ಳೆ ಕಳಿಪಿಟ್ಟು ತೀರಣಿಲ್ಲಲ್ಲೆ! !",
    "ಪಾತಿರಾತ್ರಿಕ್ಕೆ ನಿನ್ನ ಅಪ್ಪ ಉಂಟಾಗಿ ವೆಚ್ಚಿರಿಕ್ಕುನ್ನೋ ಪೋರೋಟ್ಟಯುಂ ಚಿಕ್ಕನುಂ....",
    "ಓ ಪಿನ್ನೆ ನೀ ಒಕ್ಕೆ ಪ್ರೇಮಿಕ್ಕುಮ್‌ಪೋಳ್ ಅದ್‌ ಪ್ರಣಯಂ.... ನಮ್ಮ್‌ಲ್ ಒಕ್ಕೆ ಪ್ರೇಮಿಕ್ಕುಮ್‌ಪೋಳ್ ಅದ್‌ ಕಂಪಿ....",
    "ದೈವಮೇ ನೀ ಮಾತ್ರಂ ರಕ್ಷಿಕ್ಕಣೇ....",
    "ಅವಳೆ ನೋಡಿ ಕುಡಿಯಿರಿಕ್ಕುವಾಯಿರುನ್ನಳಿಯಾ.",
    "ಚೆಲ್ಲಾಕ್ಕಣ್ಟು ನೀನೆನ್ನುವಾಚು ಪೋಟಾ ತಟಿ.ಯಾ .\
    ಷಟ್ಟ್ ಉಒ ಯುವ೼ ಮೌತ್ ಬ್ಲಡಿ gramavasis.",
    "ಪೋಯಿ ಚಾವಟ್ .\
    ನಿನ್ನೆ ಕೊನ್ನೆಯಾ patto.",
    "ನಿನ್ನೆ ಕೊನ್ನೆ ನಾಡುಕಾರ್ಕ್ಕುಂ ಗುಣೋಲ್ಲ್ಯ ವಿಟ್ಟುಕಾರ್ಕ್ಕುಂ ಗುಣೋಲ್ಲ್ಯ ಏನ್ತಿನಾ ಇಂಗ್ಗನೆ ನಾಣಂ ಕೇಟ್ಟು ಜೀವಿಕ್ಕುನ್ನಟ ಪಾಟ್ ವಾಳೆ ಚೆಙ್ಕತಳಿ ವಾಳೆ.",
)

@Client.on_message(
    filters.command("runs", COMMAND_HAND_LER) &
    f_onw_fliter
)
async def runs(_, message):
    """ /runs strings """
    effective_string = random.choice(RUN_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_text(effective_string)
    else:
        await message.reply_text(effective_string)
