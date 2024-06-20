from pymilvus import MilvusClient, DataType

client = MilvusClient(
    uri="http://localhost:19530"
)

# client.create_collection(
#     collection_name="quick_setup",
#     dimension=5
# )


# IS IT LOADED?
res = client.get_load_state(
    collection_name="baysan_demo"
)
print(res)

# LIST ALL COLLECTIONS
res = client.list_collections()
print(res)

# DESCRIBE COLLECTION
res = client.describe_collection(
    collection_name="baysan_demo"
)
print(res)


