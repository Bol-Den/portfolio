from db_config.get_data_from_db import get_data

df = get_data("investments_portfolio", "trades")
print(type(df))



