from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

# # Create your views here.
import requests

from .models import Stocks, UserInfo, UserStock, Transaction, Watchlist
import threading

webscoket_api_key = 'd1hqgb1r01qsvr2bqhc0d1hqgb1r01qsvr2bqhcg'
#

# def fun(request) :
#     page  = '''
#     <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Title</title>
# </head>
# <body>
# <h1>Stock Market App</h1>
# <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Blanditiis commodi dignissimos dolor, ducimus enim harum in ipsum iure laboriosam minus, natus odit officiis omnis optio quibusdam quo, sapiente sunt voluptatibus!</p>
# <ul>
#     <li>s1</li>
#     <li>s2</li>
#     <li>s3</li>
# </ul>
# </body>
# </html>
#     '''
#     return  HttpResponse(page)

@login_required
def index(request):
    user = request.user
    user_stocks = UserStock.objects.select_related('stock').filter(user=user)

    total_value = 0
    invested = 0

    for item in user_stocks:
        stock_value = item.purchase_quantity * item.stock.curr_price
        invested_value = item.purchase_quantity * item.purchase_price

        total_value += stock_value
        invested += invested_value
        item.total_value = stock_value

    gains = ((total_value - invested) / invested) * 100 if invested != 0 else 0

    context = {
        'data': user_stocks,
        'total_value': total_value,
        'invested': invested,
        'gains': round(gains, 2),
    }

    return render(request, 'index.html', context)

def getData(request) :
    nasdaq_tickers = [
        "AAPL",  # Apple Inc.
        "MSFT",  # Microsoft Corporation
        "GOOGL",  # Alphabet Inc. (Class A)
        "GOOG",  # Alphabet Inc. (Class C)
        "AMZN",  # Amazon.com Inc.
        "META",  # Meta Platforms Inc.
        "NVDA",  # NVIDIA Corporation
        "TSLA",  # Tesla Inc.
        "PEP",  # PepsiCo Inc.
        "INTC",  # Intel Corporation
        "CSCO",  # Cisco Systems Inc.
        "ADBE",  # Adobe Inc.
        "CMCSA",  # Comcast Corporation
        "AVGO",  # Broadcom Inc.
        "COST",  # Costco Wholesale Corporation
        "TMUS",  # T-Mobile US Inc.
        "TXN",  # Texas Instruments Inc.
        "AMGN",  # Amgen Inc.
        "QCOM",  # Qualcomm Incorporated
        "INTU",  # Intuit Inc.
        "PYPL",  # PayPal Holdings Inc.
        "BKNG",  # Booking Holdings Inc.
        "GILD",  # Gilead Sciences Inc.
        "SBUX",  # Starbucks Corporation
        "MU",  # Micron Technology Inc.
        "ADP",  # Automatic Data Processing Inc.
        "MDLZ",  # Mondelez International Inc.
        "ISRG",  # Intuitive Surgical Inc.
        "ADI",  # Analog Devices Inc.
        "MAR",  # Marriott International Inc.
        "LRCX",  # Lam Research Corporation
        "REGN",  # Regeneron Pharmaceuticals Inc.
        "ATVI",  # Activision Blizzard Inc.
        "ILMN",  # Illumina Inc.
        "WDAY",  # Workday Inc.
        "SNPS",  # Synopsys Inc.
        "ASML",  # ASML Holding N.V.
        "EBAY",  # eBay Inc.
        "ROST",  # Ross Stores Inc.
        "CTAS",  # Cintas Corporation
        "BIIB",  # Biogen Inc.
        "MELI",  # MercadoLibre Inc.
        "ORLY",  # O'Reilly Automotive Inc.
        "VRTX",  # Vertex Pharmaceuticals Inc.
        "DLTR",  # Dollar Tree Inc.
        "KHC",  # The Kraft Heinz Company
        "EXC",  # Exelon Corporation
        "FAST",  # Fastenal Company
        "JD",  # JD.com Inc.
        "CRWD"  # CrowdStrike Holdings Inc.
    ]

    headers = {
        'Content-Type': 'application/json'
    }
    token  =  "fced443141e501d554d0b38c4a34bba085172b1e"
    def getStock(ticker):
        url  = f"https://api.tiingo.com/tiingo/daily/{ticker}?token={token}"
        priceurl  =  f"https://api.tiingo.com/tiingo/daily/{ticker}/prices?token={token}"
        requestResponse = requests.get(url, headers=headers )
        Metadata  = requestResponse.json()
        print(Metadata)
        priceData  = requests.get(priceurl , headers=headers)
        print(priceData.json())
        priceData =  priceData.json()[0]['close']

        # insert into SQL
        stock = Stocks(ticker  = Metadata['ticker']  , name  =  Metadata['name'] ,  description =  Metadata['description'] , curr_price  = priceData)
        stock.save()

    nasdaq_tickers =  nasdaq_tickers[11:30]
    for i in nasdaq_tickers :
        getStock(i)


    return HttpResponse("Stock Data Downloaded")


