from image_processing import crip_pixel_count


def iswhitehair(mode_color):
    thres = 0
    for code in mode_color:
        if code >= 240:
            thres += 1
    if min(mode_color) >= 190 and sum(mode_color) >= 590:
        thres = 3
    if thres == 3:
        predict = True
        print("This is a white hair!")
    else:
        predict = False
        print("This is not a white hair...")
    return predict


def predict_white_color(im_trim, width, height):
    # 辞書を初期化
    color_freq = {}

    # 端っこを切り取るための変数を定義
    waru6height = int(height / 6)
    waru10width = int(width / 10)

    # 頻度を数えるための辞書を準備
    for colors in im_trim:
        for rgb in colors:
            cat = ':'.join([str(code) for code in rgb])
            color_freq[cat] = 0
    
    # 頻度を数える(top)
    color_freq = crip_pixel_count(im_trim, color_freq,
                                  None, None, None, waru6height)

    # 頻度を数える(left)
    color_freq = crip_pixel_count(im_trim, color_freq, 
                                  None, waru10width, waru6height, None)

    # 頻度を数える(right)
    color_freq = crip_pixel_count(im_trim, color_freq, 
                                  -waru10width, None, waru6height, None)

    # 頻出色の取得
    mode_color = max([(v, k) for k, v in color_freq.items()])[1].split(":")

    # 最頻値のコードを文字列型から整数型へ変換
    mode_color = [int(code) for code in mode_color]

    # 白かどうかの評価
    predict = iswhitehair(mode_color)

    return predict
