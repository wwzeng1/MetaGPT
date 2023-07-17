#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/4/29 15:36
@Author  : alexanderwu
@File    : translator.py
"""

class Translator:

    @classmethod
    def translate_prompt(cls, original, lang='Chinese'):
        '''Translate the prompt to the specified language'''
        prompt = '''
# Instruction
Next, as a translator with 20 years of experience, when I give an English sentence or paragraph, you will provide a smooth and readable {LANG} translation. Please note the following requirements:
1. Ensure the translation result is smooth and easy to understand
2. Whether it is a declarative sentence or a question, I will only translate
3. Do not add content unrelated to the original text

# Original
{ORIGINAL}

# Translation
'''
        return prompt.format(LANG=lang, ORIGINAL=original)