@login_required
def stocks(request):
    q = request.GET.get('q')
    if q:
        stock_list = Stocks.objects.filter(name__icontains=q).order_by('id') 
    else:
        stock_list = Stocks.objects.all().order_by('id') 

    paginator = Paginator(stock_list, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'data': page_obj,
    }
    return render(request, 'market.html', context)


def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid credentials")

    return render(request, 'login.html')


def logoutView(request) :
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        first_name  =  request.POST.get('first_name')
        last_name  = request.POST.get('last_name')

        address =   request.POST.get('address')
        panCard = request.POST.get('panCard')
        phoneNumber = request.POST.get('phoneNumber')
        profile_pic = request.FILES.get('profile_pic')
        panCard_Image = request.FILES.get('panCard_Image')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'register.html')


        user = User(username=username, email=email , first_name = first_name ,  last_name = last_name)
        user.set_password(password)
        user.save()


        user_info = UserInfo(
            user=user,
            pancard_number =panCard,
            address = address ,
            phone_number=phoneNumber,
            user_image=profile_pic,
            pancard_image=panCard_Image,
        )
        user_info.save()

        login(request, user)

        t1 = threading.Thread(
            target=send_email_async,
            kwargs={
                "subject": " Registration sucessfull",
                "message": f"Dear {user, username} welcome to our platfrom ",
                "from_email": None,
                "recipient_list": [user.email],
            }
        )
        t1.start()

        return redirect('index')

    return render(request, 'register.html')



@login_required
def buy(request , id) :
    stock  = get_object_or_404(Stocks ,  id =  id)
    user =  request.user
    purchase_quantity = int(request.POST.get('quantity'))
    purchase_price =   stock.curr_price
    print(purchase_price)


    # UserStock is an exmaple of Composite Keys in DBMS (user , stock) --> candidate key
    userStocks = UserStock.objects.filter(stock  =  stock   ,  user  =  user).first()
    if userStocks :
        userStocks.purchase_price = (userStocks.purchase_quantity*userStocks.purchase_price  +  purchase_price*purchase_quantity) / (purchase_quantity + userStocks.purchase_quantity)
        userStocks.purchase_quantity =  userStocks.purchase_quantity +  purchase_quantity
        userStocks.save()
    else  :
        userStock = UserStock(stock  = stock ,  user = user  ,  purchase_price =  purchase_price ,  purchase_quantity =  purchase_quantity )
        userStock.save()

    Transaction.objects.create(
        user=user,
        stock_symbol=stock.ticker,
        stock_name=stock.name,
        quantity=purchase_quantity,
        price=purchase_price,
        type='BUY'
    )

    t1 = threading.Thread(
        target=send_email_async,
        kwargs={
            "subject": "Buy Option executed successfully",
            "message": f"Your purchase of stock {stock.name} was successful",
            "from_email": None,
            "recipient_list": [user.email],
        }
    )
    t1.start()
    return redirect('index')



