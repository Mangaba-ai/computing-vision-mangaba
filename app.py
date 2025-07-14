# --------------------------------------------------------
# Based on yolov10
# https://github.com/THU-MIG/yolov10/app.py
# --------------------------------------------------------'

import cv2
import tempfile
import json
import numpy as np
import argparse
from ultralytics import YOLO

def yolov12_inference(source_path, model_id, image_size, conf_threshold, output_video_path=None, output_json_path=None):
    model = YOLO(model_id)
    extracted_features = []

    if source_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        # Process image
        results = model.predict(source=source_path, imgsz=image_size, conf=conf_threshold)
        annotated_image = results[0].plot()
        
        frame_features = []
        if results[0].boxes:
            for box in results[0].boxes:
                xyxy = box.xyxy[0].tolist()
                conf = box.conf[0].item()
                cls = int(box.cls[0].item())
                
                # Derived features
                x1, y1, x2, y2 = xyxy
                width = x2 - x1
                height = y2 - y1
                centroid_x = (x1 + x2) / 2
                centroid_y = (y1 + y2) / 2
                area = width * height
                aspect_ratio = width / height if height != 0 else 0
                
                frame_features.append({
                    "box_xyxy": xyxy,
                    "confidence": conf,
                    "class_id": cls,
                    "centroid_x": centroid_x,
                    "centroid_y": centroid_y,
                    "width": width,
                    "height": height,
                    "area": area,
                    "aspect_ratio": aspect_ratio
                })
        extracted_features.append({"frame_number": 0, "detections": frame_features})
        
        if output_video_path: # This will save the annotated image as a video with 1 frame
            cv2.imwrite(output_video_path, annotated_image[:, :, ::-1])
        
        if output_json_path:
            with open(output_json_path, 'w') as f:
                json.dump(extracted_features, f, indent=2)
        
        return extracted_features

    elif source_path.lower().endswith(('.mp4', '.avi', '.mov', '.webm')):
        # Process video
        cap = cv2.VideoCapture(source_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out = None
        if output_video_path:
            fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Use mp4v for broader compatibility
            out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

        frame_number = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            results = model.predict(source=frame, imgsz=image_size, conf=conf_threshold)
            annotated_frame = results[0].plot()
            if out:
                out.write(annotated_frame)

            frame_features = []
            if results[0].boxes:
                for box in results[0].boxes:
                    xyxy = box.xyxy[0].tolist()
                    conf = box.conf[0].item()
                    cls = int(box.cls[0].item())
                    
                    # Derived features
                    x1, y1, x2, y2 = xyxy
                    width = x2 - x1
                    height = y2 - y1
                    centroid_x = (x1 + x2) / 2
                    centroid_y = (y1 + y2) / 2
                    area = width * height
                    aspect_ratio = width / height if height != 0 else 0

                    frame_features.append({
                        "box_xyxy": xyxy,
                        "confidence": conf,
                        "class_id": cls,
                        "centroid_x": centroid_x,
                        "centroid_y": centroid_y,
                        "width": width,
                        "height": height,
                        "area": area,
                        "aspect_ratio": aspect_ratio
                    })
            extracted_features.append({"frame_number": frame_number, "detections": frame_features})
            frame_number += 1

        cap.release()
        if out:
            out.release()

        if output_json_path:
            with open(output_json_path, 'w') as f:
                json.dump(extracted_features, f, indent=2)

        return extracted_features

    else:
        raise ValueError("Unsupported source type. Please provide an image or video file.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="YOLOv12 CLI para extração de features e detecção de objetos.")
    parser.add_argument('--source', type=str, required=True, help='Caminho para a imagem ou vídeo de entrada.')
    parser.add_argument('--model', type=str, default='yolov12m.pt', help='ID do modelo YOLOv12 (e.g., yolov12n.pt, yolov12s.pt).')
    parser.add_argument('--imgsz', type=int, default=640, help='Tamanho da imagem para inferência.')
    parser.add_argument('--conf', type=float, default=0.25, help='Limiar de confiança para detecção.')
    parser.add_argument('--output_video', type=str, help='Caminho para salvar o vídeo/imagem anotado.')
    parser.add_argument('--output_json', type=str, help='Caminho para salvar as features extraídas em JSON.')

    args = parser.parse_args()

    print(f"Processando {args.source} com o modelo {args.model}...")
    features = yolov12_inference(
        source_path=args.source,
        model_id=args.model,
        image_size=args.imgsz,
        conf_threshold=args.conf,
        output_video_path=args.output_video,
        output_json_path=args.output_json
    )

    if features:
        print("\nFeatures Extraídas:")
        print(json.dumps(features, indent=2))
    else:
        print("Nenhuma feature extraída.")

    print("\nProcessamento concluído.")

