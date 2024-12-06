- [x] 获取书源
- [x] 解析书源
- [x] 过滤书源
- [ ] 书籍详情 ruleBookInfo
- [x] 书籍内容 ruleContent
- [x] 书籍浏览 ruleExplore 
  - 将 pages/list 改成 explore
- [ ] 书籍搜索 ruleSearch
- [x] 书籍章节 ruleToc
- [ ] 下载书籍 download.py



阅读书源解析器
* 改用自定义格式，不和 legado 规则相同。
* 不支持 jsoup 规则，不支持自定义符号，不支持正则选择器等
* 同时完全使用 webview 实现所有内容获取。
* 规则仅以 python parsel 选择器为主。
* 通过策略模式，支持多种解析器。
- [x] 支持 css 选择器
- [x] 支持 xpath 选择器
- [ ] 支持 jsonp 选择器
- [ ] 支持 js

以下不支持：
- [ ] 支持 jsoup  
- [ ] 支持正则选择器
  - [ ] AllInOne
  - [ ] OnlyOne
  - [ ] 净化
- [ ] 自定义符号
  - [ ] &&
  - [ ] ||
  - [ ] %%


## JS 引擎
* quickjs https://bellard.org/quickjs/binary_releases/
  * `.\qjs.exe "console.log(2+2)"`
* python运行js库 https://github.com/PetterS/quickjs
* xst https://github.com/Moddable-OpenSource/moddable
  * `.\xst.exe -e "print('Hello from Moddable SDK!')"`
* 