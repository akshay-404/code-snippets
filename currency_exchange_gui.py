import requests as rq
from tkinter import *
from tkinter import ttk
import os
import time
import json
import re

# --- Change file path ---
file_path = r'Git\code-snippets\additional-files\api_keys.json'
api = 'openexchangerates'

'''
Generate your own api key from https://openexchangerates.org/signup/.
Store it in a .json file with {api} as key-value pair.
'''
if os.path.isfile(file_path):
    with open(file_path) as file:
        api_key = json.load(file).get(api)
        if not api_key:
            raise KeyError(f'API key for \'{api}\' not found in \'{os.path.basename(file_path)}\'.')
else:
    raise FileNotFoundError(f'File \'{os.path.basename(file_path)}\' does not exist.')

url = f'https://openexchangerates.org/api/latest.json?app_id={api_key}'
# --- Change file path ---
data_file = f'Git\\code-snippets\\additional-files\\{api}.json'

def getData(data_file, url):
    try:
        global timeUp
        response = rq.get(url)
        print(f'Response : {response}')
        if response.status_code == 200:
            with open(data_file, 'w') as file:
                json.dump(response.json(), file)
            data['timestamp'] = response.json().get('timestamp')
            update_time()
        else:
            if not os.path.isfile(data_file):
                raise RuntimeError(f'{api} api error occured')
    except rq.exceptions.ConnectionError as e:
        print(e)

def updateData(data: dict, updatebefore = 4*3600, url=url):
    lastmodified = data.get('timestamp')
    if time.time() - lastmodified > updatebefore:
        getData(data_file, url)

if os.path.isfile(data_file):
    with open(data_file) as file:
        data = json.load(file)
    updateData(data)
else:
    getData(data_file, url)

