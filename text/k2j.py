from .japanese import japanese_to_romaji_with_accent
from .korean import (
    join_jamos, j2hcj, h2j,
    latin_to_hangul,
    number_to_hangul,
    g2pk,
)
from .cleaners import japanese_cleaners
import re
import jaconv


repl_lst = {
    'ㄲ': 'ㅋ',
    'ㄸ': 'ㅌ',
    'ㅃ': 'ㅍ',
    'ㅆ': 'ㅅ',
    'ㅉ': 'ㅊ',
    
    'ㅙ': 'ㅗ/ㅔ',
    'ㅚ': 'ㅗ/ㅣ',
    'ㅘ': 'ㅜㅏ',
    'ㅝ': 'ㅜ/ㅓ',
    'ㅞ': 'ㅜ/ㅔ',
    'ㅟ': 'ㅜㅣ',
    'ㅢ': 'ㅜㅣ',

    'ㅒ': 'ㅣㅔ',
    'ㅕ': 'ㅛ',
    'ㅖ': 'ㅣㅔ',

    'ㅓ': 'ㅗ',
    'ㅐ': 'ㅔ',
    'ㅡ': 'ㅜ',

    '||//ㅎ': 'ㄹ',
}


def get_word_list(text):
    text = latin_to_hangul(text)
    text = number_to_hangul(text)
    text = g2pk(text)
    text = j2hcj(h2j(text))
    text = re.sub(r'([\u3131-\u3163])$', r'\1.', text)
    return list(join_jamos(text.replace('  ', ' ')[:-1]))


def korean2katakana(text):
    word_lst = get_word_list(text)
    text = '/' + text.replace('/', ' ').replace('|', ' ').replace('^', ' ').replace('  ', ' ')
    print(text)
    new_lst = []

    for i, s in enumerate(word_lst):
        dh = list(j2hcj(h2j(s)))
        if len(dh) == 3:
            if dh[-1] == 'ㄴ':
                dh[-1] = 'ㄴ'
                
            elif dh[-1] == 'ㅁ' or dh[-1] == 'ㅇ':
                dh[-1] = 'ㄴ|'
            
            elif dh[-1] == 'ㄹ':
                dh[-1] = '||/'

            else: # ㄱ ㄷ ㅂ 
                dh[-1] = dh[-1]

        
        dh.append('/')
        new_lst.extend(dh)

    kr = ''.join(new_lst)
    for k, v in repl_lst.items():
        kr = kr.replace(k, v)
    kr2ro = japanese_to_romaji_with_accent(kr).replace('si', 'shi').replace('c', 'ts') \
                                              .replace('ti', 'ティ').replace('tu', 'トゥ') \
                                              .replace('di', 'ディ').replace('du', 'ドゥ')

    result = jaconv.alphabet2kata(kr2ro).replace('|', 'ー').replace('/', '').replace('^', '')
    result = result if result[-1] == '.' else result + '.'
    return f'[PREPROCESSED]{japanese_cleaners(result).replace(" ", "")}[PREPROCESSED]'