from weather_api import get_7day_forecast
from plot_weather import plot_7day_forecast


def main():
    print("=== 5天天气预报查询 ===")  # 改为5天预报

    while True:
        city = input("\n请输入城市名称(英文，如: shenzhen): ").strip()
        if not city:
            print("城市名称不能为空!")
            continue

        # 获取天气数据
        print(f"\n正在获取 {city} 的天气预报...")
        forecast = get_7day_forecast(city)

        if not forecast:
            print("获取数据失败，请重试")
            continue

        # 显示简要信息
        print(f"\n{city} 未来5天天气预报:")
        print("-" * 50)
        for day in forecast:
            print(f"{day['date']}: 白天 {day['temp_day']}°C, 夜间 {day['temp_night']}°C, {day['weather']}")
        print("-" * 50)

        # 可视化数据
        plot_7day_forecast(forecast, city)
        print(f"已生成图表: {city}_5天预报.png")  # 修改文件名

        # 是否继续
        choice = input("\n是否继续查询? (y/n): ").lower()
        if choice != 'y':
            print("感谢使用!")
            break


if __name__ == "__main__":
    main()