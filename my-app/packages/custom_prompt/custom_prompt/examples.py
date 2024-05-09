from langchain_core.pydantic_v1 import BaseModel, Field


class PlaylistAttributes(BaseModel):
    genre: list = Field(description="genre of the playlist")
    tempo: str = Field(description="tempo of the playlist")
    instruments: list = Field(description="instruments used in the playlist")
    mood: list = Field(description="mood of the playlist")
    release_decade: list = Field(description="release year of the playlist")
    etc_keywords: list = Field(description="other keywords of the playlist")


examples = [
    {"content": "뜨개질에 몰입하기 좋은 리메이크 발라드",
     "genre": ['발라드'],
     "tempo": "느림",
     "instruments": [],
     "mood": ['감성'],
     "release_decade": [],
     "etc_keywords": ['뜨개질', '집중', '리메이크']},
    {"content": "All That 국내 락&메탈",
     "genre": ['락', '메탈'],
     "tempo": "빠름",
     "instruments": ['기타', '드럼'],
     "mood": ['에너지 넘치는'],
     "release_decade": [],
     "etc_keywords": ['국내', 'All That']},
    {"content": "세대초월 회식에서 부르면 인싸되는 노래",
     "genre": ['발라드', '댄스곡', '트로트'],
     "tempo": "중",
     "instruments": [],
     "mood": ['감성', '에너지 넘치는'],
     "release_decade": [],
     "etc_keywords": ['세대초월', '회식', '인싸']},
    {"content": "밤하늘의 별과 낭만적인 피아노 연주곡",
     "genre": ['연주곡'],
     "tempo": "느림",
     "instruments": ['piano'],
     "mood": ['감성'],
     "release_decade": [],
     "etc_keywords": ['밤하늘', '별', '낭만']},
    {"content": "흐릿한 하루? 청량 일렉트로 팝으로 극복",
     "genre": ['팝', '일렉트로', 'EDM'],
     "tempo": "빠름",
     "instruments": [],
     "mood": ['감성'],
     "release_decade": [],
     "etc_keywords": ['흐릿한', '청량']},
    {"content": "영화음악의 거장, 히사이시조",
     "genre": ['OST', '영화음악'],
     "tempo": "느림",
     "instruments": [],
     "mood": ['감성적'],
     "release_decade": [],
     "etc_keywords": ['영화음악', '히사이시조']},
    {"content": "비트 속에 깊숙히 스며든 멈블 랩",
     "genre": ['랩', '힙합'],
     "tempo": "중간",
     "instruments": [],
     "mood": ['에너지 넘치는'],
     "release_decade": [],
     "etc_keywords": ['멈블', '비트']},
    {"content": "낭만적인 90년대 시네마틱 R&B",
     "genre": ['발라드'],
     "tempo": "중간",
     "instruments": [],
     "mood": ['감성적'],
     "release_decade": ['90년대'],
     "etc_keywords": ['시네마틱', '낭만']},
    {"content": "2000년대 해외 일렉트로닉",
     "genre": ['일렉트로닉'],
     "tempo": "빠름",
     "instruments": [],
     "mood": ['에너지 넘치는'],
     "release_decade": ['2000년대'],
     "etc_keywords": ['해외']},
    {"content": "2010 부터 걸그룹 전성기였다 👠",
     "genre": ['아이돌', '댄스곡'],
     "tempo": "중간",
     "instruments": [],
     "mood": ['에너지 넘치는'],
     "release_decade": ['2010년대'],
     "etc_keywords": ['걸그룹', '전성기']},
]
