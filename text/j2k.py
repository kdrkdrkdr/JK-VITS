from .cleaners import japanese_to_romaji_with_accent, korean_cleaners
from .korean import join_jamos

repl_lst = {
    '.': '. ',
    '↓': '',
    '↑': '',
    'a': 'a ',
    'i': 'i ',
    'u': 'u ',
    'e': 'e ',
    'o': 'o ',
    'Q': ' |Q ',
    'N': ' |N ',
    'U': 'u ',
    'I': 'i ',
    'A': 'a ',
    'E': 'e ',
    'O': 'o ',
}

repl_lst2 = {
    'ʧu': '츠',
    'tsu': '츠',
    'zu': '즈',
    'su': '스',

    'wa': '*ㅘ',
    'wo': '오',

    'g': 'ㄱ',
    'n': 'ㄴ',
    'd': 'ㄷ',
    'r': 'ㄹ',
    'm': 'ㅁ',
    'b': 'ㅂ',
    'v': 'ㅂ',
    'ʃ': 'ㅅ',
    's': 'ㅅ',
    'j': 'ㅈ',
    'ʧ': 'ㅊ',
    'ts': 'ㅊ',
    'k': 'ㅋ',
    't': 'ㅌ',
    'p': 'ㅍ',
    'h': 'ㅎ',
    'f': 'ㅎ',

    'a': '*ㅏ',
    'i': '*ㅣ',
    'u': '*ㅜ',
    'e': '*ㅔ',
    'o': '*ㅗ',

    'y*ㅏ':'*ㅑ',
    'y*ㅜ':'*ㅠ',
    'y*ㅔ':'*ㅖ',
    'y*ㅗ':'*ㅛ',

    '  |N':'|N',
    '  |Q':'|Q',
}

repl_lst3 = {
    '|Qㄱ': 'ㄱㄱ',
    '|Qㅅ': 'ㅅㅅ',
    '|Qㄷ': 'ㄷㄷ',
    '|Qㅊ': 'ㄷㅊ',
    '|Qㅍ': 'ㅂㅍ',

    '|Nㅁ': 'ㅁㅁ',
    '|Nㅂ': 'ㅁㅂ',
    '|Nㅍ': 'ㅁㅍ',

    '|Nㅅ': 'ㄴㅅ',
    '|Nㅈ': 'ㄴㅈ',
    '|Nㅌ': 'ㄴㅌ',
    '|Nㅊ': 'ㄴㅊ',
    '|Nㄷ': 'ㄴㄷ',
    '|Nㄴ': 'ㄴㄴ',
    '|Nㄹ': 'ㄴㄹ',

    '|Nㅋ': 'ㅇㅋ',
    '|Nㄱ': 'ㅇㄱ',
    '|Nㅇ': 'ㅇㅇ',
    '|Nㅎ': 'ㅇㅎ',
    
    '|Q': 'ㅅ',
    '|N': 'ㄴ',
}


def japanese2korean(text):
    text = japanese_to_romaji_with_accent(text).strip().replace('^', '').replace(' ', '^ ')

    for k, v in repl_lst.items():
        text = text.replace(k, v)
    for k, v in repl_lst2.items():
        text = text.replace(k, v)

    text = ' '.join([i.replace('*', 'ㅇ') if i.startswith('*') else i.replace('*', '') for i in text.strip().split(' ')])

    for k, v in repl_lst3.items():
        text = text.replace(k, v)

    text = join_jamos(text.replace('  ', ' ')).replace(' ', '').replace('^', ' ')
    return f"[PREPROCESSED]{korean_cleaners(text)}[PREPROCESSED]"


