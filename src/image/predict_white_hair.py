from src.common.utils import display_image


class PredictResultManager(object):
    def __init__(self, faces, image, debug):
        self.faces = faces
        self.image = image
        self.debug = debug
        self.results = []

    def send_face_to_predictor(self):
        for (x, y, w, h) in self.faces:
            # 顔部分の画像の切り取り
            im_trim, width, height = self.crip_face_image(x, y, w, h,
                                                          self.image)
            predictor = WhiteHairPredictor(im_trim, width, height,
                                           debug=self.debug)
            self.results.append(predictor.predict_white_or_not())

    def get_final_result(self):
        for flag in self.results:
            if flag:
                return True
        return False

    @staticmethod
    def crip_face_image(x, y, w, h, im):
        # 画像の切り抜き
        im_trim = im[y:y+h, x:x+w]
        width = len(im_trim)
        height = len(im_trim[0])
        return im_trim, width, height


class HairPredictor(object):
    def __init__(self, im_trim, width, height, debug):
        self.im_trim = im_trim
        self.debug = debug

        # 頻度を数えるための辞書を準備
        self.color_freq = self.initialize_dict(im_trim)

        # 端っこを切り取るための変数を定義
        self.waru6height = int(height / 6)
        self.waru10width = int(width / 10)

    @staticmethod
    def initialize_dict(im_trim):
        color_freq = {}
        for colors in im_trim:
            for rgb in colors:
                cat = ':'.join([str(code) for code in rgb])
                color_freq[cat] = 0
        return color_freq

    def crip_pixel_count(self, image, start_width, end_width, 
                         start_height, end_height):
        if self.debug:
            display_image(image[start_height:end_height, 
                                start_width:end_width])
        trim_image = image[start_height:end_height, 
                           start_width:end_width].tolist()
        for pixel in trim_image:
            for rgb in pixel:
                cat = ':'.join([str(code) for code in rgb])
                self.color_freq[cat] += 1
        return self.color_freq


class WhiteHairPredictor(HairPredictor):
    def __init__(self, im_trim, width, height, debug):
        super().__init__(im_trim, width, height, debug)

    def predict_white_or_not(self):
        # 色の頻度を数える(top)
        self.crip_pixel_count(self.im_trim, None, None, 
                              None, self.waru6height)

        # 色の頻度を数える(left)
        self.crip_pixel_count(self.im_trim, None, self.waru10width, 
                              self.waru6height, None)

        # 色の頻度を数える(right)
        self.crip_pixel_count(self.im_trim, -self.waru10width, None, 
                              self.waru6height, None)

        # 頻出色の取得
        color_freq_list = [(v, k) for k, v in self.color_freq.items()]
        mode_color_str = max(color_freq_list)[1].split(":")
        mode_color_int = [int(code) for code in mode_color_str]

        # 白かどうかの評価
        predict = self.iswhitehair(mode_color_int)

        return predict

    @staticmethod
    def iswhitehair(mode_color):
        thres = 0
        for code in mode_color:
            if code >= 240:
                thres += 1
        if min(mode_color) >= 190 and sum(mode_color) >= 590:
            thres = 3
        if thres == 3:
            predict = True
        else:
            predict = False
        return predict
