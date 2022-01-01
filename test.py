# import socket
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# HOST="127.0.0.1"
# client.connect((HOST, 6767)) #lắng nghe ở cổng 6767
# print(client)
# print("Client address: ", client.getsockname())
# print(type(client.getsockname()))
# client.close()
stri = "31/12/2021"


def reformatDate(date):
    year = date[6:10]
    month = date[3:5]
    day = date[0:2]
    new = year+month+day
    return new


print(type(reformatDate(stri)))
