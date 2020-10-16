#
# pip list
# pip3 install opencv-python
# pip3 install opencv-contrib-python
# pip3 install matplotlib
# pip3 install scipy
# pip3 install pillow
# pip3 install django-imagekit

import logging

from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
import cv2

from django_lesson.settings import MEDIA_ROOT

# logger = logging.getLogger(__name__)
logger = logging.getLogger("log_file")


def recognize_face(input_pic, output_pic):
    work_path = MEDIA_ROOT + '/images/'
    in_pic = work_path + input_pic
    out_pic = work_path + output_pic
    logger.warning(in_pic)
    logger.warning(out_pic)
    return


# @login_required
class PlotIndexView(TemplateView):
    template_name = 'plot/index.html'

    imagePath = MEDIA_ROOT + '/images/'
    img1 = cv2.imread(MEDIA_ROOT + '/akb48_7.png')

    recognize_face('in_48.png', 'out_48.pic')
    logger.warning('--- recognized --- ')

    cv2.imwrite(imagePath + 'output.jpg', img1)  # そのまま、ファイル出力
    gry_img = cv2.imread(MEDIA_ROOT + '/akb48_7.png', 0)
    cv2.imwrite(imagePath + 'gray.jpg', gry_img)  # グレイスケール・ファイル出力
    canny_img = cv2.Canny(gry_img, 50, 110)  # 第2,3引数は閾値
    cv2.imwrite(imagePath + 'bw.jpg', canny_img)  # 白黒・エッジ

    # 分類器の読込
    # https://github.com/opencv/opencv/tree/master/data/haarcascades
    face_path = MEDIA_ROOT + '/opencv_data/haarcascades/'
    cascade_path = face_path + 'haarcascade_frontalface_default.xml'
    print(cascade_path)

    # カスケード検出器の特徴量を取得する
    cascade = cv2.CascadeClassifier(cascade_path)
    # 顔検出の実行
    facerect = cascade.detectMultiScale(gry_img, scaleFactor=1.1, minNeighbors=6, minSize=(30, 30))
    # 矩形線の色
    rectangle_color = (0, 255, 0)  # 緑色
    # 顔を検出した場合
    if len(facerect) > 0:
        for rect in facerect:
            cv2.rectangle(img1, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), rectangle_color, thickness=2)
    # scaleFactor ：
    # 画像スケールにおける縮小量。detectMultiScaleでは画像のスケールを何度も変化させて探索するため、その際の縮小量を設定する。大きいほど誤検知が多く、小さいほど未検出となってしまう率が高くなる
    # minNeighbors：
    # 信頼性のパラメータ。検出器が検出する箇所が重複するので、より重複が多い部分が信頼性が高いこととなり、その閾値を設定します。値が大きくなるにつれて信頼性が上がるが、顔を見逃してしまう率も高くなる。
    # minSize ：
    # 物体が取り得る最小サイズ。これよりも小さい物体は無視される。
    # img = cv2.cvtColor(img1, cv2.COLOR_RGB2BGR)  # RGBからBGRに変換
    cv2.imwrite(imagePath + 'face.jpg', img1)

    # cv2.imshow('Window Name', img1)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


class PlotShowView(TemplateView):
    pass
