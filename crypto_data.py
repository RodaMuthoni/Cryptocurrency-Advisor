"""
Sample cryptocurrency dataset for the CryptoBuddy advisor chatbot.
This module contains data about various cryptocurrencies with their properties.
"""

# Sample cryptocurrency dataset with properties relevant for investment advice
cryptocurrencies = [
    {
        "name": "Bitcoin",
        "symbol": "BTC",
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 0.4,
        "description": "The original cryptocurrency, known for its first-mover advantage and high adoption rate."
    },
    {
        "name": "Ethereum",
        "symbol": "ETH",
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 0.6,
        "description": "Smart contract platform transitioning to a more energy-efficient proof-of-stake model."
    },
    {
        "name": "Cardano",
        "symbol": "ADA",
        "price_trend": "stable",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 0.8,
        "description": "Research-driven blockchain using proof-of-stake with focus on sustainability and scalability."
    },
    {
        "name": "Solana",
        "symbol": "SOL",
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 0.75,
        "description": "High-performance blockchain with fast transactions and low energy consumption."
    },
    {
        "name": "Polkadot",
        "symbol": "DOT",
        "price_trend": "stable",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 0.82,
        "description": "Multi-chain network enabling cross-blockchain transfers and interoperability."
    },
    {
        "name": "Algorand",
        "symbol": "ALGO",
        "price_trend": "rising",
        "market_cap": "low",
        "energy_use": "low",
        "sustainability_score": 0.9,
        "description": "Carbon-negative blockchain focusing on sustainable practices and efficiency."
    },
    {
        "name": "Tezos",
        "symbol": "XTZ",
        "price_trend": "stable",
        "market_cap": "low",
        "energy_use": "low",
        "sustainability_score": 0.85,
        "description": "Self-amending blockchain with a focus on governance and energy efficiency."
    },
    {
        "name": "Dogecoin",
        "symbol": "DOGE",
        "price_trend": "falling",
        "market_cap": "medium",
        "energy_use": "medium",
        "sustainability_score": 0.5,
        "description": "Meme-inspired cryptocurrency with a large community following."
    },
    {
        "name": "Avalanche",
        "symbol": "AVAX",
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 0.78,
        "description": "High-throughput blockchain platform with fast finality and eco-friendly consensus."
    },
    {
        "name": "Stellar",
        "symbol": "XLM",
        "price_trend": "stable",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 0.88,
        "description": "Payment-focused blockchain with minimal energy consumption and fast transactions."
    },
    {
        "name": "Cosmos",
        "symbol": "ATOM",
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 0.83,
        "description": "Ecosystem of interconnected blockchains with strong sustainability focus."
    },
    {
        "name": "Hedera",
        "symbol": "HBAR",
        "price_trend": "stable",
        "market_cap": "low",
        "energy_use": "low",
        "sustainability_score": 0.92,
        "description": "Enterprise-grade public network with extremely low energy consumption."
    },
    {
        "name": "Binance Coin",
        "symbol": "BNB",
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 0.65,
        "description": "Native token of the Binance ecosystem with high trading volume."
    },
    {
        "name": "Ripple",
        "symbol": "XRP",
        "price_trend": "falling",
        "market_cap": "high",
        "energy_use": "low",
        "sustainability_score": 0.79,
        "description": "Digital payment protocol focusing on financial institution transfers."
    },
    {
        "name": "Near Protocol",
        "symbol": "NEAR",
        "price_trend": "rising",
        "market_cap": "low",
        "energy_use": "low",
        "sustainability_score": 0.87,
        "description": "Developer-friendly blockchain with carbon-neutral operations."
    }
]

def get_all_cryptocurrencies():
    """Return the complete list of cryptocurrencies."""
    return cryptocurrencies

def get_cryptocurrency_by_name(name):
    """Find and return a cryptocurrency by its name."""
    for crypto in cryptocurrencies:
        if crypto["name"].lower() == name.lower():
            return crypto
    return None

def get_cryptocurrency_by_symbol(symbol):
    """Find and return a cryptocurrency by its symbol."""
    for crypto in cryptocurrencies:
        if crypto["symbol"].lower() == symbol.lower():
            return crypto
    return None