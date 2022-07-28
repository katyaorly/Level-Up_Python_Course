from translate import Translator
from langdetect import detect

def get_det_language(str_det):
    try:
        lang = detect(str_det)
        return lang
    except TypeError:
        return False

def func_trans(str_tr):
    translator = Translator(from_lang=get_det_language(str_tr), to_lang="ru")
    translation = translator.translate(str_tr)
    return translation

def func_det_tran(str_det_tran):
    detlan = get_det_language(str_det_tran)
    tranlan = func_trans(str_det_tran)
    return detlan, tranlan