def  sell(request , id) :
    stock = get_object_or_404(Stocks, id=id)
    user = request.user
    sell_quantity = int(request.POST.get('quantity'))
    userStock  =  UserStock.objects.filter(stock  =  stock ,  user =  user).first()

    if userStock.purchase_quantity <  sell_quantity :
        messages.error(request, "Can't sell more than you own")
        return redirect('market')

    userStock.purchase_quantity -= sell_quantity
    userStock.save()

    Transaction.objects.create(
        user=user,
        stock_symbol=stock.ticker,
        stock_name=stock.name,
        quantity=sell_quantity,
        price=stock.curr_price,
        type='SELL'
    )

    t1 = threading.Thread(
        target=send_email_async,
        kwargs={
            "subject": "Sell Option executed successfully",
            "message": f"Your sale of stock {stock.name} was successful",
            "from_email": None,
            "recipient_list": [user.email],
        }
    )
    t1.start()

    return redirect('index')




def send_email_async(subject  ,  message  ,  from_email , recipient_list ) :
    send_mail(subject  =  subject ,  message =  message ,  from_email= from_email , recipient_list = recipient_list )



@login_required
def transaction_history(request):
    transactions = Transaction.objects.filter(user=request.user).order_by("-date")
    context = {
        "transactions": transactions
    }
    return render(request, "transaction_history.html", context)




@login_required
def portfolio_dashboard(request):
    user = request.user
    transactions = Transaction.objects.filter(user=user)

    portfolio = {}
    for t in transactions:
        if t.stock_symbol not in portfolio:
            portfolio[t.stock_symbol] = {
                'stock_name': t.stock_name,
                'quantity': 0,
                'invested_value': 0.0,
                'current_price': 0.0, # This will be updated if live prices are integrated
            }
        if t.type == 'BUY':
            portfolio[t.stock_symbol]['quantity'] += t.quantity
            portfolio[t.stock_symbol]['invested_value'] += t.quantity * t.price
        elif t.type == 'SELL':
            portfolio[t.stock_symbol]['quantity'] -= t.quantity
            portfolio[t.stock_symbol]['invested_value'] -= t.quantity * t.price # This might need more sophisticated calculation for average cost

    # Remove stocks with zero quantity (if any after buy/sell)
    portfolio = {symbol: data for symbol, data in portfolio.items() if data['quantity'] > 0}

    # Optional: Integrate with a live stock price API (like yfinance)
    # For now, we'll use the last known price from transactions or a placeholder
    for symbol, data in portfolio.items():
        latest_transaction = transactions.filter(stock_symbol=symbol).order_by('-date').first()
        if latest_transaction:
            data['current_price'] = latest_transaction.price # Placeholder: use last transaction price
        data['current_value'] = data['quantity'] * data['current_price']

    total_portfolio_value = sum(item['current_value'] for item in portfolio.values())
    total_invested_capital = sum(item['invested_value'] for item in portfolio.values())

    context = {
        'portfolio': portfolio,
        'total_portfolio_value': total_portfolio_value,
        'total_invested_capital': total_invested_capital,
    }
    return render(request, 'portfolio_dashboard.html', context)


@login_required
def watchlist_view(request):
    watchlist_items = Watchlist.objects.filter(user=request.user)
    context = {
        "watchlist_items": watchlist_items
    }
    return render(request, "watchlist.html", context)

@login_required
def add_to_watchlist(request, stock_symbol):
    stock = get_object_or_404(Stocks, ticker=stock_symbol)
    Watchlist.objects.get_or_create(user=request.user, stock_symbol=stock.ticker, stock_name=stock.name)
    messages.success(request, f"{stock.name} added to watchlist.")
    return redirect("stocks")

@login_required
def remove_from_watchlist(request, stock_symbol):
    stock = get_object_or_404(Stocks, ticker=stock_symbol)
    Watchlist.objects.filter(user=request.user, stock_symbol=stock.ticker).delete()
    messages.success(request, f"{stock.name} removed from watchlist.")
    return redirect("watchlist_view")


