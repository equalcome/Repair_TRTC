import pandas as pd
import os

# 讀取用戶上傳的 Excel 文件
file_path = 'mrt_test.xlsx'

if os.path.exists(file_path):
    print("File exists")
    df = pd.read_excel(file_path)

    # 轉換為 JSON 格式
    json_data = df.to_json(orient='records', force_ascii=False)

    # 保存 JSON 文件
    json_file_path = 'C:/Users/User/Desktop/MRT DATA/Repair_TRTC/options.json'
    with open(json_file_path, 'w', encoding='utf-8') as file:
        file.write(json_data)

    print(f"JSON File saved: {json_file_path}")

else:
    print("File does not exist")
