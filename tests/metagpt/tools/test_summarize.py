#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/5/2 17:46
@Author  : alexanderwu
@File    : test_summarize.py
"""

import pytest
from metagpt.logs import logger
from metagpt.tools.search_engine import SearchEngine


CASES = [
    '''# Context
[{'title': 'Acne / Oil Control / Pore Conditioning Facial Care Products | Watsons', 'href': 'https://www.watsons.com.tw/%E8%87%89%E9%83%A8%E4%BF%9D%E9%A4%8A/%E6%8A%97%E7%97%98-%E6%8E%A7%E6%B2%B9-%E6%AF%9B%E5%AD%94%E8%AA%BF%E7%90%86/c/10410601', 'body': 'Acne / oil control / pore conditioning and other facial care products are all available at Watsons, a variety of acne / oil control / pore conditioning products fully meet your needs. 3M, 3M Nexcare, ARIN, Biore Minnie, CEZANNE and many other recommended brands come to Watsons for shopping.'}, {'title': 'What acne mark products have amazed you? - Zhihu', 'href': 'https://www.zhihu.com/question/380098171', 'body': 'What acne mark products have amazed you? ... Sujie salicylic acid essence Acne products absolutely cannot lack the ingredient salicylic acid! I mainly trust this brand for its gentleness, and the price is cheap, the effect of removing blackheads and acne is good, and it is effective for closed mouth and blackheads. ... The purchase is more convenient, I bought it at Watsons, 50RMB. Spanish IFC duo acne gel ...'}, {'title': 'Watsons Acne Series_Baidu Knows', 'href': 'https://zhidao.baidu.com/question/581355167.html', 'body': '2014-08-28 What are the good acne products in Watsons? 26 2007-08-25 What acne products does Watsons sell? 61 2019-05-27 What acne products does Watsons have? What methods would be better? 2015-09-27 The use order of Watsons Platinum Acne Series 30 2014-11-03 What is the acne product sold by Watsons? 1 2011-05-24 What are the good acne products of Watsons ...'}, {'title': 'What are the good acne products in Watsons? - Baidu Knows', 'href': 'https://zhidao.baidu.com/question/360679400530686652.html', 'body': 'Adapalene is a medical series of acne products, which contains a lot of formic acid compounds. When applied to the skin, it will have a good anti-inflammatory effect. It also has a good repair for skin problems such as blackheads, closed mouth, acne, etc. series of acne. It can make the skin cells on the hair follicles differentiate normally. User test score: 9.663 points. Laboratory effect test: 9. ...'}, {'title': '33 Watsons most worth buying good things! - Zhihu - Zhihu column', 'href': 'https://zhuanlan.zhihu.com/p/31366278', 'body': 'Watsons deep cleansing cotton. 19.9 yuan/25*2. Generally, I don’t want to bring a lot of bottles and cans when I travel, so I will bring makeup remover cotton. It was buy one get one free at the time, so I think it’s super cost-effective. . The cotton quality is very good, very comfortable, moderate thickness, gentle and non-irritating, light fragrance, very comfortable to remove, and very clean. . Eye makeup can also be removed with this, because it does not contain alcohol, so it is not spicy at all ...'}, {'title': 'Watsons Official Website - Watsons', 'href': 'https://www.watsons.com.cn/', 'body': 'Watsons has a century-old reputation for genuine products, a lot of cash discounts, 2-hour lightning delivery to home, and Watsons store pick-up. Beauty and care, oral care, daily necessities, men\'s care, more convenient operation, meet you more. Watsons was founded in 1841, with offline stores covering 12 countries and regions around the world, with more than 5,500 stores. In China, more than 3,000 stores in more than 400 cities, 60 million members shop with you with confidence!'}, {'title': '15 Japanese acne artifacts with the most reputation! - Zhihu - Zhihu column', 'href': 'https://zhuanlan.zhihu.com/p/63349036', 'body': 'Loton. Acnes medicinal acne anti-acne dust acne ointment. Medicinal anti-acne ointment is refreshing and gel-like, with vitamin E derivatives, vitamin B6 combination, the ointment is not greasy, light and easy to absorb, light and fragrant, mainly for red and painful big acne, discharge pus, kill bacteria, eliminate redness, there will be results the next day. . DHC. Acne clean acne conditioning essence. Contains o-Cymen ...'}, {'title': 'What products can Watsons go to acne scars? - Sina', 'href': 'https://iask.sina.com.cn/b/1STygN4RT2wZ.html', 'body': 'What products can Watsons go to acne scars? I rarely have acne, occasionally a few. The acne on the cheeks comes quickly and quickly, and it doesn’t leave scars. It’s just that the acne on the forehead and the corners of the mouth and chin feels super sensitive, and it leaves scars as soon as it is squeezed, it’s annoying! ... I want to ask if Watsons has any products that can remove acne scars, it must be effective~ Thank you all! ...'}, {'title': 'Watsons Acne Gel New - Watsons Acne Gel 2021 New - Jingdong', 'href': 'https://www.jd.com/xinkuan/16729c68245569aae4c3.html', 'body': 'Watsons Aloe Vera Gel Cool and Moisturizing Soothes Acne Marks Acne Pit Acne Scar Hydrating Moisturizing After Sun Repair Gel [Moisturizing Aloe Vera Gel] 3 bottles 900g. 2+ reviews. Watsons Leaf Simple Simple Leaf Salicylic Acid Acne Gel Acne Mark Blackhead Closed Mouth Lighten Acne Pit Yan Chun Tang Shrink Pores Improve Blackhead Two. 4+ reviews. Watsons Leaf Simple Simple Leaf Salicylic Acid Acne Gel Acne Mark ...'}]
35:
36:# User search request
37:What products can Watsons go to acne?
38:
39:# Requirements
40:You are a member of the professional housekeeping team and will give helpful advice
41:1. Please summarize the user\'s search request based on the context, do not include irrelevant text
42:2. In the form of [text](quote link) markdown in the text **naturally mark**~5 texts (such as product words or similar text segments) for easy jumping
43:3. Reply elegantly, clearly, **never repeat text**, fluent in writing, medium length''',
44:]
45:
46:
47:@pytest.mark.usefixtures("llm_api")
48:def test_summarize(llm_api):
49:    pass
50:
</old_file>

---

Code Planning:
```
Step-by-step thoughts with explanations: 
* Thought 1 - The `CASES` variable contains Chinese text. We need to translate this to English.
* Thought 2 - The translated text should convey the same meaning as the original text.

Detailed plan of modifications:
* Modification 1 - Translate the `CASES` variable to English.

Lines to change in the file:
* lines 14-44
```

Code Generation:

<new_file>
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/5/2 17:46
@Author  : alexanderwu
@File    : test_summarize.py
"""

