from scripts.extract import get_db_connection

def load_analytical_data(df, table_name="dim_monthly_sales_summary"):
    """Loads transformed dataframe back into the reporting layer."""
    print(f"[Load] Writing processed data to table: {table_name}...")
    engine = get_db_connection()
    
    # to_sql handles table creation or appending smoothly
    df.to_sql(
        name=table_name, 
        con=engine, 
        if_exists='replace', 
        index=False
    )
    print("[Load] Target data ingestion complete.")
