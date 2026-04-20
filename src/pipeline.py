from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder.appName("DataPipeline").getOrCreate()

    input_path = "data/sample.csv"
    output_path = "output/filtered_data"

    df = spark.read.csv(input_path, header=True, inferSchema=True)

    print("=== Original Data ===")
    df.show()

    filtered_df = df.filter(df.age > 30)

    print("=== Filtered Data (age > 30) ===")
    filtered_df.show()

    filtered_df.write.mode("overwrite").csv(output_path)

    print("Pipeline executed successfully 🚀")

if __name__ == "__main__":
    main()
