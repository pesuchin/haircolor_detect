import cv2


def display_image(im_trim):
    cv2.imshow("Show Image", im_trim)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def crip_pixel_count(image, color_freq,
                     start_width, end_width, start_height, end_height,
                     debug=False):
    if debug:
        display_image(image[start_height:end_height, start_width:end_width])
    trim_image = image[start_height:end_height, start_width:end_width].tolist()
    for colors in trim_image:
        for rgb in colors:
            cat = ':'.join([str(code) for code in rgb])
            color_freq[cat] += 1
    return color_freq


def crip_image(x, y, w, h, filename):
    # 画像取得
    im = cv2.imread(filename)

    # 画像の切り抜き
    im_trim = im[y:y+h, x:x+w]
    width = len(im_trim)
    height = len(im_trim[0])
    return im_trim, width, height
