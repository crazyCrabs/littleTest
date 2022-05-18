import ddddocr

ocr = ddddocr.DdddOcr()


def verify():
    results = []
    for i in range(1, 6):
        with open("{}.png".format(i), 'rb') as f:
            img_bytes = f.read()
        res = ocr.classification(img_bytes)
        results.append(res)
    return results


a = [verify() for _ in range(3)]

print(">>> 认证结果", a)