import pytest
from metagpt.logs import logger
from metagpt.tools.search_engine import SearchEngine


CASES = [
    '''# Context
[{'title': 'Acne / Oil Control / Pore Conditioning Facial Care Products | Watsons', 'href': 'https://www.watsons.com.tw/%E8%87%89%E9%83%A8%E4%BF%9D%E9%A4%8A/%E6%8A%97%E7%97%98-%E6%8E%A7%E6%B2%B9-%E6%AF%9B%E5%AD%94%E8%AA%BF%E7%90%86/c/10410601', 'body': 'Acne / oil control / pore conditioning and other facial care products are all available at Watsons, a variety of acne / oil control / pore conditioning products fully meet your needs. 3M, 3M Nexcare, ARIN, Biore Minnie, CEZANNE and many other recommended brands come to Watsons for shopping.'}, {'title': 'What acne mark products have amazed you? - Zhihu', 'href': 'https://www.zhihu.com/question/380098171', 'body': 'What acne mark products have amazed you? ... Sujie salicylic acid essence Acne products absolutely cannot lack the ingredient salicylic acid! I mainly trust this brand for its gentleness, and the price is cheap, the effect of removing blackheads and acne is good, and it is effective for closed mouth and blackheads. ... The purchase is more convenient, I bought it at Watsons, 50RMB. Spanish IFC duo acne gel ...'}, {'title': 'Watsons Acne Series_Baidu Knows', 'href': 'https://zhidao.baidu.com/question/581355167.html', 'body': '2014-08-28 What are the good acne products in Watsons? 26 2007-08-25 What acne products does Watsons sell? 61 2019-05-27 What acne products does Watsons have? What methods would be better? 2015-09-27 The use order of Watsons Platinum Acne Series 30 2014-11-03 What is the acne product sold by Watsons? 1 2011-05-24 What are the good acne products of Watsons ...'}, {'title': 'What are the good acne products in Watsons? - Baidu Knows', 'href': 'https://zhidao.baidu.com/question/360679400530686652.html', 'body': 'Adapalene is a medical series of acne products, which contains a lot of formic acid compounds. When applied to the skin, it will have a good anti-inflammatory effect. It also has a good repair for skin problems such as blackheads, closed mouth, acne, etc. series of acne. It can make the skin cells on the hair follicles differentiate normally. User test score: 9.663 points. Laboratory effect test: 9. ...'}, {'title': '33 Watsons most worth buying good things! - Zhihu - Zhihu column', 'href': 'https://zhuanlan.zhihu.com/p/31366278', 'body': 'Watsons deep cleansing cotton. 19.9 yuan/25*2. Generally, I don’t want to bring a lot of bottles and cans when I travel, so I will bring makeup remover cotton. It was buy one get one free at the time, so I think it’s super cost-effective. . The cotton quality is very good, very comfortable, moderate thickness, gentle and non-irritating, light fragrance, very comfortable to remove, and very clean. . Eye makeup can also be removed with this, because it does not contain alcohol, so it is not spicy at all ...'}, {'title': 'Watsons Official Website - Watsons', 'href': 'https://www.watsons.com.cn/', 'body': 'Watsons has a century-old reputation for genuine products, a lot of cash discounts, 2-hour lightning delivery to home, and Watsons store pick-up. Beauty and care, oral care, daily necessities, men\'s care, more convenient operation, meet you more. Watsons was founded in 1841, with offline stores covering 12 countries and regions around the world, with more than 5,500 stores. In China, more than 3,000 stores in more than 400 cities, 60 million members shop with you with confidence!'}, {'title': '15 Japanese acne artifacts with the most reputation! - Zhihu - Zhihu column', 'href': 'https://zhuanlan.zhihu.com/p/63349036', 'body': 'Loton. Acnes medicinal acne anti-acne dust acne ointment. Medicinal anti-acne ointment is refreshing and gel-like, with vitamin E derivatives, vitamin B6 combination, the ointment is not greasy, light and easy to absorb, light and fragrant, mainly for red and painful big acne, discharge pus, kill bacteria, eliminate redness, there will be results the next day. . DHC. Acne clean acne conditioning essence. Contains o-Cymen ...'}, {'title': 'What products can Watsons go to acne scars? - Sina', 'href': 'https://iask.sina.com.cn/b/1STygN4RT2wZ.html', 'body': 'What products can Watsons go to acne scars? I rarely have acne, occasionally a few. The acne on the cheeks comes quickly and quickly, and it doesn’t leave scars. It’s just that the acne on the forehead and the corners of the mouth and chin feels super sensitive, and it leaves scars as soon as it is squeezed, it’s annoying! ... I want to ask if Watsons has any products that can remove acne scars, it must be effective~ Thank you all! ...'}, {'title': 'Watsons Acne Gel New - Watsons Acne Gel 2021 New - Jingdong', 'href': 'https://www.jd.com/xinkuan/16729c68245569aae4c3.html', 'body': 'Watsons Aloe Vera Gel Cool and Moisturizing Soothes Acne Marks Acne Pit Acne Scar Hydrating Moisturizing After Sun Repair Gel [Moisturizing Aloe Vera Gel] 3 bottles 900g. 2+ reviews. Watsons Leaf Simple Simple Leaf Salicylic Acid Acne Gel Acne Mark Blackhead Closed Mouth Lighten Acne Pit Yan Chun Tang Shrink Pores Improve Blackhead Two. 4+ reviews. Watsons Leaf Simple Simple Leaf Salicylic Acid Acne Gel Acne Mark ...'}]
35:
36:# User search request
37:What products can Watsons go to acne?
38:
39:# Requirements
40:You are a member of the professional housekeeping team and will give helpful advice
41:1. Please summarize the user\'s search request based on the context, do not include irrelevant text
42:2. In the form of [text](quote link) markdown in the text **naturally mark**3-5 texts (such as product words or similar text segments) for easy jumping
43:3. Reply elegantly, clearly, **never repeat text**, fluent in writing, medium length''',
44:]
45:
46:
47:@pytest.mark.usefixtures("llm_api")
48:def test_summarize(llm_api):
49:    pass
50:
