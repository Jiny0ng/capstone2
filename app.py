import os
import openai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


openai.api_key = os.getenv("YOUR_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def generate_response():
    product_addresses = request.form.getlist('product_addresses')
    user_requirements = request.form.get('user_requirements')
    if len(product_addresses) >= 2:
        productA = product_addresses[0]
        productB = product_addresses[1]
    else:
        return jsonify({"error": "적어도 두 개의 제품 주소가 필요합니다."})
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": ("너는 여행 전문가로써 숙소를 결정하는데 도움을 줘야해"
                                               "모든 대답은 한국어로 해야해"
                                               "두개의 상품중 더 사용자에게 맞는것으로 보이는 상품을 고를꺼야")},
                {"role": "user", "content": (f"너는 여행 숙박업소 전문가로써 숙박업소 비교를 진행할꺼야"
                                            f"상품 2개가 있는데, {productA}의 상품과 {productB}의 상품을 비교할꺼야"
                                            f"productA 의 리뷰에서 장점 (ex : 재방문 의사, 저렴함, 가성비, 청결, 위치 등)"
                                            f"productB 의 리뷰에서 장점 (ex : 재방문 의사, 저렴함, 가성비, 청결, 위치 등)"
                                            "'가성비 좋아요' 와 같은말은 가격이 저렴하다 즉 경제성이 있다고 볼 수 있고"
                                            "'위치가 좋아요' 는 이동시간 혹은 여행 컨텐츠의 측면에서 메리트가 있어"
                                            "'~~가 안좋아요'를 보면 부정적인 부분을 확인할 수 있어"
                                            "이러한 점들을 비교하고 상대적으로 어떤걸 추천하는지"
                                            "추천하는 이유를 위의 좋은점을 통해 설명해야해"
                                            "A와 B의 장점을 비교하고 requirement를 토대로 더 나은 선택지를 고르고 아래의 예시처럼 출력해줘"
                                            f"사용자 요구 사항: {user_requirements}"
                                            "추천 숙소 : [추천숙소]"
                                            "요약 : [추천숙소]를 고른 이유"
                                            "주요 포인트 : 선택할때 가장 메리트 있다고 생각한 3가지 (ex : 가격, 위치, 시설)")}
            ],
            max_tokens=250,
            temperature=0.7
        )
        
        print(result)
        result = response.choices[0].text
    except Exception as e:
        result = str(e)
    
    return jsonify({
        'product_addresses': product_addresses,
        'user_requirements': user_requirements,
        'result': result
        })
        
if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)
