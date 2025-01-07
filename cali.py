import depthai as dai
import cv2
import os

# Create pipeline
pipeline = dai.Pipeline()

# Left and right cameras
left = pipeline.create(dai.node.MonoCamera)
right = pipeline.create(dai.node.MonoCamera)

# Configure cameras
left.setBoardSocket(dai.CameraBoardSocket.LEFT)
right.setBoardSocket(dai.CameraBoardSocket.RIGHT)
left.setResolution(dai.MonoCameraProperties.SensorResolution.THE_720_P)
right.setResolution(dai.MonoCameraProperties.SensorResolution.THE_720_P)

# XLink outputs
xoutLeft = pipeline.create(dai.node.XLinkOut)
xoutRight = pipeline.create(dai.node.XLinkOut)
xoutLeft.setStreamName("left")
xoutRight.setStreamName("right")

# Link cameras to outputs
left.out.link(xoutLeft.input)
right.out.link(xoutRight.input)

# Start pipeline
with dai.Device(pipeline) as device:
    qLeft = device.getOutputQueue(name="left", maxSize=4, blocking=False)
    qRight = device.getOutputQueue(name="right", maxSize=4, blocking=False)

    # Create output directories
    os.makedirs('images/left', exist_ok=True)
    os.makedirs('images/right', exist_ok=True)

    print("Press 'c' to capture, 'q' to quit.")
    counter = 0
    while True:
        inLeft = qLeft.get()
        inRight = qRight.get()

        # Get frames
        frameLeft = inLeft.getCvFrame()
        frameRight = inRight.getCvFrame()

        # Display frames
        cv2.imshow("Left", frameLeft)
        cv2.imshow("Right", frameRight)

        key = cv2.waitKey(1)
        if key == ord('c'):
            cv2.imwrite(f'images/left/left_{counter}.png', frameLeft)
            cv2.imwrite(f'images/right/right_{counter}.png', frameRight)
            print(f"Captured image pair {counter}")
            counter += 1
        elif key == ord('q'):
            break

    cv2.destroyAllWindows()
