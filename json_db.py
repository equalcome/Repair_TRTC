import pandas as pd

# 讀取 Excel 文件
station_file_path = r'C:\Users\User\Desktop\MRT DATA\Repair_TRTC\repairDB\station.xlsx'
personnel_file_path = r'C:\Users\User\Desktop\MRT DATA\Repair_TRTC\repairDB\Personnel.xlsx'  # 這裡使用你上傳的文件路徑

# 讀取數據
station_df = pd.read_excel(station_file_path)
personnel_df = pd.read_excel(personnel_file_path)

# 將數據框架轉換為 JSON 文件
station_json_data = station_df.to_json(orient='records', force_ascii=False)
personnel_json_data = personnel_df.to_json(orient='records', force_ascii=False)

# 保存 JSON 文件
with open('stationDB.json', 'w', encoding='utf-8') as f:
    f.write(station_json_data)

with open('personnelDB.json', 'w', encoding='utf-8') as f:
    f.write(personnel_json_data)
