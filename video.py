import os, cv2, torch, supervision as sv
from PytorchWildlife.models import detection as pw_detection

SOURCE_VIDEO_PATH = "/Users/sarahabdelazim/Desktop/cow_catalyst/April 1/MVI_0115.MP4"
TARGET_VIDEO_PATH = "/Users/sarahabdelazim/Desktop/cow_catalyst/April 1/MVI_0115_processed.mp4"

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
if DEVICE == "cuda":
    torch.cuda.set_device(0)

DET_CONF_THRESH = 0.40
det_model = pw_detection.MegaDetectorV6(device=DEVICE, pretrained=True, version="MDV6-yolov10-e")
det_model.eval()

cap = cv2.VideoCapture(SOURCE_VIDEO_PATH)
if not cap.isOpened():
    raise RuntimeError(f"Cannot open video: {SOURCE_VIDEO_PATH}")

fps   = cap.get(cv2.CAP_PROP_FPS) or 25.0
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc= cv2.VideoWriter_fourcc(*"avc1")
out   = cv2.VideoWriter(TARGET_VIDEO_PATH, fourcc, fps, (width, height))

box_annotator   = sv.BoxAnnotator()                      # draws rectangles only
label_annotator = sv.LabelAnnotator(text_scale=0.6, text_thickness=1)  # draws text

frame_idx = 0
FRAME_SKIP = 0

while True:
    ok, frame_bgr = cap.read()
    if not ok:
        break

    if FRAME_SKIP and (frame_idx % (FRAME_SKIP + 1) != 0):
        out.write(frame_bgr); frame_idx += 1; continue

    frame_rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
    res = det_model.single_image_detection(frame_rgb, det_conf_thres=DET_CONF_THRESH)

    dets = res["detections"]      # sv.Detections
    labels_txt = res["labels"]    # list[str], same order as dets

    annotated = box_annotator.annotate(scene=frame_bgr.copy(), detections=dets)
    annotated = label_annotator.annotate(scene=annotated, detections=dets, labels=labels_txt)

    out.write(annotated)
    frame_idx += 1

cap.release()
out.release()
print(f"Saved annotated video → {TARGET_VIDEO_PATH}")