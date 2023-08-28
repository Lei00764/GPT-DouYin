# 自动回复抖音评论

## 项目描述
该项目利用自动化测试工具 Selenium 爬取抖音视频评论，并使用 OpenAI GPT-3 的 API 进行文本生成，然后利用 Selenium 将生成的结果输入到评论回复框，实现自动回复抖音评论的功能。

## 安装
使用以下命令安装所需的 Python 包：
```bash
Copy code
pip3 install selenium
pip3 install openai
```

## 技术栈
爬虫：Selenium

## 使用说明
1. 在项目中使用 Selenium 编写爬虫脚本，用于抓取抖音视频评论。 
2. 利用 OpenAI GPT-3 的 API 进行文本生成，生成回复内容。 
3. 使用 Selenium 将生成的回复内容输入到抖音评论回复框。 
4. 运行脚本实现自动回复抖音评论的功能。

## 注意事项
1. 在使用本项目前，请确保您已经安装了 Chrome 浏览器，并下载对应版本的 ChromeDriver。 
2. 在运行脚本之前，请确保您拥有 OpenAI GPT-3 的 API 密钥。
