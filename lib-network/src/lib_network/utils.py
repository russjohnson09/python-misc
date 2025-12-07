import json

def receive_data_json(conn, buffer_size = 1024):
    data = b''
    while True:
        # data = b''
        # change this to base64 encoded and wait on a newline
        data_chunk = conn.recv(buffer_size)
        if len(data_chunk) == 0:
            continue

        data_chunk_str = data_chunk.decode()
        print("receive_data_json", data_chunk)
        data += data_chunk
        print(data)

        if '\n' in data_chunk_str: # has null terminating byte
            print("receive_data_json final: ", data)
            if len(data) == 0:
                return {}
            return json.loads(data)
