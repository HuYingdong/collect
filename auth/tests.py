import json
from django.test import Client

client = Client()


# select_data = {
#     "table": "service_policy",
#     "values": ["service_id", "customer_id", "prior"],
#     "cond": {"id": 3, "prior": 3}
# }
#
#
# response = client.get('/api/tembin/omais/auth/', data=select_data)
# result = json.loads(response.content)


insert_data = {
    "table": "service_policy",
    "values": {"service_id": 2, "customer_id": "1", "prior": 1}
}
insert_datas = {
    "table": "service_policy",
    "values": [
        {"service_id": 2, "customer_id": "1", "prior": 2},
        {"service_id": 2, "customer_id": "2", "prior": 3},
        {"service_id": 2, "customer_id": "3", "prior": 4},
        {"service_id": 2, "customer_id": "4", "prior": 5}
        ]
}

response = client.post('/api/tembin/omais/auth/', data=json.dumps(insert_data), content_type='application/json')
print(response.status_code)
print(response.content)

response = client.post('/api/tembin/omais/auth/', data=json.dumps(insert_datas), content_type='application/json')
print(response.status_code)
print(response.content)


update_data = {
    "table": "service_policy",
    "values": {"service_id": 3, "customer_id": "100", "prior": 100},
    "cond": {"service_id": 2}
}
response = client.put('/api/tembin/omais/auth/', data=json.dumps(update_data), content_type='application/json')
print(response.status_code)
print(response.content)


del_data = {
    "table": "service_policy",
    "cond": {"service_id": 2}
}
response = client.delete('/api/tembin/omais/auth/', data=json.dumps(del_data), content_type='application/json')
print(response.status_code)
print(response.content)
