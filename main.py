import schedule, requests

def to_do():
    # todo_dict = {
    #     '08:00' : 'Get Up',
    #     '08:30' : 'Breakfast',
    #     '09:00' : 'Go Work',
    #     '12:00' : 'Lanch',
    #     '18:00' : 'Go Home'
    # }

    # print("Day's Tasks")
    # for time, do in todo_dict.items():
    #     print(time, do)
    print("Здраствуйте, сегодня у вас урок в 20:00")
    response = requests.get('https://yobit.net/api/3/ticker/btc_usd').json()
    btc_price = response.get('btc_usd').get('last')
    print(f"{round(btc_price, 3)}$")

def main():
    # schedule.every(1).seconds.do(to_do)
    # schedule.every(1).minutes.do(to_do)
    # schedule.every().hour.do(to_do)

    # schedule.every().day.at('20:55').do(to_do)
    # schedule.every().wednesday.at('20:57').do(to_do)
    # schedule.every().wednesday.at('21:01').do(to_do).saturday.at('21:01').do(to_do)
    # to_do()
    while True:
        schedule.run_pending()

main()