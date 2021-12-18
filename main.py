from Scraper import FinViz
import json
from tqdm import tqdm

def read_tickers(DIR):
    with open(DIR) as file:
        lines = file.readlines()
        ticker_list = [line.rstrip().lower() for line in lines]
        return ticker_list

if __name__ == '__main__':
    tickers = read_tickers('data/tickers')
    news = {}
    print('--- pulling tickers ---')
    for ticker in tqdm(tickers):
        df = FinViz.get_news(ticker)
        news[ticker] = df.values.tolist()[1:]
    print('--- done ---')

    print('--- saving ---')
    with open('data/past_100_news_per_ticker.json', 'w') as f:
        json.dump(news, f, indent=4)
    print('Done!')