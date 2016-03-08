from gensim.models import *
import re


# What's the class that I want to extend?
class Lexophile(Word2Vec):

# $/=">";                     # input record separator
# while (<>) {
#   if (/<text /) {$text=1;}  # remove all but between <text> ... </text>
#   if (/#redirect/i) {$text=0;}  # remove #REDIRECT
#   if ($text) {

#     # Remove any text not normally visible
#     if (/<\/text>/) {$text=0;}
#     s/<.*>//;               # remove xml tags
#     s/&amp;/&/g;            # decode URL encoded chars
#     s/&lt;/</g;
#     s/&gt;/>/g;
#     s/<ref[^<]*<\/ref>//g;  # remove references <ref...> ... </ref>
#     s/<[^>]*>//g;           # remove xhtml tags
#     s/\[http:[^] ]*/[/g;    # remove normal url, preserve visible text
#     s/\|thumb//ig;          # remove images links, preserve caption
#     s/\|left//ig;
#     s/\|right//ig;
#     s/\|\d+px//ig;
#     s/\[\[image:[^\[\]]*\|//ig;
#     s/\[\[category:([^|\]]*)[^]]*\]\]/[[$1]]/ig;  # show categories without markup
#     s/\[\[[a-z\-]*:[^\]]*\]\]//g;  # remove links to other languages
#     s/\[\[[^\|\]]*\|/[[/g;  # remove wiki url, preserve visible text
#     s/{{[^}]*}}//g;         # remove {{icons}} and {tables}
#     s/{[^}]*}//g;
#     s/\[//g;                # remove [ and ]
#     s/\]//g;
#     s/&[^;]*;/ /g;          # remove URL encoded chars

#     # convert to lowercase letters and spaces, spell digits
#     $_=" $_ ";

#     chop;
#     print $_;

    def list_unknown_words(self, string):
        # Transformations taken from script at bottom of 
        # http://mattmahoney.net/dc/textdata.html
        string = string.lower()
        string = string.replace('0', ' zero ')
        string = string.replace('1', ' one ')
        string = string.replace('2', ' two ')
        string = string.replace('3', ' three ')
        string = string.replace('4', ' four ')
        string = string.replace('5', ' five ')
        string = string.replace('6', ' six ')
        string = string.replace('7', ' seven ')
        string = string.replace('8', ' eight ')
        string = string.replace('9', ' nine ')
        p = re.compile('[^a-z_]')
        words = p.sub(' ', string).split()
        unknown_words = filter(lambda word: not self.__contains__(word), words)
        print unknown_words
        return unknown_words

    # Anything to init?

    # These might already exist
    def load_model(self, filename):
        pass

    def save_model(self, filename):
        pass

    def contains(self, word):
        '''
        Checks if a word is in the model, i.e. is known.
        Input: word
        Output: boolean
        '''
        return self.__contains__

    def create_librarian(self, word):
        '''
        Creates a Librarian object
        Input: unknown word
        Output: Librarian object
        '''
        pass

    def dispatch_libarian(self, librarian):
        '''
        Starts a Librarian object and gets its results, i.e. a list of strings
        Input: Librarian object
        Output: Librarian's results as list of strings
        '''
        pass

    def learn_word(self, list_of_strings):
        '''
        Learns a new words
        Input: phrase generator object
        Output: none or should it return something so that we can dismiss
        the librarian?
        '''
        pass

        '''
        Probably want some testing functions, plus things to use the model
        , or not since it extends word2vec model object
        '''

# s = 'the 99th quick brown fox didn\'t jump over the lazy Queen'
# lex = Lexophile()
# print lex.list_unknown_words(s)
