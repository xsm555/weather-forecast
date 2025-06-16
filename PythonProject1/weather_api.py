import requests
from datetime import datetime, timedelta


def get_api_key():
    """从文件读取API密钥"""
    try:
        with open('api_key.txt', 'r', encoding='utf-8') as f:
            return f.read().strip()
    except FileNotFoundError:
        print("错误：请创建api_key.txt文件并添加API密钥")
        return ""


def get_7day_forecast(city):
    """
    获取指定城市7天天气预报
    返回：包含7天数据的列表
    """
    api_key = get_api_key()
    if not api_key:
        return []

    # 使用正确的API端点（免费用户使用5天预报）获取7天数据会出错
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={api_key}"

    # 添加请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "application/json"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)

        # 检查响应状态（初次错误点，着重处理）
        # https://api.openweathermap.org/data/2.5/weather?q=London&appid=对应密钥，可浏览此网页来判断密钥是否有效
        if response.status_code == 401:
            print("API密钥无效或未授权，请检查密钥")
            return []
        response.raise_for_status()  # 检查其他错误

        data = response.json()

        # 提取关键数据（改为处理5天预报数据）
        forecast = []
        for item in data['list']:
            # 只取每天12:00的数据作为当日预报
            if item['dt_txt'].endswith("12:00:00"):
                date = datetime.strptime(item['dt_txt'], '%Y-%m-%d %H:%M:%S').strftime('%m/%d')

                forecast.append({
                    'date': date,
                    'temp_day': item['main']['temp'],
                    'temp_night': item['main']['temp_min'],  # 使用最低温作为夜间温度
                    'weather': item['weather'][0]['description'],
                    'humidity': item['main']['humidity']
                })

        # 只返回5天数据（免费API最多5天）
        return forecast[:5]

    except requests.exceptions.RequestException as e:
        print(f"网络错误: {str(e)}")
        print(f"详细错误信息: {e.response.text if hasattr(e, 'response') else '无响应'}")
        return []
    except KeyError:
        print("API返回数据格式错误")
        return []