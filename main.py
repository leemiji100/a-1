# 기본 프롬프트 데이터 (프로그램 시작할 때 미리 들어있는 것들)
prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "당신은 10년 경력의 전문 블로거입니다. 주어진 주제에 대해 SEO에 최적화된 블로그 글을 작성해주세요.",
        "category": "텍스트 생성",
        "favorite": False
    },
    {
        "title": "제품 썸네일 생성",
        "content": "다음 제품의 매력적인 썸네일 이미지를 생성해주세요. 밝은 배경과 선명한 색감을 사용해주세요.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "IT 컨설턴트 페르소나",
        "content": "당신은 10년 경력의 IT 컨설턴트입니다. 기업의 디지털 전환 전략에 대해 전문적이고 실용적인 조언을 제공해주세요.",
        "category": "페르소나",
        "favorite": False
    }
]

print(prompts)
