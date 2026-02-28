# 💀 HADES
### Hard Disk Explorer & Storage

> *"토요일 오후. 배우 한 명. 노트북 한 대. 달리 할 일이 없었다."*

---

## 이게 뭔가요?

HADES는 외장 하드 드라이브에 무엇이 있는지 정확히 아는 디스크 인덱싱 시스템입니다 — 아마 당신보다 더 잘 알 겁니다.

스캔하고, 버전을 추적하고, 변경 사항을 감지하고, 모든 걸 예쁜 Excel 파일로 뱉어냅니다. 왜 안 되겠어요?

---

## 무엇을 할 수 있나요?

- 🔍 **자동 디스크 감지** – 연결하면 HADES가 알아서 인식
- 📁 **파일 인덱스** – 모든 파일, 모든 디스크, 한 곳에
- 🔄 **변경 사항 추적** – 무엇이 있었는지, 지금 무엇이 있는지, 무엇이 사라졌는지 앎
- 📊 **Excel 내보내기** – 대시보드 + 디스크별 개별 시트
- ⚡ **스마트 캐시** – 변경 사항 없으면 재생성 없음 (29만6천 개 파일 다시 읽기는 스포츠가 아님)
- 💾 **SQLite 데이터베이스** – 지속적, 견고, 절대 안 잊음

---

## 설치

```bash
git clone https://github.com/ferkomatolcsi-coder/HADES.git
cd HADES
pip install -r requirements.txt
```

---

## 사용법

**스캔** – 연결된 디스크 인덱싱:
```bash
python3 hades_scan.py
```

**내보내기** – Excel 파일 생성:
```bash
python3 hades_export.py
```

결과: HADES 폴더에 `HADES_export_날짜_시간.xlsx`

---

## 요구 사항

- Python 3.8+
- macOS 또는 Linux
- 한동안 들여다보지 않은 외장 디스크 최소 하나

---

## 호환성

| 플랫폼  | 상태 |
|---------|------|
| macOS   | ✅ 테스트됨 |
| Linux   | ✅ 지원됨 |
| Windows | 🤷 언젠가는 |

---

## 로드맵

- [ ] 웹 UI (Flask 기반 대시보드)
- [ ] GitHub Actions 자동 스캔
- [ ] Windows 지원
- [ ] 토요일엔 잠 좀 자기

---

## 제작자

**ferkomatolcsi-coder** – 배우, 개발자, 토요일 발명가.  
프로젝트를 만들 계획이 없었다. 그냥 그렇게 됐다.

---

*Built with Passion* 🔥  
*(그리고 커피 한 잔... 아니 여러 잔)*
