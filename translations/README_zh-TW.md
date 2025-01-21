# TTDOTEXE (TikTok.exe)

TTDOTEXE (TikTok.exe) 是一個創新的項目，結合了 TikTok 的迷因魅力（如經典的 OIA 旋轉貓）與尖端技術。此專案利用 Python 和 Microsoft Azure Quantum Framework 開發，提供了一種既有趣又技術性的區塊鏈和 ASCII 藝術解決方案。

## 功能

- **ASCII 動畫藝術**：將 GIF 轉換為令人驚嘆的 ASCII 動畫，可在終端中展示。
- **量子計算整合**：利用 Microsoft Azure Quantum Framework 提升加密和計算效率。
- **Solana 區塊鏈**：基於 Solana 的高速、低成本架構，確保區塊鏈互動流暢。
- **基於 Python 的 SPL Token**：首個完全用 Python 編寫的 Solana Token。
- **以社群為中心**：完全開源，旨在激發協作和創造力。

## 先決條件

在執行本項目之前，請確保已安裝以下內容：

- **Docker**
- **Python 3.8+**
- **pip**

## 安裝

1. 克隆此存儲庫：

```bash
git clone https://github.com/ttdotexe/tiktokexe.git
cd tiktokexe
```

2. 安裝依賴項：

```bash
pip install -r requirements.txt
```

3. （可選）設置虛擬環境：

```bash
python -m venv venv
source venv/bin/activate  # 在 Windows 上：venv\Scripts\activate
```

## 本地執行專案

1. 執行 ASCII 動畫：

```bash
python TIKTOKEXE.py
```

2. 使用 fetch_wallet 腳本獲取 Token 持有人：

```bash
python fetch_wallet.py
```

## 使用 Docker 執行

1. 構建 Docker 映像：

```bash
docker build -t tiktokexe .
```

2. 執行容器：

```bash
docker run --rm -it tiktokexe
```

## 專案結構

```plaintext
.
├── assets                # GIF 和其他資源
├── images_rdm            # 參考圖像
├── src                   # 原始碼
│   ├── ascii_generator.py
│   ├── ascii_player.py
│   ├── utils.py
├── translations          # 翻譯文件
├── TIKTOKEXE.py          # 主入口點
├── fetch_wallet.py       # 獲取 Token 持有人腳本
├── requirements.txt      # Python 依賴項
├── Dockerfile            # Docker 配置
└── README.md             # 項目文檔
```

## 為什麼選擇 Microsoft Azure Quantum？

Azure Quantum 提供了最先進的量子算法，提升加密功能、優化計算過程並實現安全的密鑰交換。這一整合確保 TTDOTEXE 高效、可擴展且安全。

## 授權

此專案基於 MIT 授權。查看 [LICENSE](LICENSE) 文件以了解更多細節。

## 貢獻

歡迎貢獻！隨時開啟問題或提交拉取請求。

## 聯繫

在 [GitHub](https://github.com/ttdotexe/tiktokexe) 上關注 TTDOTEXE 的進展。分享您的反饋，讓我們共同改進這個專案！
