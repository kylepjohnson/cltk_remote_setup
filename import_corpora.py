from cltk.corpus.utils.importer import CorpusImporter
from cltk.corpus.greek.tlgu import TLGU


corpus_importer = CorpusImporter('greek')
corpus_importer.import_corpus('greek_models_cltk')
corpus_importer.import_corpus('tlg', '~/TLG_E/')
corpus_importer.import_corpus('phi7', '~/PHI7/')

corpus_importer.import_corpus('greek_software_tlgu')
t = TLGU()
t.convert_corpus(corpus='tlg')


corpus_importer = CorpusImporter('latin')
corpus_importer.import_corpus('latin_models_cltk')
corpus_importer.import_corpus('phi5', '~/PHI5/')
t.convert_corpus(corpus='phi5')
