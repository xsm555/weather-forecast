# 将数据可视化处理
from pyecharts import options as opts
from pyecharts.charts import Line


def plot_7day_forecast(forecast, city):
    """
    可视化天气预报
    forecast: 从get_7day_forecast获取的数据
    city: 城市名称
    """
    if not forecast:
        return

    # 准备数据。二维列表初始化的用法
    dates = [day['date'] for day in forecast]
    temp_day = [day['temp_day'] for day in forecast]
    temp_night = [day['temp_night'] for day in forecast]
    weather_descriptions = [day['weather'] for  day in forecast]

    # 创建折线图
    line = (
        Line()
        .add_xaxis(dates)
        .add_yaxis(
            series_name="白天温度",
            y_axis=temp_day,
            is_smooth=True,  # 平滑曲线
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最高温"),
                    opts.MarkPointItem(type_="min", name="最低温"),
                ]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average", name="平均温度")]
            ),
            label_opts=opts.LabelOpts(is_show=True),  # 显示数值标签
        )
        .add_yaxis(
            series_name="夜间温度",
            y_axis=temp_night,
            is_smooth=True,
            markpoint_opts=opts.MarkPointOpts(
                data=[opts.MarkPointItem(type_="min", name="最低温")]
            ),
            markline_opts=opts.MarkLineOpts(
                data=[
                    opts.MarkLineItem(type_="average", name="平均值"),
                    opts.MarkLineItem(symbol="none", x="90%", y="max"),
                ]
            ),
            label_opts=opts.LabelOpts(is_show=True),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title=f"{city} 5天天气预报",
                subtitle="数据来源: OpenWeatherMap"
            ),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            xaxis_opts=opts.AxisOpts(
                type_="category",
                boundary_gap=False,
                axislabel_opts=opts.LabelOpts(rotate=45)  # X轴标签旋转45度
            ),
            yaxis_opts=opts.AxisOpts(
                name="温度 (°C)",
                name_location="end",
                name_gap=20,
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(width=2)
                ),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            legend_opts=opts.LegendOpts(
                pos_top="10%",
                pos_right="10%"
            ),
            datazoom_opts=[opts.DataZoomOpts(is_show=True)],
        )
    )

    # 添加天气描述标签
    for i, desc in enumerate(weather_descriptions):
        line.set_series_opts(
            markarea_opts=opts.MarkAreaOpts(
                data=[
                    [
                        {"xAxis": dates[i], "name": desc},
                        {"xAxis": dates[i]}
                    ]
                ],
                label_opts=opts.LabelOpts(position="inside", color="#333"),
            )
        )

    # 保存为HTML文件(直接从网页打开，可视化更好)
    output_file = f"{city}_5天预报.html"
    line.render(output_file)
    print(f"图表已保存至: {output_file}")
    return output_file