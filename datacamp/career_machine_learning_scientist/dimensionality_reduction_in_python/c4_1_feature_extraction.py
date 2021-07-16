from data import load_sales_data, load_ansur_ii_male_data


def manual_feature_extraction(sales_df):
    # Calculate the price from the quantity sold and revenue
    sales_df['price'] = sales_df.revenue / sales_df.quantity
    # Drop the quantity and revenue features
    reduced_df = sales_df.drop(["revenue", "quantity"], axis=1)
    print(reduced_df.head())


def manual_feature_extraction2(ansur_df):
    cols = ["acromialheight", "axillaheight", "sittingheight"]
    height_df = ansur_df[cols]
    height_df.rename(columns={
        "acromialheight": "height_1",
        "axillaheight": "height_2",
        "sittingheight": "height_3"
    }, inplace=True)
    # Calculate the mean height
    height_df['height'] = height_df[[
        "height_1", "height_2", "height_3"]].mean(axis=1)
    # Drop the 3 original height features
    reduced_df = height_df.drop(["height_1", "height_2", "height_3"], axis=1)
    print(reduced_df.head())


# sales_df = load_sales_data()
# manual_feature_extraction(sales_df)

ansur_df = load_ansur_ii_male_data()
manual_feature_extraction2(ansur_df)
