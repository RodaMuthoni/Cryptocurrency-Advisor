"""
Crypto advisor module for the CryptoBuddy chatbot.
This module contains functions to analyze cryptocurrencies and provide investment advice.
"""

from crypto_data import get_all_cryptocurrencies

def get_trending_cryptocurrencies():
    """
    Find cryptocurrencies with rising price trends.
    Returns a list of cryptocurrencies that are currently trending upward.
    """
    cryptos = get_all_cryptocurrencies()
    return [crypto for crypto in cryptos if crypto["price_trend"] == "rising"]

def get_sustainable_cryptocurrencies():
    """
    Find environmentally sustainable cryptocurrencies.
    Returns cryptocurrencies with low energy use and high sustainability scores.
    """
    cryptos = get_all_cryptocurrencies()
    return [
        crypto for crypto in cryptos 
        if crypto["energy_use"] == "low" and crypto["sustainability_score"] > 0.7
    ]

def get_profitable_cryptocurrencies():
    """
    Find potentially profitable cryptocurrencies.
    Returns cryptocurrencies with rising price trends and high market caps.
    """
    cryptos = get_all_cryptocurrencies()
    return [
        crypto for crypto in cryptos 
        if crypto["price_trend"] == "rising" and crypto["market_cap"] == "high"
    ]

def get_longterm_cryptocurrencies():
    """
    Find cryptocurrencies suitable for long-term growth.
    Combines profitability and sustainability factors.
    """
    cryptos = get_all_cryptocurrencies()
    return [
        crypto for crypto in cryptos 
        if (crypto["market_cap"] in ["high", "medium"]) and
           (crypto["sustainability_score"] > 0.6) and
           (crypto["price_trend"] in ["rising", "stable"])
    ]

def format_crypto_list(cryptos, emoji="💰"):
    """
    Format a list of cryptocurrencies into a readable string.
    Adds emoji and formats each cryptocurrency's details.
    """
    if not cryptos:
        return "No cryptocurrencies match these criteria at the moment."
    
    result = ""
    for crypto in cryptos:
        result += f"{emoji} {crypto['name']} ({crypto['symbol']})\n"
        result += f"   Price Trend: {crypto['price_trend'].capitalize()}\n"
        result += f"   Market Cap: {crypto['market_cap'].capitalize()}\n"
        result += f"   Energy Use: {crypto['energy_use'].capitalize()}\n"
        result += f"   Sustainability: {crypto['sustainability_score'] * 100:.0f}%\n"
        result += f"   {crypto['description']}\n\n"
    
    return result