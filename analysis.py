import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# ============================================================
# 1. LOAD DATA
# ============================================================

reviews = pd.read_excel("Local business audit.xlsx")
menu = pd.read_excel("Local business audit.xlsx", sheet_name="Menu")


# ============================================================
# 2. DATA QUALITY CHECK
# ============================================================

print("========== DATA QUALITY CHECK ==========")

print("Dataset Shape:", reviews.shape)

print("\nColumns:")
print(reviews.columns.tolist())

print("\nMissing Values:")
print(reviews.isna().sum())

print("\nDuplicate Rows:", reviews.duplicated().sum())

print("\nData Types:")
print(reviews.dtypes)


# ============================================================
# 3. BASIC RESTAURANT ANALYSIS
# ============================================================

print("\n========== RESTAURANT ANALYSIS ==========")

restaurant_review_count = (
    reviews["Restaurant"]
    .value_counts()
    .rename("Review_Count")
)

print("\nReview Count:")
print(restaurant_review_count)

avg_ratings = (
    reviews
    .groupby("Restaurant")["Rating"]
    .mean()
    .round(2)
)

print("\nAverage Rating:")
print(avg_ratings)


# ============================================================
# 4. VADER SENTIMENT ANALYSIS
# ============================================================

print("\n========== SENTIMENT ANALYSIS ==========")

analyzer = SentimentIntensityAnalyzer()

reviews["VADER_Score"] = (
    reviews["Review"]
    .apply(lambda x: analyzer.polarity_scores(x)["compound"])
)

reviews["VADER_Sentiment"] = reviews["VADER_Score"].apply(
    lambda x:
        "Positive" if x >= 0.05
        else "Negative" if x <= -0.05
        else "Neutral"
)

print("\nSample VADER Results:")
print(
    reviews[
        ["Rating", "Review", "VADER_Score", "VADER_Sentiment"]
    ].head(10)
)


# ============================================================
# 5. VADER VALIDATION
# ============================================================

print("\n========== VADER VALIDATION ==========")

accuracy = (
    reviews["Sentiment"] == reviews["VADER_Sentiment"]
).mean()

print(
    "VADER Agreement:",
    round(accuracy * 100, 2),
    "%"
)

sentiment_comparison = pd.crosstab(
    reviews["Sentiment"],
    reviews["VADER_Sentiment"]
)

print("\nManual vs VADER Sentiment:")
print(sentiment_comparison)


# ============================================================
# 6. RATING-SENTIMENT MISMATCH
# ============================================================

print("\n========== RATING-SENTIMENT MISMATCH ==========")

mismatch = (
    (
        (reviews["Rating"] <= 2) &
        (reviews["VADER_Sentiment"] == "Positive")
    )
    |
    (
        (reviews["Rating"] >= 4) &
        (reviews["VADER_Sentiment"] == "Negative")
    )
)

reviews["Sentiment_Mismatch"] = mismatch

print(
    "Rating-Sentiment Mismatches:",
    mismatch.sum()
)

print("\nMismatches by Restaurant:")
print(
    reviews[mismatch]["Restaurant"]
    .value_counts()
)

print("\nMismatch Rate by Restaurant:")
mismatch_rate = (
    reviews
    .groupby("Restaurant")["Sentiment_Mismatch"]
    .mean()
    .mul(100)
    .round(2)
)

print(mismatch_rate)


# ============================================================
# 7. COMPLAINT CATEGORY ANALYSIS
# ============================================================

print("\n========== COMPLAINT ANALYSIS ==========")

complaint_counts = (
    reviews["Complaint_Category"]
    .value_counts()
)

print("\nComplaint Category Distribution:")
print(complaint_counts)


complaint_by_restaurant = pd.crosstab(
    reviews["Restaurant"],
    reviews["Complaint_Category"],
    normalize="index"
).mul(100).round(2)

print("\nComplaint Category % by Restaurant:")
print(complaint_by_restaurant)


# ============================================================
# 8. NEGATIVE SENTIMENT BY COMPLAINT CATEGORY
# ============================================================

print("\n========== NEGATIVE SENTIMENT BY CATEGORY ==========")

negative_by_category = (
    pd.crosstab(
        reviews["Complaint_Category"],
        reviews["VADER_Sentiment"],
        normalize="index"
    )
    .mul(100)
    .round(2)
)

print(
    negative_by_category["Negative"]
    .sort_values(ascending=False)
)


# ============================================================
# 9. RESTAURANT + COMPLAINT + NEGATIVE REVIEW ANALYSIS
# ============================================================

print("\n========== PROBLEM ANALYSIS ==========")

problem_analysis = (
    reviews
    .groupby(
        ["Restaurant", "Complaint_Category"]
    )
    .agg(
        Total_Reviews=("Review", "count"),

        Negative_Reviews=(
            "VADER_Sentiment",
            lambda x: (x == "Negative").sum()
        )
    )
    .reset_index()
)

problem_analysis["Negative_%"] = (
    problem_analysis["Negative_Reviews"]
    / problem_analysis["Total_Reviews"]
    * 100
).round(2)

print(problem_analysis.to_string(index=False))


# ============================================================
# 10. LOW-RATING PROBLEM ANALYSIS
# ============================================================

print("\n========== LOW-RATING ANALYSIS ==========")

low_rating_analysis = (
    reviews[reviews["Rating"] <= 2]
    .groupby(
        ["Restaurant", "Complaint_Category"]
    )
    .agg(
        Low_Rating_Reviews=("Review", "count"),

        Negative_VADER=(
            "VADER_Sentiment",
            lambda x: (x == "Negative").sum()
        )
    )
    .reset_index()
)

