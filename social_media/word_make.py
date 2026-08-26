letters=["l","e","r","t","a","y","I","x","n"]
print(f"given letters are : {letters} ")
print("make as many words as you can from these ")
print("you must not enter sam word again (:")
word=[]
 
words_made=0
 
total_words=154
valid_words = [
    "anxiety", "elytran", "exaltin", "laxity",
    "antler", "elixir", "elytra", "enrapt", "laxier", "linear", "nearly", "ratine", "retain", "retina", "retnal", "tyreax", "xenia", "xenial", "xianit", "yarnit",
    "alter", "anear", "antre", "artel", "axite", "axled", "early", "elain", "enray", "entia", "exalt", "exine", "exite", "extal", "eyrai", "inert", "inter", "irate", "later", "latex", "layer", "learn", "leary", "linet", "liter", "litre", "nieta", "niota", "ratel", "relax", "relay", "renal", "renix", "taler", "tinea", "train", "tread", "trial", "twain", "vital", "vixen", "xatyr", "xenia", "xeric", "xylan",
    "anil", "ante", "anti", "aren", "aret", "arty", "aryl", "axel", "axil", "axle", "axon", "earn", "elan", "elan", "etar", "eyra", "eyry", "into", "ital", "itay", "lane", "lant", "lare", "lari", "late", "lati", "lean", "lear", "lent", "leri", "liar", "lien", "lier", "line", "lint", "lira", "lire", "lite", "lynx", "near", "neat", "next", "nile", "nito", "nixe", "rail", "rain", "ranit", "rate", "real", "rein", "renl", "rial", "riel", "rile", "rina", "riot", "rite", "tael", "tail", "tain", "tale", "tali", "tane", "tare", "tarn", "teal", "tear", "tela", "tern", "tier", "tile", "tine", "tiny", "tire", "tirl", "tyne", "tyre", "tyri", "vile", "vine", "vita", "vixen", "xian", "xile", "xylo", "yard", "yare", "yarn", "yean", "year", "yern", "yeti",
    "ail", "ain", "air", "ait", "ale", "ali", "alt", "ane", "ani", "ant", "any", "are", "art", "ate", "atx", "axe", "ayi", "ear", "eat", "ela", "eli", "elt", "enr", "era", "ern", "eta", "eta", "idx", "ila", "ile", "ina", "ira", "ire", "ita", "lax", "lea", "lei", "ler", "let", "lex", "ley", "lia", "lie", "lin", "lit", "lye", "lyn", "nat", "nay", "nea", "nei", "net", "nil", "nit", "nix", "nye", "rai", "ran", "rat", "ray", "rei", "rel", "ren", "ret", "ria", "rin", "rit", "rix", "rya", "rye", "tae", "tai", "tan", "tax", "tea", "tel", "ten", "ter", "tex", "tie", "til", "tin", "tlr", "tra", "try", "tye", "xan", "xea", "xin", "yal", "yan", "yar", "yea", "yen", "yer", "yet", "yin",
    "ae", "ai", "al", "an", "ar", "as", "at", "ax", "ay", "ea", "el", "en", "er", "et", "ex", "ia", "id", "il", "in", "ir", "it", "la", "le", "li", "ln", "ly", "na", "ne", "ni", "ny", "ra", "re", "ri", "ta", "te", "ti", "tx", "ty", "xi", "ya", "ye", "yi"
]
 
 
while True :
    ask_word=input("enter the word you made :").strip().lower()
    if ask_word in valid_words :
        if ask_word in word :
            print("this word already founded by you ")
            break
        words_made+=1
        print(f"word is correct , words left to make are {total_words-words_made}.")
        word.append(ask_word)
        print(word)
     
    else :
        if ask_words=="e" or ask_words=="exit" :
          break
