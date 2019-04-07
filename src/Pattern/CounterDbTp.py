import pdb

from Pattern.Counter import Counter


class CounterDbTp(Counter):
    '''
    This class represents a trade showing Counter doubletop pattern (inherits from Counter)

    Class variables
    ---------------

    start: datetime, Required
           Time/date when the trade was taken. i.e. 20-03-2017 08:20:00s
    pair: str, Required
          Currency pair used in the trade. i.e. AUD_USD
    timeframe: str, Required
               Timeframe used for the trade. Possible values are: D,H12,H10,H8,H4
    trend_i: datetime, Required
             start of the trend
    type: str, Optional
          What is the type of the trade (long,short)
    SL:  float, Optional
         Stop/Loss price
    TP:  float, Optional
         Take profit price
    SR:  float, Optional
         Support/Resistance area
    bounce_1st : with tuple (datetime,price) containing the datetime
                 and price for this bounce
    bounce_2nd : with tuple (datetime,price) containing the datetime
                 and price for this bounce
    rsi_1st : bool, Optional
              Is price in overbought/oversold
              area in first peak
    rsi_2nd : bool, Optional
              Is price in overbought/oversold
              area in second peak
    n_rsibounces : int, Optional
                  Number of rsi bounces for trend conducting to 1st bounce
    slope: float, Optional
           Float with the slope of trend conducting to 1st bounce
    '''

    def __init__(self, pair, start, **kwargs):

        self.start = start

        allowed_keys = ['timeframe', 'period', 'trend_i', 'type', 'SL',
                        'TP', 'SR']
        self.__dict__.update((k, v) for k, v in kwargs.items() if k in allowed_keys)
        super().__init__(pair)

    def set_1stbounce(self):
        '''
        Function to set bounce_1st (the one that is before the most recent)
        and rsi_1st class attributes

        Returns
        -------
        Nothing
        '''

        self.set_bounces(part='openAsk')
        self.bounce_1st=self.bounces[-2]

        # now check rsi for this bounce
        candle = self.clist_period.fetch_by_time(self.bounce_1st[0])

        isonrsi = False

        if candle.rsi >= 70 or candle.rsi <= 30:
            isonrsi = True

        self.rsi_1st = isonrsi

    def set_2ndbounce(self):
        '''
        Function to set bounce_2nd (the one that is the most recent)
        and rsi_2nd class attributes

        Returns
        -------
        Nothing
        '''

        self.set_bounces(part='openAsk')
        self.bounce_2nd=self.bounces[-1]

        # now check rsi for this bounce
        candle = self.clist_period.fetch_by_time(self.bounce_2nd[0])

        isonrsi = False

        if candle.rsi >= 70 or candle.rsi <= 30:
            isonrsi = True

        self.rsi_2nd = isonrsi

    def init_feats(self):
        '''
        Function to initialise all object features

        Returns
        -------
        It will initialise all object's features
        '''
        self.set_lasttime()
        self.set_bounces()
        self.bounces_fromlasttime()
        self.set_entry_onrsi()

    def init_trend_feats(self):
        '''
        Function to initialize the features for
        trend going from 'trend_i' to 'bounce_1st'

        Returns
        -------
        Nothing
        '''

        c = Counter(
            start=str(self.bounce_1st[0]),
            pair=self.pair,
            timeframe=self.timeframe,
            type=self.type,
            period=1000,
            SR=self.SR,
            SL=self.SL,
            TP=self.TP,
            trend_i=str(self.trend_i))

        c.init_feats()

        self.n_rsibounces=c.n_rsibounces
        self.slope=c.slope
        pdb.set_trace()
        print("h")