low_rating_analysis["Negative_%"] = (
    low_rating_analysis["Negative_VADER"]
    / low_rating_analysis["Low_Rating_Reviews"]
    * 100
).round(2)


# Priority score is a project-defined heuristic
# combining problem volume and negative percentage.

low_rating_analysis["Priority_Score"] = (
    low_rating_analysis["Low_Rating_Reviews"]
    * low_rating_analysis["Negative_%"]
).round(2)

print(
    low_rating_analysis
    .sort_values(
        "Priority_Score",
        ascending=False
    )
    .to_string(index=False)
)


# ============================================================
# 11. TOP 3 PROBLEMS PER RESTAURANT
# ============================================================

print("\n========== TOP 3 PROBLEMS ==========")

top_problems = (
    low_rating_analysis
    .sort_values(
        ["Restaurant", "Priority_Score"],
        ascending=[True, False]
    )
    .groupby("Restaurant")
    .head(3)
)

print(
    top_problems.to_string(index=False)
)


# ============================================================
# 12. RATING DISTRIBUTION
# ============================================================

print("\n========== RATING DISTRIBUTION ==========")

rating_distribution = pd.crosstab(
    reviews["Restaurant"],
    reviews["Rating"]
)

print(rating_distribution)


rating_percentage = (
    pd.crosstab(
        reviews["Restaurant"],
        reviews["Rating"],
        normalize="index"
    )
    .mul(100)
    .round(2)
)

print("\nRating Percentage:")
print(rating_percentage)


# ============================================================
# 13. LOW vs HIGH RATING RATE
# ============================================================

rating_summary = (
    reviews
    .groupby("Restaurant")["Rating"]
    .agg(
        Low_Rating_Rate=lambda x: (x <= 2).mean() * 100,
        High_Rating_Rate=lambda x: (x >= 4).mean() * 100
    )
    .round(2)
)

print("\nLow vs High Rating Rate:")
print(rating_summary)


# ============================================================
# 14. NEGATIVE REVIEW % BY RESTAURANT
# ============================================================

negative_by_restaurant = (
    reviews
    .groupby("Restaurant")["VADER_Sentiment"]
    .apply(
        lambda x: (x == "Negative").mean() * 100
    )
    .round(2)
)

print("\nNegative Review %:")
print(negative_by_restaurant)


# ============================================================
# 15. MENU PRICE ANALYSIS
# ============================================================

print("\n========== MENU PRICE ANALYSIS ==========")

restaurant_columns = [
    "Dwaraka Grand",
    "Udupi Swada",
    "Sri Krishna Aramane"
]

avg_prices = (
    menu[restaurant_columns]
    .mean()
    .round(2)
)

print("\nAverage Menu Price:")
print(avg_prices)


# ============================================================
# 16. PRICE PREMIUM
# ============================================================

price_comparison = pd.DataFrame({
    "Average_Price": avg_prices
})

price_comparison["Premium_vs_Cheapest_%"] = (
    (
        price_comparison["Average_Price"]
        / price_comparison["Average_Price"].min()
        - 1
    )
    * 100
).round(2)

print("\nPrice Comparison:")
print(price_comparison)


# ============================================================
# 17. RESTAURANT COMPETITOR BENCHMARK
# ============================================================

benchmark = pd.DataFrame({
    "Average_Price": avg_prices,
    "Average_Rating": avg_ratings,
    "Negative_Review_%": negative_by_restaurant
}).round(2)

print("\n========== COMPETITOR BENCHMARK ==========")

print(benchmark)


# ============================================================
# 18. DISH-LEVEL PRICE COMPARISON
# ============================================================

menu["Dwaraka_vs_Cheapest_%"] = (
    (
        menu["Dwaraka Grand"]
        /
        menu[
            ["Udupi Swada", "Sri Krishna Aramane"]
        ].min(axis=1)
        - 1
    )
    * 100
).round(2)

dish_price_comparison = (
    menu[
        [
            "Menu",
            "Dwaraka Grand",
            "Udupi Swada",
            "Sri Krishna Aramane",
            "Dwaraka_vs_Cheapest_%"
        ]
    ]
    .sort_values(
        "Dwaraka_vs_Cheapest_%",
        ascending=False
    )
)

print("\nDwaraka Dish-Level Price Premium:")
print(
    dish_price_comparison.to_string(index=False)
)


# ============================================================
# 19. FINAL REVIEW ANALYSIS TABLE
# ============================================================

review_analysis = reviews[
    [
        "Review id",
        "Restaurant",
        "Review date",
        "Rating",
        "Reviewer",
        "Review",
        "Complaint_Category",
        "Sentiment",
        "VADER_Score",
        "VADER_Sentiment",
        "Sentiment_Mismatch"
    ]
].copy()


# ============================================================
# 20. EXPORT FINAL TABLES FOR POWER BI
# ============================================================

print("\n========== EXPORTING FILES ==========")

benchmark.to_csv(
    "restaurant_benchmark.csv"
)

problem_analysis.to_csv(
    "problem_analysis.csv",
    index=False
)

rating_summary.to_csv(
    "rating_summary.csv"
)

review_analysis.to_csv(
    "review_analysis.csv",
    index=False
)

dish_price_comparison.to_csv(
    "dish_price_comparison.csv",
    index=False
)
low_rating_analysis.to_csv("low_rating_analysis.csv", index=False)

print("\nFiles created successfully:")
print("1. restaurant_benchmark.csv")
print("2. problem_analysis.csv")
print("3. rating_summary.csv")
print("4. review_analysis.csv")
print("5. dish_price_comparison.csv")

print("\n========== ANALYSIS COMPLETE ==========")

