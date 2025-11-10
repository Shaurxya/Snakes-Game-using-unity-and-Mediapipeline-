import socket, struct, cv2, mediapipe as mp
import math

SERVER_IP = "127.0.0.1"
PORT = 5060
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.3, min_tracking_confidence=0.3, max_num_hands=1)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print(f"🟢 Sending hand data to Unity on port {PORT}")

def count_fingers(hand_landmarks):
    """Return number of fingers extended (1–5)."""
    tips = [4, 8, 12, 16, 20]
    mcp = [2, 5, 9, 13, 17]
    count = 0
    for tip, base in zip(tips[1:], mcp[1:]):  # skip thumb for simplicity
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[base].y:
            count += 1
    return count

while True:
    success, frame = cap.read()
    if not success:
        continue
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    res = hands.process(rgb)

    x_val = -1.0
    finger_count = 0

    if res.multi_hand_landmarks:
        hand = res.multi_hand_landmarks[0]
        x_val = hand.landmark[8].x  # index fingertip
        finger_count = count_fingers(hand)

        mp_drawing.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)
        cv2.putText(frame, f"Fingers: {finger_count}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        cv2.putText(frame, f"X={x_val:.2f}", (20, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

    # send X and fingerCount (float + int)
    data = struct.pack("fi", x_val, finger_count)
    sock.sendto(data, (SERVER_IP, PORT))

    cv2.imshow("MediaPipe Hand", frame)
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
sock.close()
cv2.destroyAllWindows()