exchange_rates = data.get('rates')
currency_names = {
    'AED': 'United Arab Emirates Dirham', 'AFN': 'Afghan Afghani', 'ALL': 'Albanian Lek', 'AMD': 'Armenian Dram', 
    'ANG': 'Netherlands Antillean Guilder', 'AOA': 'Angolan Kwanza', 'ARS': 'Argentine Peso', 'AUD': 'Australian Dollar', 
    'AWG': 'Aruban Florin', 'AZN': 'Azerbaijani Manat', 'BAM': 'Bosnia-Herzegovina Convertible Mark', 'BBD': 'Barbadian Dollar', 
    'BDT': 'Bangladeshi Taka', 'BGN': 'Bulgarian Lev', 'BHD': 'Bahraini Dinar', 'BIF': 'Burundian Franc', 
    'BMD': 'Bermudian Dollar', 'BND': 'Brunei Dollar', 'BOB': 'Bolivian Boliviano', 'BRL': 'Brazilian Real', 
    'BSD': 'Bahamian Dollar', 'BTC': 'Bitcoin', 'BTN': 'Bhutanese Ngultrum', 'BWP': 'Botswana Pula', 
    'BYN': 'Belarusian Ruble', 'BZD': 'Belize Dollar', 'CAD': 'Canadian Dollar', 'CDF': 'Congolese Franc', 
    'CHF': 'Swiss Franc', 'CLF': 'Chilean Unit of Account (UF)', 'CLP': 'Chilean Peso', 'CNH': 'Chinese Yuan (Offshore)', 
    'CNY': 'Chinese Yuan', 'COP': 'Colombian Peso', 'CRC': 'Costa Rican Colón', 'CUC': 'Cuban Convertible Peso', 
    'CUP': 'Cuban Peso', 'CVE': 'Cape Verdean Escudo', 'CZK': 'Czech Republic Koruna', 'DJF': 'Djiboutian Franc', 
    'DKK': 'Danish Krone', 'DOP': 'Dominican Peso', 'DZD': 'Algerian Dinar', 'EGP': 'Egyptian Pound', 
    'ERN': 'Eritrean Nakfa', 'ETB': 'Ethiopian Birr', 'EUR': 'Euro', 'FJD': 'Fijian Dollar', 
    'FKP': 'Falkland Islands Pound', 'GBP': 'British Pound Sterling', 'GEL': 'Georgian Lari', 'GGP': 'Guernsey Pound', 
    'GHS': 'Ghanaian Cedi', 'GIP': 'Gibraltar Pound', 'GMD': 'Gambian Dalasi', 'GNF': 'Guinean Franc', 
    'GTQ': 'Guatemalan Quetzal', 'GYD': 'Guyanaese Dollar', 'HKD': 'Hong Kong Dollar', 'HNL': 'Honduran Lempira', 
    'HRK': 'Croatian Kuna', 'HTG': 'Haitian Gourde', 'HUF': 'Hungarian Forint', 'IDR': 'Indonesian Rupiah', 
    'ILS': 'Israeli New Sheqel', 'IMP': 'Isle of Man Pound', 'INR': 'Indian Rupee', 'IQD': 'Iraqi Dinar', 
    'IRR': 'Iranian Rial', 'ISK': 'Icelandic Króna', 'JEP': 'Jersey Pound', 'JMD': 'Jamaican Dollar', 
    'JOD': 'Jordanian Dinar', 'JPY': 'Japanese Yen', 'KES': 'Kenyan Shilling', 'KGS': 'Kyrgystani Som', 
    'KHR': 'Cambodian Riel', 'KMF': 'Comorian Franc', 'KPW': 'North Korean Won', 'KRW': 'South Korean Won', 
    'KWD': 'Kuwaiti Dinar', 'KYD': 'Cayman Islands Dollar', 'KZT': 'Kazakhstani Tenge', 'LAK': 'Laotian Kip', 
    'LBP': 'Lebanese Pound', 'LKR': 'Sri Lankan Rupee', 'LRD': 'Liberian Dollar', 'LSL': 'Lesotho Loti', 
    'LYD': 'Libyan Dinar', 'MAD': 'Moroccan Dirham', 'MDL': 'Moldovan Leu', 'MGA': 'Malagasy Ariary', 
    'MKD': 'Macedonian Denar', 'MMK': 'Myanma Kyat', 'MNT': 'Mongolian Tugrik', 'MOP': 'Macanese Pataca', 
    'MRU': 'Mauritanian Ouguiya', 'MUR': 'Mauritian Rupee', 'MVR': 'Maldivian Rufiyaa', 'MWK': 'Malawian Kwacha', 
    'MXN': 'Mexican Peso', 'MYR': 'Malaysian Ringgit', 'MZN': 'Mozambican Metical', 'NAD': 'Namibian Dollar', 
    'NGN': 'Nigerian Naira', 'NIO': 'Nicaraguan Córdoba', 'NOK': 'Norwegian Krone', 'NPR': 'Nepalese Rupee', 
    'NZD': 'New Zealand Dollar', 'OMR': 'Omani Rial', 'PAB': 'Panamanian Balboa', 'PEN': 'Peruvian Nuevo Sol', 
    'PGK': 'Papua New Guinean Kina', 'PHP': 'Philippine Peso', 'PKR': 'Pakistani Rupee', 'PLN': 'Polish Zloty', 
    'PYG': 'Paraguayan Guarani', 'QAR': 'Qatari Rial', 'RON': 'Romanian Leu', 'RSD': 'Serbian Dinar', 
    'RUB': 'Russian Ruble', 'RWF': 'Rwandan Franc', 'SAR': 'Saudi Riyal', 'SBD': 'Solomon Islands Dollar', 
    'SCR': 'Seychellois Rupee', 'SDG': 'Sudanese Pound', 'SEK': 'Swedish Krona', 'SGD': 'Singapore Dollar', 
    'SHP': 'Saint Helena Pound', 'SLL': 'Sierra Leonean Leone', 'SOS': 'Somali Shilling', 'SRD': 'Surinamese Dollar', 
    'SSP': 'South Sudanese Pound', 'STD': 'São Tomé and Príncipe Dobra (pre-2018)', 'STN': 'São Tomé and Príncipe Dobra', 
    'SVC': 'Salvadoran Colón', 'SYP': 'Syrian Pound', 'SZL': 'Swazi Lilangeni', 'THB': 'Thai Baht', 
    'TJS': 'Tajikistani Somoni', 'TMT': 'Turkmenistani Manat', 'TND': 'Tunisian Dinar', 'TOP': 'Tongan Paanga', 
    'TRY': 'Turkish Lira', 'TTD': 'Trinidad and Tobago Dollar', 'TWD': 'New Taiwan Dollar', 'TZS': 'Tanzanian Shilling', 
    'UAH': 'Ukrainian Hryvnia', 'UGX': 'Ugandan Shilling', 'USD': 'United States Dollar', 'UYU': 'Uruguayan Peso', 
    'UZS': 'Uzbekistan Som', 'VES': 'Venezuelan Bolívar Soberano', 'VND': 'Vietnamese Dong', 'VUV': 'Vanuatu Vatu', 
    'WST': 'Samoan Tala', 'XAF': 'CFA Franc BEAC', 'XAG': 'Silver (troy ounce)', 'XAU': 'Gold (troy ounce)', 
    'XCD': 'East Caribbean Dollar', 'XDR': 'Special Drawing Rights', 'XOF': 'CFA Franc BCEAO', 'XPD': 'Palladium (troy ounce)', 
    'XPF': 'CFP Franc', 'XPT': 'Platinum (troy ounce)', 'YER': 'Yemeni Rial', 'ZAR': 'South African Rand', 
    'ZMW': 'Zambian Kwacha', 'ZWL': 'Zimbabwean Dollar'
}
value = [f'{x} - {y}' for x, y in list(zip(currency_names.keys(), currency_names.values()))]

