from django.shortcuts import render, redirect, get_object_or_404
from .models import Stock
from app.forms.forms import StockForm

# import pandas as pd
# import matplotlib.pyplot as plt
import plotly.express as px


# Create your views here.
def index(request):
    stocks = Stock.objects.all()
    # context = {"stocks": stocks}

    # Extract data from Stock objects
    # data = {
    #     "date": [stock.date for stock in stocks],
    #     "trade_code": [stock.trade_code for stock in stocks],
    #     "high": [float(stock.high) for stock in stocks],
    #     "low": [float(stock.low) for stock in stocks],
    #     "open": [float(stock.open) for stock in stocks],
    #     "close": [float(stock.close) for stock in stocks],
    #     "volume": [int(stock.volume.replace(",", "")) for stock in stocks],
    # }

    # # Create a DataFrame from the data
    # df = pd.DataFrame(data)

    # # Prepare data for line chart
    # line_data = df.groupby(["trade_code", "date"])["close"].mean().unstack()

    # # Prepare data for bar chart
    # bar_data = df.groupby(["trade_code", "date"])["volume"].sum().unstack()

    # # Generate line chart and save it as a temporary file
    # line_chart = line_data.plot.line()
    # line_chart.set_xlabel("Date")
    # line_chart.set_ylabel("Close")

    # # Generate bar chart and save it as a temporary file
    # bar_chart = bar_data.plot.bar()
    # bar_chart.set_xlabel("Date")
    # bar_chart.set_ylabel("Volume")

    # # Save the plots as temporary files
    # line_chart_path = "static/line_chart.png"
    # bar_chart_path = "static/bar_chart.png"
    # line_chart.figure.savefig(line_chart_path)
    # bar_chart.figure.savefig(bar_chart_path)

    fig = px.line(
        x=[c.date for c in stocks],
        y=[c.close for c in stocks],
        title="Stocks by dates",
        labels={"x": "Date", "y": "Close"},
    )

    fig.update_layout(title={"font_size": 22, "xanchor": "center", "x": 0.5})

    chart = fig.to_html()
    context = {"chart": chart, "stocks": stocks}

    return render(request, "index.html", context)


def create_stock(request):
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = StockForm()
    return render(request, "create_stock.html", {"form": form})


def update_stock(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    if request.method == "POST":
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = StockForm(instance=stock)
    return render(request, "update_stock.html", {"form": form})


def delete_stock(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    if request.method == "POST":
        stock.delete()
        return redirect("index")
    return render(request, "delete_stock.html", {"stock": stock})
