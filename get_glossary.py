import pandas as pd

def get_glossary(currency):
    df = pd.read_json('https://api.exchangerate.host/symbols')
    df = df.reset_index()
    df.drop([0,1], axis=0, inplace=True)
    df = df.reset_index(drop=True)
    df = df.drop(columns=['motd', 'success'])
    return((df.loc[df['index'] == currency].reset_index(drop=True))['symbols'][0]['description'])
