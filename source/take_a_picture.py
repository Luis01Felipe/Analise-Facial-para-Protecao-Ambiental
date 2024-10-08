import cv2
import os


def tirar_foto():
    # Caminho onde a imagem será salva
    save_path = 'faces/analyzing'

    # Verifica se a pasta existe, caso contrário, cria
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Carregar o classificador em cascata para detecção de rostos
    face_cascade = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')

    # Abrir a webcam
    cap = cv2.VideoCapture(0)

    # Captura uma imagem
    ret, frame = cap.read()

    # Verifica se a captura foi bem-sucedida
    if not ret:
        print("Não foi possível capturar a imagem.")
    else:
        # Converter a imagem para escala de cinza
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detectar rostos na imagem
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        # Desenhar retângulos ao redor dos rostos detectados
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Mostrar a imagem com os rostos detectados
        cv2.imshow('faces Detectados', frame)

        # Salvar a imagem capturada na pasta 'faces/analyzing'
        image_path = os.path.join(save_path, 'imagem_capturada.jpg')
        cv2.imwrite(image_path, frame)
        print(f"Imagem salva em: {image_path}")

    # Libera a webcam e fecha as janelas
    cap.release()
    cv2.destroyAllWindows()


# Exemplo de uso
tirar_foto()
