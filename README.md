# Selenium_douban_GetCookies
(selenium/time/json)
# 豆瓣登录 Cookie 获取工具

一个基于 Selenium 的自动化脚本，用于登录豆瓣账号并保存 Cookies 到本地 JSON 文件。获取的 Cookies 可用于后续爬虫请求，避免重复登录和验证码干扰。

## 功能特点

- 自动打开 Edge 浏览器，跳转到豆瓣登录页面。
- 自动切换到密码登录方式。
- 自动填写账号密码（需在代码中配置）。
- 支持滑块验证码手动处理（等待 10 秒供用户拖动）。
- 登录成功后提取当前会话的所有 Cookies。
- 将 Cookies 以 JSON 格式保存到本地文件 `douban_edge_cookies.json`。

## 环境要求

- Python 3.6+
- Microsoft Edge 浏览器
- Edge WebDriver（Selenium 会自动管理，也可手动下载）

## 安装依赖

```bash
pip install selenium
