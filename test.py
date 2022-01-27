import pyupbit

access = "Lw9Wux57QIhVBT0YXGgOary3uzbyYWjOQNKCtcbk"          # 본인 값으로 변경
secret = "krco88XNPYfg0POGwhUujP1adiF50Exg9VbMmDW3"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회