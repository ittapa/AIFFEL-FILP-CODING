from flask import Flask, render_template, request
import os
from PIL import Image

app = Flask(__name__)

'''
이미지 처리 함수
'''
def image_resize(image, width, height):
        return image.resize((int(width), int(height)))

def image_rotate(image):
    return image.transpose(Image.ROTATE_180)



@app.route("/index")
def index():
    return render_template("p1.html")

@app.route("/imgPre", methods=['POST'] )
def imgPreprocssing():
    if request.method == "POST":
        file = request.files["imgFile"]
        if not file: return render_template('p1.html', label="No Files")

        img = Image.open(file)

        is_rotate = request.form.get("rotate")
        is_resize = request.form.get("resize")

        if is_resize == 'on':
            img = image_resize(img, 1920, 1080)

        if is_rotate == 'on':
            img = image_rotate(img)

        img.save('r_img.png')

        src_dir = os.path.dirname(os.path.abspath(__file__))
        print(src_dir)
        image_path = os.path.join(src_dir, 'result_image.png')

        # 결과 리턴
        return render_template('p1.html', label=image_path)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 3000))