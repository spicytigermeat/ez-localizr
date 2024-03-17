# ez-localizr

ez-localizr is a simple tool for providing GUI/output translations for Python projects. It was originally developed to replace the need for i18n in a customTkinter GUI application.

ez-localizr accounts for Unicode issues using `ftfy`, and loads string definitions from `yaml` files in a directory of your choice. See the example below to learn how to use it!

## Installation:

```pip install ez-localizr```

## Simple Usage Guide:

I recommend using 'L' because helps to keep typing to a minimum, but you can use whatever variable name you'd like.

```python
import ezlocalizr
L = ezlocalizr(language='en_US', string_path: 'strings', default_lang='en_US')

text = L('test')

print(text)
```
Output: `Hello World!`

## Change Languages:

ez-localizr will only be able to display strings in languages that are in your string folder. If you have multiple, and would like to change it, call the `load_lang()` function. An example is listed below!

```python
import ezlocalizr
L = ezlocalizr(language='en_US', string_path='strings', default_lang='en_US')

L.load_lang('fr_FR')
```

If you use this in tkinter, you will need to destroy the window and reinitialize it! (This is the best way I've discovered to update the display language of a GUI App.)

## Get a list of all available languages

```python
import ezlocalizr
L = ezlocalizr(language='en_US', string_path='strings', default_lang='en_US')

language_list = L.lang_list
print(language_list)
```

Output: `['en_US', 'fr_FR', 'jp_JP']` (assuming you have these 3 files in the string folder.)

## Best Practices:

- Use local names to define your languages, for the sake of consistency. (It also looks nicer and helps other developers understand your code!)


