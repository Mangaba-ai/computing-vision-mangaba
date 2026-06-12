<div align="center">
  <img src="assets/mangaba-logo.svg" alt="Mangaba AI" width="140"/>

  [![Mangaba AI](https://img.shields.io/badge/Mangaba-AI-F97518?style=for-the-badge)](https://www.mangaba.ia.br)
  [![Site](https://img.shields.io/badge/mangaba.ia.br-1E0D01?style=for-the-badge)](https://www.mangaba.ia.br)
</div>

# Visão Computacional Mangaba Enjoy

Este repositório contém uma aplicação de linha de comando (CLI) para detecção e extração de features de objetos usando modelos YOLOv12. A aplicação é otimizada para execução via PowerShell, permitindo processamento eficiente de imagens e vídeos.

## 🚀 Instalação e Configuração

### Pré-requisitos

- **Python**: 3.11 ou superior
- **PyTorch**: 2.2.2 ou superior
- **CUDA**: 11.8 ou superior (para aceleração via GPU, opcional)
- **Sistema Operacional**: Windows, Linux, macOS

### Instalação Rápida

1.  **Clone o Repositório:**
    ```bash
    git clone https://github.com/sunsmarterjie/yolov12.git
    cd yolov12
    ```

2.  **Configuração do Ambiente Virtual:**

    É altamente recomendável usar um ambiente virtual para gerenciar as dependências do projeto.

    ```powershell
    # Criar ambiente virtual
    python -m venv venv

    # Ativar ambiente virtual (PowerShell)
    .\venv\Scripts\Activate.ps1

    # Instalar dependências
    pip install -r requirements.txt
    ```

### Verificação da Instalação

Para verificar se tudo foi instalado corretamente e se o CUDA está disponível:

```powershell
# Ative o ambiente virtual se ainda não estiver ativo
.\venv\Scripts\Activate.ps1

python -c "import torch; print(f'CUDA disponível: {torch.cuda.is_available()}'); print(f'Versão do PyTorch: {torch.__version__}')"
```

## 🔧 Uso da Aplicação CLI (`app.py`)

A aplicação `app.py` permite realizar inferência de detecção de objetos em imagens ou vídeos, extrair features e salvar os resultados.

### Argumentos da Linha de Comando

-   `--source`: **(Obrigatório)** Caminho para a imagem ou vídeo de entrada.
-   `--model`: ID do modelo YOLOv12 a ser usado (ex: `yolov12n.pt`, `yolov12s.pt`, `yolov12m.pt`, `yolov12l.pt`, `yolov12x.pt`). Padrão: `yolov12m.pt`.
-   `--imgsz`: Tamanho da imagem para inferência. Padrão: `640`.
-   `--conf`: Limiar de confiança para detecção. Padrão: `0.25`.
-   `--output_video`: Caminho para salvar o vídeo/imagem anotado.
-   `--output_json`: Caminho para salvar as features extraídas em formato JSON.

### Exemplos de Uso no PowerShell

Certifique-se de que seu ambiente virtual esteja ativado antes de executar os comandos.

```powershell
# Ativar ambiente virtual
.\venv\Scripts\Activate.ps1
```

#### 1. Processar uma Imagem e Salvar Resultados

```powershell
python app.py `
    --source "C:\caminho\para\sua\imagem.jpg" `
    --model "yolov12s.pt" `
    --imgsz 640 `
    --conf 0.3 `
    --output_video "C:\caminho\para\saida\imagem_anotada.jpg" `
    --output_json "C:\caminho\para\saida\features_imagem.json"
```

#### 2. Processar um Vídeo e Salvar Resultados

```powershell
python app.py `
    --source "C:\caminho\para\seu\video.mp4" `
    --model "yolov12m.pt" `
    --imgsz 640 `
    --conf 0.25 `
    --output_video "C:\caminho\para\saida\video_anotado.mp4" `
    --output_json "C:\caminho\para\saida\features_video.json"
```

#### 3. Apenas Extrair Features (sem salvar vídeo/imagem)

```powershell
python app.py `
    --source "C:\caminho\para\sua\imagem.png" `
    --model "yolov12n.pt" `
    --output_json "C:\caminho\para\saida\features_somente.json"
```

#### 4. Apenas Salvar Vídeo/Imagem Anotado (sem JSON de features)

```powershell
python app.py `
    --source "C:\caminho\para\seu\video.avi" `
    --model "yolov12l.pt" `
    --output_video "C:\caminho\para\saida\video_apenas_anotado.avi"
```

## 📊 Modelos YOLOv12 Suportados

A aplicação suporta os seguintes modelos YOLOv12 pré-treinados:

| Modelo      | Descrição                               |
| :---------- | :-------------------------------------- |
| `yolov12n.pt` | Nano (menor, mais rápido)               |
| `yolov12s.pt` | Small                                   |
| `yolov12m.pt` | Medium (padrão, bom equilíbrio)         |
| `yolov12l.pt` | Large                                   |
| `yolov12x.pt` | Extra Large (maior precisão, mais lento) |

Você pode baixar esses modelos do repositório oficial do YOLOv12 ou de outras fontes confiáveis e colocá-los no diretório raiz do seu projeto ou em um local acessível.

## 🤝 Contribuição

Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novos recursos.

## 📄 Citação

Se você usar este trabalho em sua pesquisa, por favor, cite o artigo original do YOLOv12:

```BibTeX
@article{tian2025yolov12,
  title={YOLOv12: Detectores de Objetos em Tempo Real com Foco em Atenção},
  author={Tian, Yunjie and Ye, Qixiang and Doermann, David},
  journal={arXiv preprint arXiv:2502.12524},
  year={2025}
}
```