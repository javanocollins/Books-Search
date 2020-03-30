def convert(string):
    li = string.replace(' ', '').replace('.', '').replace(',', '').replace('\n', '').lower()
    return li

def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1


paragraph = """There are names of sixteen (16) books of the Bible hidden in the paragraph below. 
Lets see how many you can find. A preacher found 15 books in twenty minutes; it took him 3 weeks 
just to find the 16th one, HAVE FUN! I once made a remark about the hidden books of the Bible. 
A certain luke, kept people looking so hard for facts, and for others, it was a revelation. 
Some were in a jam, especially since the names of the books were not capitalized. But the 
truth finally struck home to numbers of our readers. To others it was a job. We want it to 
be a most fascinating little moment for you. Yes, there will be some really easy ones to spot. 
Others may require judges to help find them. I will quickly admit it usually takes the preacher 
to find one of them, and there will be loud lamentations when it is found. A little lady says she 
brews a cup of tea so she can concentrate better. See how you will compete. Relax now, for there 
really are sixteen books of the Bible in this paragraph."""

books_list = {
    'Genesis','Exodus','Leviticus','Numbers',
    'Deuteronomy','Joshua','Judges','Ruth',
    'Samuel','Kings','Chronicles','Ezra',
    'Nehemiah','Esther','Job','Psalm',
    'Proverbs','Ecclesiastes','Song of Solomon','Isaiah',
    'Jeremiah','Lamentations','Ezekiel','Daniel',
    'Hosea','Joel','Amos','Obadiah',
    'Jonah','Micah','Nahum','Habakkuk',
    'Zephaniah','Haggai','Zechariah','Malachi',
    'Matthew','Mark','Luke','John',
    'Acts','Romans','Corinthians','Galatians',
    'Ephesians','Philippians','Colossians','Thessalonians',
    'Timothy','Titus','Philemon','Hebrews',
    'James','Peter','John','Jude','Revelation',
}

num = 1
for i in books_list:
    if i.lower() in convert(paragraph):
        print(num, '-', i)
        num+=1

print(convert(paragraph))