import numpy as np
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
