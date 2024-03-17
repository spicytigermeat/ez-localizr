import yaml
import locale
import glob
import logging

from pathlib import Path as P
from ftfy import fix_text as fxy

def logger_init():
	log = logging.getLogger(__name__)

	logger_fmt = "| %(levelname)s | %(message)s | %(asctime)s |"	
	logger_date_fmt = "%H:%M:%S"
	logging.basicConfig(format=logger_fmt, datefmt=logger_date_fmt)

	log.setLevel(logging.INFO)

	return log

class ezlocalizr:
	def __init__(self, 
				 language = None, 
				 string_path = None,
				 default_lang = None):

		self.string_path = string_path

		# language should never be None, but this is a failsafe
		if language in [None]:
			language = locale.getdefaultlocale()[0]
		if not P(P(self.string_path) / P(f"{language}.yaml")).exists():
			language = default_lang

		self.lang = language
		self.L = self.load_lang(language)
		self.default = self.load_lang(default_lang)

		self.log = logger_init()

	def __call__(self, k):
		try:
			return fxy(self.L[k])
		except KeyError:
			return fxy(self.default[k])
			self.log.warning(f"| Unable to load '{k}' from the dictionary for {self.lang}, defaulting to English.")
		except:
			return fxy(str(k))
			self.log.warning(f"| Unable to load '{k}' from the dictionary for {self.lang} or default, returning a dummy string.")

	def __repr__(self):
		self.log.info(f"ez-localizr: Using Language: {self.lang}")

	def __len__(self):
		return len(self.L.keys())

	@property
	def dictionary(self):
		# return the string dictionary
		return self.L

	@property
	def lang_list(self):
		# return a list of all possible languages
		return [P(file).stem for file in glob.glob(str(P(P(self.string_path) / P('*.yaml'))), recursive=True)]

	@property
	def curr_lang(self):
		return self.L['lang_code']

	def load_lang(self, lang):
		try:
			with open(P(P(self.string_path) / P(f"{lang}").with_suffix('.yaml')), 'r', encoding='utf-8') as l:
				return yaml.safe_load(l.read())
		except yaml.YAMLError as e:
			self.log.warning(f"| Unable to load language. Terminating LabelMakr.\n YAML Error: {e}")

if __name__ == "__main__":
	L = ezlocalizr(language='en_US', string_path=P('strings'), default_lang='en_US')

	print(L('lang_code'))