#!/usr/bin/env python3
"""
CryptoBuddy: A beginner-friendly rule-based chatbot for cryptocurrency advice.
This script creates a simple cryptocurrency advisor that responds to user queries
with investment suggestions based on profitability and sustainability metrics.
"""

import sys
import time
from crypto_data import get_all_cryptocurrencies
from crypto_advisor import (
    get_trending_cryptocurrencies,
    get_sustainable_cryptocurrencies,
    get_profitable_cryptocurrencies,
    get_longterm_cryptocurrencies,
    format_crypto_list
)
from console_colors import bold, green, yellow, blue, cyan, red, magenta

def print_with_delay(text, delay=0.03):
    """Print text with a typing effect for better UX."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def display_greeting():
    """Display a friendly greeting message to the user."""
    greeting = f"""
{bold(green('🤖 Welcome to CryptoBuddy! 🤖'))}
Your friendly cryptocurrency investment advisor.

I can help you find cryptocurrencies based on:
  📈 {yellow('Profitability')} (price trends and market cap)
  🌱 {green('Sustainability')} (energy usage and environmental impact)
  🔮 {blue('Long-term growth potential')}

{bold('Try asking me:')}
  • Which crypto is trending up?
  • What's the most sustainable coin?
  • Which crypto is best for long-term growth?
  • Show me profitable cryptocurrencies
  • Help or ? for assistance

{bold(red('Disclaimer:'))} Cryptocurrency investments involve significant risks.
This is educational information only. Always do your own research before investing.

{bold('Type "exit" to quit at any time.')}
"""
    print(greeting)

def process_query(query):
    """
    Process user queries and return appropriate responses.
    Uses if-else logic to match queries with cryptocurrency advice.
    """
    query = query.lower().strip()
    
    # Exit command
    if query in ["exit", "quit", "bye"]:
        return None
    
    # Help command
    if query in ["help", "?"]:
        return f"""
{bold('CryptoBuddy Commands:')}
  • {yellow('trending')} or {yellow('trending up')} - Show cryptocurrencies with rising prices
  • {green('sustainable')} - Show environmentally friendly cryptocurrencies
  • {blue('profitable')} - Show potentially profitable cryptocurrencies
  • {magenta('long-term')} or {magenta('growth')} - Show coins good for long-term investment
  • {cyan('list all')} - Show all available cryptocurrencies
  • {bold('exit')} - Quit CryptoBuddy
"""
    
    # Trending cryptocurrencies
    if any(keyword in query for keyword in ["trending", "trend", "rising", "going up"]):
        trending = get_trending_cryptocurrencies()
        if trending:
            response = f"{bold(yellow('📈 Trending Cryptocurrencies:'))}\n\n"
            response += format_crypto_list(trending, "🚀")
            return response
        return "I couldn't find any trending cryptocurrencies at the moment."
    
    # Sustainable cryptocurrencies
    if any(keyword in query for keyword in ["sustainable", "sustainability", "green", "eco", "environment"]):
        sustainable = get_sustainable_cryptocurrencies()
        if sustainable:
            response = f"{bold(green('🌱 Sustainable Cryptocurrencies:'))}\n\n"
            response += format_crypto_list(sustainable, "🌿")
            return response
        return "I couldn't find any highly sustainable cryptocurrencies at the moment."
    
    # Profitable cryptocurrencies
    if any(keyword in query for keyword in ["profitable", "profit", "money", "earn"]):
        profitable = get_profitable_cryptocurrencies()
        if profitable:
            response = f"{bold(blue('💰 Potentially Profitable Cryptocurrencies:'))}\n\n"
            response += format_crypto_list(profitable, "💎")
            return response
        return "I couldn't find any cryptocurrencies that meet high profitability criteria at the moment."
    
    # Long-term growth cryptocurrencies
    if any(keyword in query for keyword in ["long-term", "long term", "growth", "future"]):
        longterm = get_longterm_cryptocurrencies()
        if longterm:
            response = f"{bold(magenta('🔮 Cryptocurrencies for Long-Term Growth:'))}\n\n"
            response += format_crypto_list(longterm, "🌠")
            return response
        return "I couldn't find any cryptocurrencies ideal for long-term growth at the moment."
    
    # List all cryptocurrencies
    if any(keyword in query for keyword in ["list all", "show all", "all crypto"]):
        all_cryptos = get_all_cryptocurrencies()
        response = f"{bold(cyan('📋 All Available Cryptocurrencies:'))}\n\n"
        response += format_crypto_list(all_cryptos, "💰")
        return response
    
    # Fallback response for unknown queries
    return f"""
{yellow("I'm not sure how to answer that question.")} 

Try asking about:
  • Trending cryptocurrencies
  • Sustainable coins
  • Profitable investments
  • Long-term growth options

Or type {bold("help")} for assistance.
"""

def main():
    """Main function to run the CryptoBuddy chatbot."""
    display_greeting()
    
    while True:
        # Get user input
        print(f"\n{bold('CryptoBuddy')} 🤖 > ", end="")
        user_input = input()
        
        # Process the query
        response = process_query(user_input)
        
        # Exit if response is None
        if response is None:
            print(f"\n{bold(green('Thanks for using CryptoBuddy! Happy investing! 💰'))}")
            break
        
        # Display the response
        print()
        print_with_delay(response)

if __name__ == "__main__":
    main()