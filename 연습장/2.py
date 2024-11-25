
import numpy as np
from math import sin, cos, atan2, sqrt, pi

class ReedsSheppPath:
    def __init__(self, start, goal, turning_radius):
        self.start = start
        self.goal = goal
        self.turning_radius = turning_radius

    def compute_path(self):
        paths = []
        for path_type in self.get_path_types():
            path = self.calculate_path(path_type)
            if path:
                paths.append(path)

        # 최단 경로 선택
        best_path = min(paths, key=lambda p: p['length'])
        return best_path

    def get_path_types(self):
        # Reeds-Shepp의 48가지 기본 경로 유형을 반환
        return [
            # 예시: LRL, RLR, LSL, RSR 등의 경로 유형을 여기에 추가
        ]

    def calculate_path(self, path_type):
        # 주어진 경로 유형에 따라 경로 계산
        # L, S, R은 각각 좌회전, 직선, 우회전을 의미
        # 이 부분에서 각 경로 유형에 따라 세그먼트를 계산하고
        # 전체 경로의 길이를 반환
        return {'type': path_type, 'length': calculated_length}

def main():
    start = (0, 0, 0)  # 시작 좌표 및 방향 (x, y, theta)
    goal = (10, 10, pi/2)  # 목표 좌표 및 방향 (x, y, theta)
    turning_radius = 1.0  # 최소 회전 반경

    rs_path = ReedsSheppPath(start, goal, turning_radius)
    best_path = rs_path.compute_path()
    print(f"Best path type: {best_path['type']} with length {best_path['length']}")

if __name__ == "__main__":
    main()
from scipy.special import erfc

# OFDM QPSK 및 LDPC 파라미터
subcarrier_count = 600  # 예: 10 MHz 대역폭에서 15 kHz 간격
ldpc_rate = 5/6         # LDPC 코딩율
symbol_per_packet = 1200
snr_db_range = np.arange(0, 40, 0.1)  # SNR 범위 (dB)

# QPSK 심볼 생성
def generate_qpsk_symbols(num_symbols):
    symbols = (np.random.randint(0, 2, num_symbols) * 2 - 1) + 1j * (np.random.randint(0, 2, num_symbols) * 2 - 1)
    return symbols / np.sqrt(2)  # 에너지 정규화

# AWGN 채널 적용
def apply_awgn(signal, snr_db):
    snr_linear = 10**(snr_db / 10)
    noise_power = np.mean(np.abs(signal)**2) / snr_linear
    noise = np.sqrt(noise_power / 2) * (np.random.randn(*signal.shape) + 1j * np.random.randn(*signal.shape))
    return signal + noise

# LDPC 디코딩 (간단화된 비율 계산)
def ldpc_decode(packet, ldpc_rate):
    # LDPC 디코딩 성공 여부를 단순화해 PER 추정
    return np.random.rand() > ldpc_rate

# PER 계산
def simulate_per(snr_db):
    error_count = 0
    packet_count = 1000  # 테스트 패킷 수
    for _ in range(packet_count):
        symbols = generate_qpsk_symbols(symbol_per_packet)
        received_signal = apply_awgn(symbols, snr_db)
        if not ldpc_decode(received_signal, ldpc_rate):
            error_count += 1
    return error_count / packet_count

# SNR 값에 따른 PER 계산
per_results = []
for snr_db in snr_db_range:
    per = simulate_per(snr_db)
    per_results.append(per)
    print(f"SNR(dB): {snr_db}, PER: {per}")

# SNR 찾기 (PER = 0.1)
target_snr = snr_db_range[np.argmin(np.abs(np.array(per_results) - 0.1))]
print(f"PER = 0.1을 만족하는 SNR 값: {target_snr} dB")