rate = lambda ip, op: exchange_rates[op] / exchange_rates[ip]

root = Tk()
root.title('Open Exchange Rates')
root.resizable(False, False)
# --- Change file path ---
root.iconbitmap(r'Git\code-snippets\additional-files\exchange_icon_129243.ico')

title = Label(root, text='Currency Exchange Rate Calculator', font=('Helvetica', 20, 'bold'))
title.grid(column=0, row=0, columnspan=5, pady=(5,5))

list_1 = ttk.Combobox(root, values=value, font=('Helvetica', 18, 'normal'), state='readonly')
list_1.set('Select a currency...')
list_1.grid(column=0, row=1, columnspan=2)
list_2 = ttk.Combobox(root, values=value, font=('Helvetica', 18, 'normal'), state='readonly')
list_2.set('Select a currency...')
list_2.grid(column=0, row=2, columnspan=2)

validate = lambda value: bool(re.fullmatch(r'^\d*\.?\d{0,3}$', value))
validate_cmd = root.register(validate)

entry1Var, entry2Var = DoubleVar(), DoubleVar()
entry_1 = Entry(root, font=('Helvetica', 18, 'bold'), textvariable=entry1Var, state='disabled', validate='key', validatecommand=(validate_cmd, '%P'))
entry_1.grid(column=2, row=1, columnspan=2)
entry_2 = Entry(root, font=('Helvetica', 18, 'bold'), textvariable=entry2Var, state='disabled', validate='key', validatecommand=(validate_cmd, '%P'))
entry_2.grid(column=2, row=2, columnspan=2)

def assign(event=None):
    try:
        global ip_var, op_var, ip_box, op_box
        ip_var, ip_box = (entry1Var, list_1) if root.focus_get() == entry_1 else (entry2Var, list_2)
        op_var, op_box = (entry2Var, list_2) if ip_var == entry1Var else (entry1Var, list_1)
    except KeyError:
        pass

root.bind_all('<FocusIn>', assign)

def main(*args):
    try:
        global ip_var, op_var, ip_box, op_box
        if list_1.get() != 'Select a currency...':
            entry_1.configure(state='normal')
        if list_2.get() != 'Select a currency...':
            entry_2.configure(state='normal')
        ip, op = ip_box.get().split()[0], op_box.get().split()[0]
        op_var.set(round(ip_var.get() * rate(ip, op), 3))
    except KeyError or TclError:
        pass

entry1Var.trace_add('write', main)
entry2Var.trace_add('write', main)

list_1.bind('<<ComboboxSelected>>', main)
list_2.bind('<<ComboboxSelected>>', main)

updateButton = Button(root, text='Update',  command=lambda: getData(data_file, url), font=("consolas", 16, 'bold'))
updateButton.grid(column=0, row=3, columnspan=2, sticky='ew')
exitButton = Button(root, text='Exit',  command=root.quit, font=("consolas", 16, 'bold'))
exitButton.grid(column=2, row=3, columnspan=2, sticky='ew')

timeUp = StringVar()
timeUp.set(f'Last Updated : {time.strftime("%H:%M:%S - %b %d %Y", time.localtime(data["timestamp"]))} ({api})')

def update_time():
    timeUp.set(f'Last Updated : {time.strftime("%H:%M:%S - %b %d %Y", time.localtime(data["timestamp"]))} ({api})')

modifiedTime = Label(root, textvariable=timeUp, font=('Consolas', 10), )
modifiedTime.grid(column=0, row=4, columnspan=4, pady=(5,5))

root.mainloop()