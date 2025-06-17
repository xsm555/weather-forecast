# 天气查询与可视化系统

这是一个基于 Python 的天气查询系统，可以获取指定城市的天气预报数据并生成可视化图表。

## 功能特点
- 查询全球任意城市的天气预报
- 获取5天天气预报数据
- 生成交互式温度变化图表
- 支持数据导出

## 技术栈
- Python 3
- Requests（网络请求）
- PyEcharts（数据可视化）
- OpenWeatherMap API

## 安装与使用

1. 克隆仓库：
```bash
git clone https://github.com/xsm555/weather-forecast.git
```

2. 安装依赖：
```bash
pip install requests pyecharts
```

3. 获取 OpenWeatherMap API 密钥：
   - 访问 https://openweathermap.org/api 注册账号
   - 创建 API 密钥
   - 在项目根目录创建 `api_key.txt` 文件并粘贴密钥

4. 运行程序：
```bash
python main.py
```



## 贡献指南
欢迎提交 Issue 或 Pull Request！
