import cv2

for i in range(10):
    cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)

    if cap.isOpened():
        ret, frame = cap.read()

        if ret:
            print(
                f"摄像头编号 {i}: "
                f"分辨率 {frame.shape[1]}x{frame.shape[0]}"
            )
        else:
            print(f"摄像头编号 {i}: 打开成功但无法读取画面")

    cap.release()