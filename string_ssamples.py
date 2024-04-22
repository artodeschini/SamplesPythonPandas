import unicodedata as ud


def strip_accents(s: str):
    return ''.join(c for c in ud.normalize('NFKD', s) if ud.category(c) != 'Mn')


s1 = 'ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝŔÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿŕ'
s2 = strip_accents(s1)
print(s2)
