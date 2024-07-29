from langchain_teddynote.document_loaders import HWPLoader
import pprint

# HWP 문서 로드
loader = HWPLoader("디지털_정부혁신_추진계획.hwp")
docs = loader.load()

pprint.pprint(docs[0].page_content[:2000])