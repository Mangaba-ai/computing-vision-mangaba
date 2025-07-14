# Script PowerShell para executar análise de vídeo com YOLOv12
# Substitua os caminhos conforme necessário

python app.py `
    --source "C:\Users\Lenovo\computing-vision-mangaba\6387-191695740_large.mp4" `
    --model "yolov12m.pt" `
    --imgsz 640 `
    --conf 0.25 `
    --output_video "C:\Users\Lenovo\computing-vision-mangaba\output\video_anotado.mp4" `
    --output_json "C:\Users\Lenovo\computing-vision-mangaba\output\features_video.json"

# Pausa para ver o resultado
Write-Host "Análise concluída! Pressione qualquer tecla para continuar..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")